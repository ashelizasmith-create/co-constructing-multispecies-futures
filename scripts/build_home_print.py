"""Impose the 94 general cards for home printing, preserving source vector artwork.

Run from any directory: python scripts/build_home_print.py

Inputs are the repository's retained live-text PDF and cards.json. Original PDFs
are never modified. Fold files are single-sided; duplex files alternate complete
front and back sheets, mapped for portrait paper / flip on the long edge.
"""

from __future__ import annotations

import hashlib
import json
import math
from collections import Counter
from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"
OUTPUT = SITE / "downloads"
SOURCE = OUTPUT / "Multispecies_Futures_Original_LiveText.pdf"
DATA = SITE / "data" / "cards.json"
MANIFEST = SITE / "data" / "home-print-manifest.json"

CARD_W, CARD_H = 252.0, 180.0  # 3.5 x 2.5 inches, after rotating the source.
ROW_GAP = 18.0
COL_GAP = 12.0
INK = (0.14, 0.24, 0.38)
MUTED = (0.36, 0.39, 0.43)
GUIDE = (0.46, 0.48, 0.50)
PAPERS = {"Letter": (612.0, 792.0), "A4": (210 / 25.4 * 72, 297 / 25.4 * 72)}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def label(page, x, y, text, size=8.2, bold=False, color=INK):
    page.insert_text((x, y), text, fontsize=size,
                     fontname="hebo" if bold else "helv", color=color)


def paragraph(page, rect, text, size=10, color=INK, bold=False):
    result = page.insert_textbox(rect, text, fontsize=size,
                                fontname="hebo" if bold else "helv",
                                color=color, lineheight=1.35)
    if result < 0:
        raise ValueError(f"Text overflow: {text[:60]}")


def crop_marks(page, rect):
    """Keep all cutting guides outside the unchanged card artwork."""
    x0, y0, x1, y1 = rect
    gap, tick = 2, 6
    for x, direction in ((x0, -1), (x1, 1)):
        for y in (y0, y1):
            page.draw_line((x + direction * gap, y),
                           (x + direction * (gap + tick), y),
                           color=GUIDE, width=0.35)
    for y, direction in ((y0, -1), (y1, 1)):
        for x in (x0, x1):
            page.draw_line((x, y + direction * gap),
                           (x, y + direction * (gap + tick)),
                           color=GUIDE, width=0.35)


def add_card(page, source, source_page, rect):
    native = source[source_page - 1]
    if tuple(native.trimbox) != (0.0, 0.0, 180.0, 252.0):
        raise ValueError("Unexpected source trim geometry; do not rescale blindly.")
    # show_pdf_page uses positive counterclockwise rotation. Visually checked:
    # rotate=90 turns the downward-running source text into upright landscape.
    page.show_pdf_page(rect, source, source_page - 1,
                       clip=native.trimbox, rotate=90, keep_proportion=True)


def base_header(page, title, subtitle, settings):
    label(page, 42, 31, "CO-CONSTRUCTING MULTISPECIES FUTURES", 8.1, True)
    label(page, 42, 56, title, 20, True)
    label(page, 42, 74, subtitle, 8.7, color=MUTED)
    label(page, 42, 91, settings, 8.3, True)


def save_pdf(doc, name, title, subject):
    target = OUTPUT / name
    doc.set_metadata({"title": title, "subject": subject,
                      "creator": "Co-Constructing Multispecies Futures home-print layout",
                      "keywords": "print and play, multispecies, home printing, cards"})
    doc.save(target, garbage=4, deflate=True, clean=True)
    return target


