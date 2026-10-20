#!/usr/bin/env python3
"""Export the canonical workshop log to CSV and the public history page.

Run from any directory: python3 scripts/export_workshop_log.py
Only site/data/workshops.json owns workshop data. The script uses the Python
standard library and leaves the page's navigation, styling, and prose intact.
"""
from __future__ import annotations

import argparse
import csv
from datetime import date
import html
import io
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "site/data/workshops.json"
CSV_PATH = ROOT / "site/data/workshops.csv"
PAGE_PATH = ROOT / "site/workshops.html"
BEGIN = "<!-- BEGIN GENERATED WORKSHOP LOG -->"
END = "<!-- END GENERATED WORKSHOP LOG -->"
FIELDS = [
    "id", "title", "connection_kind", "date_label", "event_start", "event_end",
    "date_basis", "place", "theme", "iteration", "evidence_status", "confidence",
    "unknowns", "sources",
]
GROUPS = [
    ("workshop", "Workshops & card use"),
    ("development", "Development contexts"),
    ("presentation", "Presentations"),
    ("related", "Related embodied practice"),
]
MONTHS = (
    "January", "February", "March", "April", "May", "June", "July", "August",
    "September", "October", "November", "December",
)


def validate(data: dict) -> None:
    """Reject ambiguous identifiers and malformed public-source links."""
    date.fromisoformat(data["updated"])
    if not isinstance(data.get("entries"), list):
        raise ValueError("The log must contain an entries array.")
    ids = set()
    for row in data["entries"]:
        if any(key not in row for key in FIELDS):
            raise ValueError(f"Entry is missing required fields: {row.get('id', '(no id)')}")
        ident = row["id"]
        if not isinstance(ident, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", ident):
            raise ValueError(f"Use a lowercase, hyphenated entry id: {ident!r}")
        if ident in ids:
            raise ValueError(f"Duplicate workshop id: {ident}")
        ids.add(ident)
        if row["connection_kind"] not in dict(GROUPS):
            raise ValueError(f"Unknown connection_kind in {ident}")
        for key in set(FIELDS) - {"event_start", "event_end", "sources"}:
            if not isinstance(row[key], str):
                raise ValueError(f"{ident}.{key} must be text.")
        for key in ("event_start", "event_end"):
            value = row[key]
            if value is None:
                continue
            if not isinstance(value, str) or not re.fullmatch(r"\d{4}(?:-\d{2}(?:-\d{2})?)?", value):
                raise ValueError(f"{ident}.{key} must be null, YYYY, YYYY-MM, or YYYY-MM-DD.")
            # Check the known components without supplying an unknown event date.
            date.fromisoformat(value + {4: "-01-01", 7: "-01", 10: ""}[len(value)])
        if not isinstance(row["sources"], list) or not row["sources"]:
            raise ValueError(f"Provide at least one source label for {ident}.")
        for source in row["sources"]:
            if not isinstance(source.get("label"), str) or not source["label"].strip():
                raise ValueError(f"A source label is missing in {ident}.")
            if source.get("url"):
                link = urlsplit(source["url"])
                if link.scheme not in ("http", "https") or not link.netloc:
                    raise ValueError(f"A source URL in {ident} must be a public HTTP(S) link.")


def csv_text(entries: list[dict]) -> str:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=FIELDS, lineterminator="\n")
    writer.writeheader()
    for entry in entries:
        row = {key: entry[key] for key in FIELDS}
        row["sources"] = " | ".join(
            source["label"] + (f" ({source['url']})" if source.get("url") else "")
            for source in entry["sources"]
        )
        writer.writerow(row)
    return output.getvalue()


def render_entry(entry: dict) -> str:
    e = {key: html.escape(str(value), quote=True) for key, value in entry.items() if key != "sources"}
    searchable = " ".join(entry[key] for key in (
        "title", "date_label", "place", "theme", "iteration", "evidence_status"
    )).lower()
    sources = []
    for source in entry["sources"]:
        label = html.escape(source["label"])
        if source.get("url"):
            url = html.escape(source["url"], quote=True)
            sources.append(f'<a href="{url}">{label} ↗</a>')
        else:
            sources.append(label)
    return (
        f'<article class="history-entry" id="{e["id"]}" data-kind="{e["connection_kind"]}" '
        f'data-search="{html.escape(searchable, quote=True)}">\n'
        f'<div class="history-date"><span>{e["date_label"]}</span>'
        f'<span class="history-status">{e["evidence_status"]}</span></div>\n'
        f'<div class="history-body"><h3>{e["title"]}</h3><p class="history-place">{e["place"]}</p>'
        f'<p>{e["iteration"]}</p><p class="history-theme">{e["theme"]}</p>'
        f'<details><summary>Source &amp; open details</summary><p>{e["unknowns"]}</p>'
        f'<p class="history-sources">{"<br>".join(sources)}</p></details></div></article>'
    )


def history_html(data: dict) -> str:
    updated = date.fromisoformat(data["updated"])
    label = f"{updated.day} {MONTHS[updated.month - 1]} {updated.year}"
    parts = [
        BEGIN,
        f'<p class="history-count" id="history-count" role="status" aria-live="polite" '
        f'data-updated="{label}">{len(data["entries"])} entries · updated {label}</p>',
        '<div id="history-list">',
    ]
    for kind, title in GROUPS:
        rows = [row for row in data["entries"] if row["connection_kind"] == kind]
        if not rows:
            continue
        parts.append(f'<section class="history-group" data-group="{kind}" aria-labelledby="heading-{kind}">'
                     f'<h2 id="heading-{kind}">{html.escape(title)}</h2>')
        if kind == "related":
            parts.append('<p class="group-note">These projects inform the wider embodied practice. '
                         'Their inclusion does not claim that every session used the card deck.</p>')
        parts.extend(render_entry(row) for row in rows)
        parts.append('</section>')
    parts.extend(['</div>', END])
    return '\n'.join(parts)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check that generated outputs are current without writing them.")
    args = parser.parse_args()
    try:
        data = json.loads(SOURCE.read_text(encoding="utf-8"))
        validate(data)
        page = PAGE_PATH.read_text(encoding="utf-8")
        if page.count(BEGIN) != 1 or page.count(END) != 1:
            raise ValueError("The history page must have exactly one generated-log marker pair.")
        page_output = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END),
                             lambda _: history_html(data), page, count=1, flags=re.S)
        outputs = {CSV_PATH: csv_text(data["entries"]), PAGE_PATH: page_output}
        stale = [path for path, content in outputs.items()
                 if not path.exists() or path.read_text(encoding="utf-8") != content]
        if args.check:
            if stale:
                print("Run python3 scripts/export_workshop_log.py to refresh: " +
                      ", ".join(str(path.relative_to(ROOT)) for path in stale), file=sys.stderr)
                return 1
            print(f"Workshop log is current: {len(data['entries'])} entries in JSON, CSV, and the history page.")
            return 0
        for path, content in outputs.items():
            path.write_text(content, encoding="utf-8", newline="")
        print(f"Exported {len(data['entries'])} entries to site/data/workshops.csv and site/workshops.html.")
        return 0
    except (OSError, ValueError, TypeError, KeyError) as exc:
        print(f"Workshop log: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
