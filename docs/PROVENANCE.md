# Source provenance

This inventory distinguishes original repository files, later supplied exports, and website adaptations. Historical filenames are recorded here as source evidence. The retained files now have descriptive project names; see [the filename map](FILE-NAMES.md). USDA identifies one workshop context, not the umbrella project or every use of the deck.

## Original repository snapshot

Inventory baseline: commit `2748be6bc6d6559c85034264a90c928c2d695786` (commit message: `Printable 2-sided cards`).

| File | Bytes | PDF pages | Purpose |
| --- | ---: | ---: | --- |
| `USDA_FullDeckwBleed_TextAsShapes_WithBleed.pdf` | 2,783,192 | 244 | Multispecies deck print export with outlined text. |
| `FullDeckNoBorder_WithBleed.pdf` | 4,289,252 | 200 | Related precision livestock farming deck print export with outlined text. |
| `SDL_WB_Engagement.png` | 177,454 | — | Existing project image; preserve its original file. |
| `LICENSE` | 7,048 | — | Existing CC0 1.0 Universal dedication; unchanged. |

Both repository PDFs have a 246 × 318 point media box. Their first-page trim boxes are `[33, 33, 213, 285]`, giving a **180 × 252 point / 2.5 × 3.5 inch** finished card. The first-page bleed boxes extend approximately 4.68 points beyond each trim edge. These are individual card sides with printer marks, not imposed Letter/A4 print sheets.

## Additional exports supplied for preparation

| Supplied filename | Bytes | PDF pages | Media size | Text extraction |
| --- | ---: | ---: | --- | --- |
| `USDA_FullDeckwBleed_EditableText.pdf` | 518,960 | 244 | 180 × 252 pt | Live text appears on 122 pages; useful for extracting prompts. |
| `USDA_FullDeckwBleed_TextAsShapes.pdf` | 2,715,700 | 244 | 180 × 252 pt | No extractable live text; outlined visual reference. |
| `PLF2025_FullDeckNoBorder_WithBleed.pdf` | 4,331,253 | 200 | 246 × 318 pt | No extractable live text; outlined export. |

**These files are not byte-identical substitutes for the repository PDFs.** In particular, the supplied USDA exports use the card's finished dimensions as their media size, while the repository USDA export has a larger page with printer marks. File naming alone is not sufficient to choose a print master.

No claim of complete visual equivalence is made solely from matching page counts. Keep the selected source filename and PDF page number attached to extracted card data. Page counts include backs and other deck material, not just unique prompts.

## Deck structure

The multispecies source has **122 paired cards / 244 pages**. Odd pages are fronts and the following even pages are backs.

| Category | Paired cards | Original PDF page range, including backs |
| --- | ---: | --- |
| Spatial | 1 | 1–2 |
| Temporal | 1 | 3–4 |
| Affective | 14 | 5–32 |
| Narrative point of view | 7 | 33–46 |
| Narrative construction | 20 | 47–86 |
| More-than-human collaborator / relational and ontological | 16 | 87–118 |
| Pivot | 23 | 119–164 |
| Speculation, with food-system context | 10 | 165–184 |
| Ways of knowing | 12 | 185–208 |
| Facilitator instructions | 18 | 209–244 |

The PLF export has **100 paired cards / 200 pages**: 10 repeated instruction cards, 25 Mood, 30 Object, 25 Spark, and 10 repeated Narrative cards. Its instructions are present: they specify one Mood, three Objects, one Spark, and one Narrative. A Narrative card separately refers to three selected cards, so that historical inconsistency should be clarified in use guidance instead of silently rewriting the archival artwork.

## General selection derived for this website

`site/downloads/Multispecies_Futures_General_Cards.pdf` is a new **94-card / 188-page selection**, extracted from repository `USDA_FullDeckwBleed_TextAsShapes_WithBleed.pdf`. It contains original pages **1–164 and 185–208**, preserving their order, layouts, and PDF page boxes. It excludes the 10 contextual Speculation cards and the 18 historical facilitator cards. It is a selection of existing artwork, not a redesigned deck.

The original full deck remains available. The website's modular guidance supplies the newer spatial/temporal starting mode; this should not be presented as the sole historical workshop protocol. Historical materials also describe starting from Construction, Tone/Mood, and Speculation.