def build_fold(source, cards, paper, dimensions):
    width, height = dimensions
    doc = fitz.open()
    pages = []
    sheets = math.ceil(len(cards) / 3)
    x0 = (width - CARD_W * 2) / 2
    fold_x = width / 2
    y0 = (height - (3 * CARD_H + 2 * ROW_GAP)) / 2 + 12
    for sheet, start in enumerate(range(0, len(cards), 3), 1):
        page = doc.new_page(width=width, height=height)
        chosen = cards[start:start + 3]
        base_header(page, "Print, fold, play",
                    f"{paper if paper == 'A4' else 'US Letter'} | 94 general cards | Sheet {sheet:02} of {sheets}",
                    "100% / Actual size | Single-sided | Fold each back behind its front")
        placements = []
        for row, card in enumerate(chosen):
            y = y0 + row * (CARD_H + ROW_GAP)
            front = fitz.Rect(x0, y, fold_x, y + CARD_H)
            back = fitz.Rect(fold_x, y, x0 + 2 * CARD_W, y + CARD_H)
            add_card(page, source, card["front_page"], front)
            add_card(page, source, card["back_page"], back)
            crop_marks(page, fitz.Rect(front.x0, y, back.x1, y + CARD_H))
            # The fold guides are in discarded gutters, not drawn over the art.
            page.draw_line((fold_x, y - 8), (fold_x, y - 2),
                           color=GUIDE, width=0.6, dashes="[2 2] 0")
            page.draw_line((fold_x, y + CARD_H + 2), (fold_x, y + CARD_H + 8),
                           color=GUIDE, width=0.6, dashes="[2 2] 0")
            label(page, x0 + 10, y - 7, f"{start + row + 1:02}  {card['category_label']} / FRONT", 6.8, color=MUTED)
            label(page, fold_x + 11, y - 7, "BACK / fold at the join", 6.8, color=MUTED)
            placements.append({"card_id": card["id"], "card_number": start + row + 1,
                               "front_source_page": card["front_page"],
                               "back_source_page": card["back_page"],
                               "front_rect_pt": list(front), "back_rect_pt": list(back),
                               "fold_x_pt": fold_x, "rotation_ccw": 90})
        label(page, 42, height - 58,
              "Cut each outer strip. Fold at the front/back join, printed sides out. Glue the blank insides.", 8.1)
        label(page, 42, height - 43,
              "Finished cards: 3.5 x 2.5 in / 88.9 x 63.5 mm. Print one PDF page per sheet; do not use Fit.", 7.5, color=MUTED)
        pages.append({"pdf_page": sheet, "sheet": sheet, "placements": placements,
                      "blank_pair_slots": 3 - len(chosen)})
    target = save_pdf(doc, f"Multispecies_Futures_Home_Print_{paper}_Fold.pdf",
                      f"Multispecies Futures - {paper} - Single-sided fold-and-glue",
                      "94 general cards, unchanged original vector artwork, three front/back strips per sheet.")
    return {"filename": target.name, "paper": paper, "method": "fold",
            "page_count": len(doc), "physical_sheets": sheets, "card_count": len(cards),
            "cards_per_sheet": 3, "print_sides": "single-sided", "recommended": True,
            "source_artwork": "live-text PDF, unchanged, rotated 90 degrees counterclockwise",
            "settings": "100% / Actual size; one page per sheet; no Fit, shrink, or booklet",
            "pages": pages, "bytes": target.stat().st_size, "sha256": sha256(target)}


def build_duplex(source, cards, paper, dimensions):
    width, height = dimensions
    doc = fitz.open()
    pages = []
    sheets = math.ceil(len(cards) / 6)
    grid_width = 2 * CARD_W + COL_GAP
    x0 = (width - grid_width) / 2
    y0 = (height - (3 * CARD_H + 2 * ROW_GAP)) / 2 + 12
    for sheet, start in enumerate(range(0, len(cards), 6), 1):
        chosen = cards[start:start + 6]
        for face in ("front", "back"):
            page = doc.new_page(width=width, height=height)
            pdf_page = len(doc)
            base_header(page, "Print front and back",
                        f"{paper if paper == 'A4' else 'US Letter'} | {face.upper()}S | Sheet {sheet:02} of {sheets} | PDF page {pdf_page:02} of {sheets * 2}",
                        "100% / Actual size | Two-sided | Flip on the long edge | Portrait")
            placements = []
            for index, card in enumerate(chosen):
                row, front_col = divmod(index, 2)
                col = front_col if face == "front" else 1 - front_col
                x = x0 + col * (CARD_W + COL_GAP)
                y = y0 + row * (CARD_H + ROW_GAP)
                rect = fitz.Rect(x, y, x + CARD_W, y + CARD_H)
                source_page = card[face + "_page"]
                add_card(page, source, source_page, rect)
                crop_marks(page, rect)
                label(page, x + 10, y - 7, f"{start + index + 1:02}  {card['category_label']} / {face.upper()}",
                      6.5, color=MUTED)
                placements.append({"card_id": card["id"], "card_number": start + index + 1,
                                   "source_page": source_page, "face": face,
                                   "row": row, "column": col, "rect_pt": list(rect),
                                   "rotation_ccw": 90})
            label(page, 42, height - 58,
                  "Test PDF pages 1-2 first. Check that each back lines up behind the matching front, then cut.", 8.0)
            footer = ("Back positions are reversed left to right for long-edge duplex printing. Do not mirror the artwork."
                      if face == "back" else
                      "Keep the PDF page order. Finished cards: 3.5 x 2.5 in / 88.9 x 63.5 mm. No Fit or booklet mode.")
            label(page, 42, height - 43, footer, 7.5, color=MUTED)
            pages.append({"pdf_page": pdf_page, "sheet": sheet, "face": face,
                          "placements": placements, "blank_card_slots": 6 - len(chosen)})
    target = save_pdf(doc, f"Multispecies_Futures_Home_Print_{paper}_Duplex.pdf",
                      f"Multispecies Futures - {paper} - Long-edge duplex",
                      "94 general cards; six cards per sheet; portrait long-edge duplex; paired front/back pages.")
    return {"filename": target.name, "paper": paper, "method": "duplex",
            "page_count": len(doc), "physical_sheets": sheets, "card_count": len(cards),
            "cards_per_sheet": 6, "print_sides": "two-sided", "recommended": False,
            "flip": "long-edge", "orientation": "portrait",
            "settings": "100% / Actual size; one page per side; no Fit, shrink, mirror, or booklet",
            "source_artwork": "live-text PDF, unchanged, rotated 90 degrees counterclockwise",
            "pages": pages, "bytes": target.stat().st_size, "sha256": sha256(target)}


