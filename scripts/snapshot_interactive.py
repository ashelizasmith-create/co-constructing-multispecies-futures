#!/usr/bin/env python3
"""Preserve the reviewed Interactive Tool without replacing a numbered snapshot.

Run after browser QA:
    python scripts/snapshot_interactive.py

Validate version consistency without creating a snapshot:
    python scripts/snapshot_interactive.py --check

Only the Python standard library is required. The source HTML is copied byte for
byte. An existing identical snapshot is accepted; different bytes under the same
version are rejected so a published download cannot be silently replaced.
"""

from __future__ import annotations

import argparse
from datetime import date
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys


PROJECT_NAME = "Co-Constructing Multispecies Futures"
TOOL_LABEL = "Interactive Tool"
FILE_STEM = "Co-Constructing_Multispecies_Futures_Interactive"
VERSION_PATTERN = r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)"


class SnapshotError(ValueError):
    """A source or existing snapshot does not meet the release contract."""


class VisibleText(HTMLParser):
    """Read title, main heading, and visible version labels without running JS."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title_parts: list[str] = []
        self.heading_parts: list[str] = []
        self.visible_parts: list[str] = []
        self.in_title = False
        self.in_heading = False
        self.hidden_tag: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "title":
            self.in_title = True
        elif tag == "h1":
            self.in_heading = True
        elif tag in {"script", "style"}:
            self.hidden_tag = tag

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False
        elif tag == "h1":
            self.in_heading = False
        elif tag == self.hidden_tag:
            self.hidden_tag = None

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)
        if self.in_heading:
            self.heading_parts.append(data)
        if not self.hidden_tag:
            self.visible_parts.append(data)


def normal_text(parts: list[str]) -> str:
    return " ".join(" ".join(parts).split())


def js_string(source: str, name: str) -> str:
    """Require one unescaped, single-line string constant for release metadata."""
    pattern = rf"^\s*const\s+{re.escape(name)}\s*=\s*(['\"])([^\\\r\n]*?)\1\s*;"
    matches = re.findall(pattern, source, flags=re.MULTILINE)
    if len(matches) != 1:
        raise SnapshotError(f"Expected one literal {name} constant in site/interactive.html.")
    return matches[0][1]


def validated_source(root: Path) -> tuple[dict, bytes, Path]:
    version = (root / "VERSION").read_text(encoding="utf-8").strip()
    if not re.fullmatch(VERSION_PATTERN, version):
        raise SnapshotError("VERSION must contain a MAJOR.MINOR.PATCH number, such as 0.1.0.")

    metadata = json.loads((root / "site/version.json").read_text(encoding="utf-8"))
    if not isinstance(metadata, dict):
        raise SnapshotError("site/version.json must contain an object.")
    if metadata.get("version") != version:
        raise SnapshotError("VERSION and site/version.json disagree about the version.")
    if metadata.get("project_name") != PROJECT_NAME:
        raise SnapshotError("site/version.json does not use the current project name.")
    if not isinstance(metadata.get("status"), str) or not metadata["status"].strip():
        raise SnapshotError("site/version.json must supply a nonempty status.")
    version_date = metadata.get("date")
    try:
        if not isinstance(version_date, str) or date.fromisoformat(version_date).isoformat() != version_date:
            raise ValueError
    except ValueError as exc:
        raise SnapshotError("site/version.json date must use YYYY-MM-DD.") from exc

    source_bytes = (root / "site/interactive.html").read_bytes()
    source = source_bytes.decode("utf-8")
    expected_constants = {
        "PROJECT_NAME": PROJECT_NAME,
        "TOOL_LABEL": TOOL_LABEL,
        "APP_VERSION": version,
        "VERSION_STATUS": metadata["status"],
        "VERSION_DATE": version_date,
    }
    for name, expected in expected_constants.items():
        actual = js_string(source, name)
        if actual != expected:
            raise SnapshotError(f"{name} is {actual!r}; expected {expected!r} from the release metadata.")

    export_pattern = r"^\s*const\s+EXPORT_BASENAME\s*=\s*`([^`]+)`\s*;"
    export_names = re.findall(export_pattern, source, flags=re.MULTILINE)
    expected_export = "Co-Constructing_Multispecies_Futures_Session_v${APP_VERSION}"
    if export_names != [expected_export]:
        raise SnapshotError("Session export filenames must use the project name and APP_VERSION.")

    visible = VisibleText()
    visible.feed(source)
    visible.close()
    if normal_text(visible.title_parts) not in {PROJECT_NAME, f"{PROJECT_NAME} — {TOOL_LABEL}"}:
        raise SnapshotError("The HTML title does not match the current project name.")
    if normal_text(visible.heading_parts) != PROJECT_NAME:
        raise SnapshotError("The visible main heading does not match the current project name.")
    badge_pattern = rf"{re.escape(TOOL_LABEL)}\s*·\s*v({VERSION_PATTERN})\b"
    badge_versions = set(re.findall(badge_pattern, normal_text(visible.visible_parts)))
    if badge_versions != {version}:
        raise SnapshotError("The visible Interactive Tool version label does not match VERSION.")

    destination = root / "site/downloads" / f"{FILE_STEM}_v{version}.html"
    return metadata, source_bytes, destination


def existing_snapshot_matches(destination: Path, source_bytes: bytes) -> bool:
    if destination.is_symlink():
        raise SnapshotError(f"Refusing to use a symbolic link as the snapshot: {destination.name}.")
    if not destination.exists():
        return False
    if not destination.is_file() or destination.read_bytes() != source_bytes:
        raise SnapshotError(
            f"Refusing to overwrite {destination.name}: that version already has different contents. "
            "Assign a new version consistently before creating another snapshot."
        )
    return True


def snapshot(root: Path, *, check_only: bool = False) -> dict:
    metadata, source_bytes, destination = validated_source(root)
    already_exists = existing_snapshot_matches(destination, source_bytes)

    if already_exists:
        outcome = "unchanged"
    elif check_only:
        outcome = "ready"
    else:
        destination.parent.mkdir(parents=True, exist_ok=True)
        try:
            handle = destination.open("xb")
        except FileExistsError:
            # Another invocation may have created the same version since validation.
            if not existing_snapshot_matches(destination, source_bytes):
                raise SnapshotError("The snapshot path changed during creation; check it before retrying.")
            outcome = "unchanged"
        else:
            try:
                with handle:
                    handle.write(source_bytes)
            except OSError:
                # Remove only the partial file created by this invocation.
                destination.unlink(missing_ok=True)
                raise
            outcome = "created"

    return {
        "result": outcome,
        "version": metadata["version"],
        "status": metadata["status"],
        "date": metadata["date"],
        "snapshot": destination.relative_to(root).as_posix(),
        "bytes": len(source_bytes),
        "sha256": hashlib.sha256(source_bytes).hexdigest(),
        "check_only": check_only,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true", help="Validate without creating a snapshot.")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    try:
        result = snapshot(root, check_only=args.check)
    except (SnapshotError, OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"Snapshot not created: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