The selected PDF is 1,975,924 bytes; its SHA-256 is `b0ca7b59bc14107348f6bcd54b55a273f839dc1103e26dc5d80d299733668f53`. The [download manifest](../site/data/download-manifest.json) maps each selected card to its original page and records the public download names. Recompute this value if the derivative changes.

## Home-print derivatives

The home-print editions impose the same 94 selected cards onto ordinary paper. They are separately named derivatives; the individual-card print master remains available.

| Filename in `site/downloads/` | Paper and method | PDF pages / physical sheets | Cards per sheet |
| --- | --- | --- | ---: |
| `Multispecies_Futures_Home_Print_Letter_Fold.pdf` | US Letter, single-sided fold | 32 / 32 | 3 |
| `Multispecies_Futures_Home_Print_A4_Fold.pdf` | A4, single-sided fold | 32 / 32 | 3 |
| `Multispecies_Futures_Home_Print_Letter_Duplex.pdf` | US Letter, duplex | 32 / 16 | 6 |
| `Multispecies_Futures_Home_Print_A4_Duplex.pdf` | A4, duplex | 32 / 16 | 6 |

All use actual-size printing at 100%. Duplex layouts are portrait and require long-edge flipping; fronts and backs remain adjacent in the PDF, so any instruction sheet must be printed separately. Single-sided layouts pair each front and back in a strip for cutting, folding with printed faces outward, and gluing. The final sheets include unused positions because 94 is not divisible by three or six.

The [home-print manifest](../site/data/home-print-manifest.json) records source checksums, final file checksums and sizes, and the card placements used for geometry, coverage, and front/back pairing checks.

Digital layout checks do not establish physical printer registration. Separate one-page instruction files are `Multispecies_Futures_Home_Print_Letter_Instructions.pdf` and `Multispecies_Futures_Home_Print_A4_Instructions.pdf`. Each includes a 72-point / 1-inch calibration square. Print the matching instructions and test a first sheet or duplex pair before a full run. A physical print proof has not been performed in this preparation environment.

## SHA-256 checksums

| File | SHA-256 |
| --- | --- |
| Repository `USDA_FullDeckwBleed_TextAsShapes_WithBleed.pdf` | `b6019dbd23e3290bd3114ec45316355e4c1ecae0934c7bc21b33a42c1693f8fa` |
| Repository `FullDeckNoBorder_WithBleed.pdf` | `ab7ff4e7bd3fb64cf75c54490fe72e9fad0b7c3d2835ef1e61228c7d2afa6ad2` |
| Repository `SDL_WB_Engagement.png` | `186dcd603bcf514239078aa8f309225d44d33647a631cc2589850242383ba3c3` |
| Repository `LICENSE` | `a2010f343487d3f7618affe54f789f5487602331c0a8d03f49e9a7c547cf0499` |
| Supplied `USDA_FullDeckwBleed_EditableText.pdf` | `60d9ff5905a1b8fed9f75526a84032e106091b7f74800e160591cf3d3e01f178` |
| Supplied `USDA_FullDeckwBleed_TextAsShapes.pdf` | `f54d4e40f40340c7715ec814de93e3646ce3c1c14d9c961e5957d7acd3449fe2` |
| Supplied `PLF2025_FullDeckNoBorder_WithBleed.pdf` | `cecd23108574bd0ed949d7c687e70e3170863cf6a6f71b657f0a258761bd84d0` |

Checksums identify the inspected bytes. A change to any file requires a new checksum and a description of the change.

## Working documents and public adaptation

The supplied working document has six tabs: Narrative; Epistemic; Pivot Cards (Make it); More-than-human; Introduction/Overview; and Tab 6. The first four contain prompt and use-method material. The introduction points to related presentations. The final tab contains working notes and is not public website copy.

Additional workshop guides describe the general method as collective worldbuilding, prototyping, and rehearsal. The 2026 FoodID and Nordic table guides identify the team as Ash Smith, Sam Bendix, and Julia McQuillan. The general guide uses Ash Eliza Smith and describes the three team members' roles. The exact release attribution is recorded for review in [ZENODO-DRAFT.md](ZENODO-DRAFT.md).