def build_instructions(paper, dimensions):
    width, height = dimensions
    doc = fitz.open()
    page = doc.new_page(width=width, height=height)
    left, right = 48, width - 48
    label(page, left, 40, "CO-CONSTRUCTING MULTISPECIES FUTURES", 8.4, True)
    label(page, left, 74, "Make your card deck", 24, True)
    paragraph(page, fitz.Rect(left, 93, right, 132),
              "94 general cards. Original artwork, arranged for home printing. "
              "Choose the PDF that matches your paper: US Letter or A4.", 10.5)
    label(page, left, 154, "START HERE: PRINT, FOLD, GLUE", 10.5, True)
    paragraph(page, fitz.Rect(left, 169, right, 262),
              "1. Open the Fold PDF. Print single-sided, one page per sheet, at 100% or Actual size.\n"
              "2. Cut along the outside crop marks to make three long strips per sheet.\n"
              "3. Fold each strip at the join between front and back, keeping both printed sides out.\n"
              "4. Glue the blank insides together and press flat while drying.\n"
              "The full deck uses 32 sheets. The final sheet contains one card.", 10.0)
    label(page, left, 292, "HAVE A TWO-SIDED PRINTER?", 10.5, True)
    paragraph(page, fitz.Rect(left, 307, right, 411),
              "Use the Duplex PDF for six finished cards per sheet. Select portrait paper, "
              "two-sided printing and Flip on long edge. Keep the file's page order.\n"
              "Print PDF pages 1-2 as a test first. Hold the sheet to a light: each back should "
              "sit behind its matching front. If your printer shifts the two sides, use the Fold file.\n"
              "The full deck is 32 PDF pages on 16 sheets. Cut at the crop marks after printing.", 10.0)
    label(page, left, 441, "CHECK YOUR SCALE BEFORE PRINTING THE WHOLE DECK", 10.5, True)
    paragraph(page, fitz.Rect(left, 456, right, 501),
              "Print this page at 100% / Actual size and measure the square below. "
              "Turn off Fit, Shrink, multiple-pages-per-sheet and booklet settings. "
              "Select the matching paper size.", 10.0)
    square = fitz.Rect(left, 522, left + 72, 594)
    page.draw_rect(square, color=INK, width=0.5)
    paragraph(page, fitz.Rect(left + 90, 530, right, 592),
              "This square must measure\n1 inch x 1 inch\n25.4 mm x 25.4 mm", 11, bold=True)
    paragraph(page, fitz.Rect(left, 617, right, 676),
              "Finished card size: 3.5 x 2.5 inches / 88.9 x 63.5 mm.\n"
              "For fold-and-glue, ordinary paper works; the two glued layers make each card sturdier. "
              "For duplex, use card stock your printer supports.", 10.0)
    paragraph(page, fitz.Rect(left, 694, right, height - 32),
              "This calibration page is separate from the deck. It is not a cover sheet and "
              "should not be inserted into a duplex print job. Original prompts and artwork are unchanged.",
              8.2, color=MUTED)
    target = save_pdf(doc, f"Multispecies_Futures_Home_Print_{paper}_Instructions.pdf",
                      f"Multispecies Futures - {paper} - Printing instructions and scale check",
                      "Separate one-page home-print instructions with an exact 1-inch calibration square.")
    return {"filename": target.name, "paper": paper, "method": "instructions",
            "page_count": 1, "physical_sheets": 1, "calibration_square_pt": [72, 72],
            "bytes": target.stat().st_size, "sha256": sha256(target)}


