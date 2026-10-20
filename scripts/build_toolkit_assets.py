"""Build the review edition from supplied deck files; never overwrite originals.

Run from this repository with explicit --uploads and --audit paths.
Images use the cropped live-text source for clean gradient rendering; the selected print PDF preserves the original
repository PDF's trim/bleed geometry and front/back order.
"""
import argparse
import csv
import hashlib
import json
import shutil
from pathlib import Path

import fitz


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build(uploads, audit):
    repo = Path(__file__).resolve().parents[1]
    site = repo / "site"
    for directory in ("assets/cards", "data", "downloads"):
        (site / directory).mkdir(parents=True, exist_ok=True)
    data = json.loads((audit / "core-deck-cards.json").read_text())
    cropped = uploads / "USDA_FullDeckwBleed_EditableText.pdf"
    bleed = repo / "originals/Co-Constructing_Multispecies_Futures_Complete_Deck_Print.pdf"
    source = fitz.open(cropped)
    # Visual page review confirms these are extraction losses of the ft ligature.
    corrections = {3: [("shif-work", "shift-work")],
                   101: [("ofen", "often")],
                   215: [("ofen", "often")],
                   219: [("ofen", "often")],
                   227: [("shif,", "shift,")],
                   243: [("Afer", "After")]}
    for card in data["cards"]:
        page = card["front_page"]
        card["display_text"] = card["source_text"]
        card["search_text"] = card["text"]
        for before, after in corrections.get(page, []):
            card["display_text"] = card["display_text"].replace(before, after)
            card["search_text"] = card["search_text"].replace(before, after)
        card["collection"] = ("facilitator" if card["kind"] == "instruction"
                               else "food-systems" if card["context_specific"]
                               else "general")
        for face in ("front", "back"):
            number = card[face + "_page"]
            rel = f"assets/cards/{number:03d}.webp"
            # Body text is rotated clockwise in the print source.
            pix = source[number - 1].get_pixmap(matrix=fitz.Matrix(3, 3).prerotate(-90), alpha=False)
            pix.pil_save(str(site / rel), format="WEBP", quality=88)
            card[face + "_image"] = rel
    data["original_source_filename"] = cropped.name
    data["source_file"] = "Multispecies_Futures_Original_LiveText.pdf"
    for card in data["cards"]:
        card["source_file"] = data["source_file"]
    data["edition"] = "Working web edition; original card wording retained"
    data["general_cards"] = sum(c["collection"] == "general" for c in data["cards"])
    data["digital_adaptation_note"] = (
        "The Play view samples combinations from examples on the single Spatial and "
        "Temporal cards. Other layers draw complete original cards. A card with several "
        "options remains one card; participants choose one or combine them. Food-system "
        "speculations are a separate contextual collection."
    )
    (site / "data/cards.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    (site / "data/cards.js").write_text("window.TOOLKIT_DATA = " + json.dumps(data, ensure_ascii=False) + ";\n")
    with (site / "data/cards.csv").open("w", newline="", encoding="utf-8-sig") as f:
        fields = ["id", "category_label", "collection", "front_page", "back_page", "display_text", "source_file"]
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(data["cards"])

    original = fitz.open(bleed)
    selected = fitz.open()
    mapping = []
    for card in data["cards"]:
        if card["collection"] == "general":
            out_page = len(selected) + 1
            selected.insert_pdf(original, from_page=card["front_page"]-1, to_page=card["back_page"]-1)
            mapping.append({"card_id": card["id"], "original_front": card["front_page"], "selected_front": out_page})
    selected.set_metadata({"title": "Co-Constructing Multispecies Futures - General Cards (working selection)",
                           "subject": "94 original general-purpose cards, preserving paired fronts and backs and print geometry"})
    general_pdf = site / "downloads/Multispecies_Futures_General_Cards.pdf"
    selected.save(general_pdf, garbage=4, deflate=True)
    copies = [
        (bleed, "Multispecies_Futures_Original_Print.pdf"),
        (uploads / "USDA_FullDeckwBleed_EditableText.pdf", "Multispecies_Futures_Original_LiveText.pdf"),
        (uploads / "USDA_FullDeckwBleed_TextAsShapes.pdf", "Multispecies_Futures_Original_Outlined.pdf"),
        (uploads / "PLF2025_FullDeckNoBorder_WithBleed.pdf", "PLF2025_Workshop_Deck.pdf"),
    ]
    manifest = []
    for path, name in copies:
        target = site / "downloads" / name
        shutil.copy2(path, target)
        manifest.append({"download": name, "source_filename": path.name, "sha256": digest(target), "bytes": target.stat().st_size})
    shutil.copy2(repo / "LICENSE", site / "downloads/EXISTING-REPOSITORY-LICENSE.txt")
    shutil.copy2(repo / "originals/Co-Constructing_Multispecies_Futures_Workshop_Image.png", site / "assets/workshop-cards.png")
    manifest.append({"download": general_pdf.name, "source_filename": bleed.name,
                     "sha256": digest(general_pdf), "bytes": general_pdf.stat().st_size,
                     "derivation": "General activity cards only; unchanged artwork and page boxes. No contextual speculation or old facilitator sequence.",
                     "page_count": len(selected), "card_count": len(mapping), "page_mapping": mapping})
    (site / "data/download-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps({"all_cards": len(data["cards"]), "general_cards": len(mapping), "general_pdf_pages": len(selected), "assets": len(source), "downloads": len(manifest)}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--uploads", required=True, type=Path)
    parser.add_argument("--audit", required=True, type=Path)
    args = parser.parse_args()
    build(args.uploads, args.audit)