The separate document **“Futuring Speculative Design Co-Creation Guidelines and Card Deck”** was reviewed across all 23 tabs. Its **“One-Page over view of Speculative Devices Co-Creat”** tab (`t.vblnmf94gpxa`) uses the current project title and describes Invitation → Prototyping → Rehearsal, with Ash Eliza Smith, Sam Bendix, and Julia McQuillan as the team. This working guide supplies additional context; the project owner's later manuscript remains authoritative for the public methodological framing.

The FoodID tab **“hand out teachers FoodID 2026”** (`t.hb8osc4uuibs`) gives a specific workshop recipe. Participants recall a pleasant sensory food memory from ages four to seven and share only as comfortable, imagine a food-system dream in 2046, and create a blank-card “What if, in 2046…” prompt. Each group then selects one Narrative: Constructions, one Speculation, and one Affect card; self-authored fantasy cards can supply the speculation prompt. Groups compose a two- or three-sentence sensory story set in 2046 and write it on sticky paper to share. The dated workshop context is June 22–23, 2026. Although introductory timing language varies, the activities consistently name 2046. This contextual recipe does not establish the only way to use the toolkit, and the three embodied approaches come from the manuscript rather than this handout.

Other tabs retain different workshop settings. The October 24, 2025 robotics instructions use Nebraska in **2050**, and the April 23, 2026 Nordic sensory table guide also uses **2050** for its food-fantasy and group-story exercise. Keep those horizons attached to their own workshop editions; they do not replace FoodID's **2046** setting.

An additional instructions document contains differing About Us drafts, including a possible Lisa PytlikZilig credit. That uncertainty remains visible in the release draft and has not been converted into a final creator roster. The workshop materials describe a Speculative Devices Lab × Edgeworks production context; exact institutional wording and relevance to each release component remain to be checked.

A visually inspected FoodID Helsinki/VTT title slide dated October 27, 2025, embedded in tab `t.2qug0wjmftr9` of the 23-tab guide, explicitly credits **activity design** to Ash Smith, Sam Bendix, Julia McQuillan, and Lisa PytlikZillig. This is direct evidence for that activity, with the two-l spelling PytlikZillig. It does not by itself resolve the complete toolkit's creator roster. The slide's contextual credit is retained in the source review without publishing participant information from neighboring slides.

Working documents, meeting transcripts, participant information, and contextual notes have not been copied wholesale into this repository. Source documents can contain proposed language or credit for a specific workshop; neither automatically establishes a final claim for the complete toolkit.

## Authoritative manuscript for public framing

The project owner supplied `451Smith_McQuillan_Performing_the_What-If_final_pass.docx` and directed that its account of the deck guide this work. The manuscript remains outside the public repository and release package. This documentation uses a short, curated overview rather than reproducing it.

The owner subsequently clarified that **Performing the What-If: Embodied Worldbuilding with More-than-Human Intelligences, from Roleplay to Emerging Technologies**, by **Ash Eliza Smith and Julia McQuillan**, is a **forthcoming chapter in *Strategic Handbook of Worldbuilding* (Routledge) and is not yet public**. The book title and publisher come from the project owner's publication update. Editors, publication year, page range, public URL, and chapter DOI remain unspecified. Public-facing metadata is in [publications.json](../site/data/publications.json), with a short [paper overview](../site/paper.html). The README's `paper-and-tools` heading provides a durable entry point from the chapter to the tools.

Its methodology section identifies the card deck and interactive site as shared tools for building and telling speculative scenes, explicitly building on *The Thing From The Future* (Candy & Watson, 2014) and the *Rehearsing Realities* framework (Smith, Leadabrand, et al., in press). Its wider practice moves iteratively between discussion and imagination, embodied rehearsal, reflection, and writing or making.

The manuscript describes encountering, moving with, and becoming-with as overlapping modes. The public guide keeps their embodied and relational meaning: attend to another being's constraints, notice where it resists expectation, and return to discuss what happened. Participation can change through scale, orientation, attention, and constraint; it does not require all bodies to move alike. Rehearsal can generate further work or remain unresolved.

The intended audiences named in the manuscript are facilitators, designers, artists, organizers, educators, researchers, and community partners. The manuscript's author line is not a deck credit statement, and the authors of a cited framework are not automatically deck creators. Formal release attribution remains a separate decision.

## Supplied interactive source

The project owner supplied `futures_machinenew.html`. Its original bytes are preserved in `originals/Co-Constructing_Multispecies_Futures_Interactive_Imported.html`; the active working copy is now `site/interactive.html`.