def verify(entries, cards):
    ids = {c["id"] for c in cards}
    by_id = {c["id"]: c for c in cards}
    result = []
    for item in entries:
        doc = fitz.open(OUTPUT / item["filename"])
        width, height = PAPERS[item["paper"]]
        assert len(doc) == item["page_count"]
        assert all(abs(p.rect.width - width) < 0.01 and abs(p.rect.height - height) < 0.01 for p in doc)
        if item["method"] == "instructions":
            result.append({"filename": item["filename"], "geometry": "passed", "calibration": "72 x 72 pt"})
            continue
        expected_count = Counter({i: 1 for i in ids})
        fronts, backs = [], []
        if item["method"] == "fold":
            for page in item["pages"]:
                for place in page["placements"]:
                    fronts.append(place["card_id"])
                    backs.append(place["card_id"])
                    assert by_id[place["card_id"]]["front_page"] == place["front_source_page"]
                    assert place["back_source_page"] == place["front_source_page"] + 1
                    a, b = fitz.Rect(place["front_rect_pt"]), fitz.Rect(place["back_rect_pt"])
                    assert a.x1 == b.x0 == place["fold_x_pt"]
                    assert abs((b.x1 - b.x0) - CARD_W) < 0.001
                    assert abs(a.width - CARD_W) < 0.001 and abs(a.height - CARD_H) < 0.001
                    assert a.y0 == b.y0 and a.y1 == b.y1
                    assert a.x0 >= 36 and b.x1 <= width - 36
        else:
            assert len(doc) % 2 == 0
            for front, back in zip(item["pages"][::2], item["pages"][1::2]):
                assert front["face"] == "front" and back["face"] == "back"
                assert front["sheet"] == back["sheet"]
                for a, b in zip(front["placements"], back["placements"]):
                    assert a["card_id"] == b["card_id"]
                    fronts.append(a["card_id"])
                    backs.append(b["card_id"])
                    assert by_id[a["card_id"]]["front_page"] == a["source_page"]
                    assert b["source_page"] == a["source_page"] + 1
                    ra, rb = fitz.Rect(a["rect_pt"]), fitz.Rect(b["rect_pt"])
                    assert abs(ra.width - CARD_W) < 0.001 and abs(ra.height - CARD_H) < 0.001
                    assert abs(rb.width - CARD_W) < 0.001 and abs(rb.height - CARD_H) < 0.001
                    assert abs(ra.x0 - (width - rb.x1)) < 0.001
                    assert abs(ra.x1 - (width - rb.x0)) < 0.001
                    assert ra.y0 == rb.y0 and ra.y1 == rb.y1
                    assert ra.x0 >= 36 and ra.x1 <= width - 36
        assert Counter(fronts) == expected_count
        assert Counter(backs) == expected_count
        result.append({"filename": item["filename"], "geometry": "passed",
                       "unique_fronts": len(set(fronts)), "unique_backs": len(set(backs)),
                       "pair_mapping": "passed", "source_artwork": "vector import, no mirrored glyphs"})
    return result


def main():
    data = json.loads(DATA.read_text())
    cards = [c for c in data["cards"] if c.get("collection") == "general"]
    if len(cards) != 94 or len({c["id"] for c in cards}) != 94:
        raise ValueError("Expected exactly 94 distinct general-card IDs.")
    if any(c["kind"] != "prompt" or c["context_specific"] for c in cards):
        raise ValueError("General selection unexpectedly includes contextual or facilitator cards.")
    source_hash = sha256(SOURCE)
    source = fitz.open(SOURCE)
    assert len(source) == 244
    entries = []
    for paper, dimensions in PAPERS.items():
        entries.append(build_fold(source, cards, paper, dimensions))
        entries.append(build_duplex(source, cards, paper, dimensions))
        entries.append(build_instructions(paper, dimensions))
    checks = verify(entries, cards)
    assert source_hash == sha256(SOURCE)
    manifest = {
        "edition": "94 general cards, imposed for home printing",
        "source_file": SOURCE.name,
        "source_sha256": source_hash,
        "source_page_count": len(source),
        "card_count": 94,
        "finished_card_points": [CARD_W, CARD_H],
        "finished_card_inches": [3.5, 2.5],
        "artwork_policy": "Original vector artwork preserved; only orientation and sheet placement changed.",
        "default_method": "fold",
        "physical_printer_test": "Not performed. Print one test sheet before the complete deck.",
        "automated_checks": checks,
        "downloads": entries,
    }
    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    for item in entries:
        print(json.dumps({key: item[key] for key in ("filename", "page_count", "physical_sheets", "bytes")}))


if __name__ == "__main__":
    main()