| Original file property | Value |
| --- | --- |
| Bytes | 39,181 |
| SHA-256 | `6dbd640be639547ff62324d8590faef132b7583b5f3d0b59735a54fdfc18c930` |
| HTML page title | Co-Creating Multispecies Worlds |
| Title within source credit paragraph | Co-Constructing Multispecies Worlds |
| Umbrella project / repository title | Co-Constructing Multispecies Futures |

The imported source retains its original bytes and internal titles under its new descriptive filename. Its supplied filename is recorded above and in the filename map. At the project owner's request, the active project is titled **Co-Constructing Multispecies Futures**, with **Card Deck** and **Interactive Tool** as its two format labels. The current Interactive Tool path is `site/interactive.html`; the earlier working path `site/futures-machine.html` has been replaced. This naming change does not alter the preserved original bytes or credit names.

The original's default bank contains 84 options across nine layers: Spatial (10), Temporal (10), Affect (10), Voice (8), Form (10), Collaborator (8), Pivot (8), Speculation (10), and Sensing (10). This is an **adapted bank**, separate from the 94 physical cards in the general selection and the 122 paired cards in the full original deck.

The source supplies spatial/temporal defaults, optional layers, a lever-based draw, locks, custom text, Tell it / Now: try it areas, and local microphone-recording code. The integrated version adds current-slip and notes export as text or JSON and printing of the current slip and notes. JSON includes the current prompts, active layers and locks, adapted prompt bank, and embodied prompt. It is not a saved session history or an import system. Edits and recordings remain in the page session; users must download what they want to keep, with audio downloaded separately. No participant stories or recordings are uploaded by the app.

The original and integrated copies remain separately identifiable. The preserved original's checksum was verified against the supplied file. **0.1.0** is the first tracked development version; its snapshot remains unchanged. **0.1.1** preserves navigation, orientation, and citation improvements. **0.1.2** is the current source and adds the confirmed book metadata and an Examples navigation link. All three snapshots are retained in `site/downloads/`.

| Standalone snapshot | Bytes | SHA-256 |
| --- | ---: | --- |
| `Co-Constructing_Multispecies_Futures_Interactive_v0.1.0.html` | 55,421 | `5efdce2494d75c5f0c7e29a29ac6bd263d600a8a7a5378f28a8d5a8b40651254` |
| `Co-Constructing_Multispecies_Futures_Interactive_v0.1.1.html` | 57,084 | `fbc104a5a43dcebbd5c4d014f1aec251b1c8bfc7eabe551fc3bced0797c72ef2` |
| `Co-Constructing_Multispecies_Futures_Interactive_v0.1.2.html` | 57,290 | `0601ce6479e0144607a408f3edc77169e45ab559da7b2769adc4817b98d8c4bb` |

The 0.1.2 snapshot matches the current `site/interactive.html`. Its diff against 0.1.1 is limited to the version, two book-credit sentences, and the Examples navigation link; functional JavaScript is unchanged apart from `APP_VERSION`. The 0.1.0 and 0.1.1 snapshot checksums remain unchanged. Public deployment of 0.1.2 still requires verification. Baseline draw, hold, prompt editing, modal keyboard, and image-decoding checks are recorded in the changelog. The 0.1.1 browser check verified the homepage-to-citation path, exact clipboard citation, and the app's five-item navigation with a current-page label; other toolkit pages open in a new tab from the app to preserve the session. The private preview deployment was verified on October 20, 2026. Real microphone recording and physical printer registration remain untested.

Integration and usability changes preserve source credit names; the manuscript-informed overview adds the fuller methodological context. See [VERSIONING.md](VERSIONING.md), the [changelog](../CHANGELOG.md), and the [0.1.2 release draft](RELEASE-NOTES-v0.1.2.md).

The supplied credit paragraph says:

> Co-Constructing Multispecies Worlds was created by Ash Eliza Smith, developed in the Speculative Devices Lab with Julia McQuillan and Sam Bendix. This tool draws on that deck and a wider lineage of visionary card decks — including The Thing From The Future by Stuart Candy and Jeff Watson — and will continue to be developed and updated.

This is direct attribution evidence from the supplied interactive file. It does not by itself settle the final creator order for a mixed-material Zenodo deposit. The release draft records the current integration changes and bounded test results; formal archival metadata remains pending.
