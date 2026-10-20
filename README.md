# Co-Constructing Multispecies Futures

An evolving toolkit for imagining and rehearsing multispecies futures through chance, affect, storytelling, and embodied play. Available as a **Card Deck** and **Interactive Tool**.

[Website](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/) · [Interactive Tool](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/interactive.html) · [Print the cards](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/index.html#print) · [Facilitation guide](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/guide.html) · [How to cite](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/paper.html#cite) · [Workshop history](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/workshops.html) · [Versions](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/versions.html)

## Overview

Build and tell speculative scenes, then enter them through roleplay, movement, and rehearsal. Return to talking, sketching, or writing with what the body noticed. The toolkit supports facilitators, designers, artists, organizers, educators, researchers, and community partners working with more-than-human others: animals, plants, machines, ecosystems, and infrastructures.

The deck and interactive site build on **The Thing From The Future** (Candy & Watson, 2014) and the **Rehearsing Realities** framework (Smith, Leadabrand, et al., in press). The wider practice draws on performance, dance and somatic practice, walking scores, speculative design, spatial storytelling, playable theater, and immersive practice. See [Paper and tools](#paper-and-tools) for the conceptual relationship and references.

Use the toolkit across settings. Food-system, USDA, and precision livestock farming materials document particular workshop contexts within its development. The original editions remain available alongside the general selection.

## Quickstart

### Use the Interactive Tool

1. Open [the Interactive Tool online](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/interactive.html). To keep a standalone copy, use [the version-history download](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/versions.html#v0-1-2) or save [the version 0.1.2 HTML](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/downloads/Co-Constructing_Multispecies_Futures_Interactive_v0.1.2.html) and open the saved file in a browser.
2. Begin with **Spatial** and **Temporal**. Pull to draw a combination, hold a result you want to keep, and add optional layers.
3. Use **Tell it** to write, then **Now: try it** to take the scene into movement, attention, or rehearsal.
4. Save your session slip and notes as text or JSON, or print them. Download voice recordings separately before closing or reloading the page.

The tool runs in the browser with JavaScript. Notes, prompt edits, and recordings remain in the page session; there is no automatic session history. Microphone recording depends on browser support and permission. The adapted prompt bank is separate from the complete physical-card corpus.

### Run the complete website locally

The website is static HTML, CSS, and JavaScript; no build step or package installation is required. With Git and Python 3 available:

```sh
git clone https://github.com/ashelizasmith-create/co-constructing-multispecies-futures.git
cd co-constructing-multispecies-futures
python3 -m http.server 8000 --directory site
```

Open <http://localhost:8000/> to browse the cards, use the tool, and read the guide locally. The [public website](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/) is also live on GitHub Pages. See [publishing guidance](docs/PUBLISHING.md) for deployment records and future updates.

## Formats and printing

### Card Deck

| Edition | Contents | Download |
| --- | --- | --- |
| General selection | 94 activity cards / 188 sides; original artwork selected for use across settings. | [Individual-card print PDF](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/downloads/Multispecies_Futures_General_Cards.pdf) |
| Complete multispecies source | 122 paired cards: 94 general activity cards, 10 food-system speculation cards, and 18 facilitator cards. | [Original print edition](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/downloads/Multispecies_Futures_Original_Print.pdf) · [PDF with live text](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/downloads/Multispecies_Futures_Original_LiveText.pdf) |
| PLF workshop edition | 100 paired cards / 200 sides; a related precision livestock farming edition with its own categories and repeated instruction cards. | [PLF PDF](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/downloads/PLF2025_Workshop_Deck.pdf) |
| Accessible card text | 122 source-card entries with categories, transcriptions, and original page references. | [CSV](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/data/cards.csv) · [JSON](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/data/cards.json) |

For ordinary printers, choose a **home-print edition of the 94-card general selection**:

| Paper | Single-sided fold | Duplex | Print guide |
| --- | --- | --- | --- |
| US Letter | [Letter fold PDF](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/downloads/Multispecies_Futures_Home_Print_Letter_Fold.pdf) · 32 sheets | [Letter duplex PDF](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/downloads/Multispecies_Futures_Home_Print_Letter_Duplex.pdf) · 16 sheets | [Letter instructions](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/downloads/Multispecies_Futures_Home_Print_Letter_Instructions.pdf) |
| A4 | [A4 fold PDF](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/downloads/Multispecies_Futures_Home_Print_A4_Fold.pdf) · 32 sheets | [A4 duplex PDF](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/downloads/Multispecies_Futures_Home_Print_A4_Duplex.pdf) · 16 sheets | [A4 instructions](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/downloads/Multispecies_Futures_Home_Print_A4_Instructions.pdf) |

Print at **Actual size / 100%** on the matching paper size. Turn off Fit, Shrink, Multiple pages per sheet, and Booklet settings. Finished cards measure **3.5 × 2.5 inches**.

- **Fold:** print one-sided, cut the three front/back strips on each sheet, fold with the printed faces outward, and glue the blank interiors together.
- **Duplex:** print portrait with **Flip on long edge**. The 32 PDF pages make 16 sheets with six cards per sheet. Test pages 1–2 first.
- **Calibration:** print the separate instructions and measure the 1-inch square. Keep instruction pages outside the duplex card PDF so front/back pairing stays intact.

Individual-card print PDFs retain production page boxes and crop marks for a print provider to arrange on sheets. The live-text PDF has selectable text; it is not the editable design source. See [provenance](docs/PROVENANCE.md) for export differences, page mappings, and checksums. A physical proof is still needed for the printer being used.

### Interactive Tool

[Open the current tool online](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/interactive.html) or visit [version history](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/versions.html) to choose a numbered standalone download. The stable online tool path serves the current version; numbered HTML files preserve earlier reviewed versions. The browser for the original cards is in [the complete website](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/index.html#deck).

## Usage

1. **Agree on a situation.** Begin with a place and a time, or a question the group wants to explore.
2. **Choose layers.** Add affect, point of view, form, or a more-than-human collaborator. Choose one option from a multi-prompt card, or deliberately work with a combination.
3. **Build a scene together.** Tell, draw, write, sound, or stage it. Leave room for everyone to contribute and for the more-than-human participant to resist an expected role.
4. **Enter and revise it.** Try a different rhythm, scale, orientation, constraint, or relation. Use a Pivot when a change would help.
5. **Return and reflect.** Discuss or write what changed, what surprised you, and what you want to carry into another rehearsal. Mark the ending as well as the beginning.

**Encountering**, **moving with**, and **becoming-with** are overlapping approaches, not a required sequence. Adapt movement to the people present. Taking up another position remains partial; it does not give full access to another being's experience. A rehearsal may become a story, artwork, prototype, or technology—or remain a gesture, question, or unresolved experience.

For an optional food-system recipe, the FoodID handout begins with a pleasant sensory memory, invites each person to write a “What if, in 2046…” future-fantasy card, then has each group choose Construction, Speculation, and Affect prompts for a two- or three-sentence sensory story. This setting belongs to that workshop; groups can choose another horizon.

See the [printable use guide](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/guide.html) for a longer session and [the paper overview](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/paper.html) for the methodological framing.

### Examples and visual guidance

The [Examples page](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/examples.html) brings together **25 images** with source context, captions, credits, and image descriptions: all three owner-authorized manuscript figures, MuMu, The Middle, workshop and robotic practice, and six teaching images. These document related practices as well as card sessions; inclusion does not establish that the deck was used in every image. The homepage now uses photographs and card previews to make the routes into the tool, printing, and facilitation easier to recognize. The expanded guide presents eight original instruction-card images with their text and links to the complete 18-card sequence.

A separate [community preparation preview](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/downloads/Co-Constructing_Multispecies_Futures_Community_Preparation_v0.1.0.html), version **0.1.0**, prepares an image, credit, alt text, and reflection in the browser for download. It does **not** upload, receive, review, or publish contributions. The preview is available through the Examples page and processes the chosen image locally. Its [source notes and connected-form specification](integrations/community/README.md) describe a future submission flow; no form account or submission endpoint is configured.

## Repository structure

| Path | Purpose |
| --- | --- |
| `site/index.html` | Visually guided toolkit homepage, original-card browser, downloads, and use guidance. |
| `site/interactive.html` | Current Interactive Tool. |
| `site/guide.html` | Printable facilitation guide with eight original instruction-card images and text, plus the complete source-sequence index. |
| `site/paper.html` | About & cite: framework orientation, development citation, lineages, and the forthcoming chapter. |
| `site/examples.html`, `site/data/examples.json` | 25-image Examples collection with source context, captions, credits, image descriptions, and reuse information. |
| `site/workshops.html` | Searchable working history of workshops, development contexts, presentations, and related practice. |
| `site/versions.html` | Version history and numbered tool downloads. |
| `site/data/workshops.json` | Single editable source for the 25-entry workshop and development log; generates its CSV and public history entries. |
| `site/downloads/` | Print files, instructions, and versioned HTML snapshots. |
| `site/data/` | Card text, publication metadata, and download/provenance manifests. |
| `site/assets/` | Card images, shared styles, and browser code. |
| `originals/` | Byte-preserved supplied interactive source; historical identity is documented in provenance. |
| `scripts/` | Asset preparation, home-print generation, workshop-log exports, and guarded interactive snapshots. |
| `docs/` | Provenance, versioning, publishing guidance, release checklist, and draft archival metadata. |
| `integrations/indexhibit/` | Ready-to-paste exhibit content and installation notes for the existing portfolio page. |
| `integrations/community/` | Local image-preparation preview v0.1.0, downloadable notes/package workflow, and an unconfigured connected-form specification. |
| `.github/workflows/pages.yml` | GitHub Actions deployment of `site/` to the verified public website. |
| `VERSION`, `site/version.json` | Current development version information. |

Original repository PDFs, the workshop image, and the imported interactive source are retained under descriptive names in `originals/`. The [filename map](docs/FILE-NAMES.md) records their earlier names and unchanged checksums. To add or correct an event, follow [Keeping the workshop log](docs/WORKSHOP-LOG.md); edit its JSON source, then regenerate the CSV and page.

## Versions and changelog

The current source version is **0.1.2**, with a 25-image Examples collection, a visually guided homepage, original instruction-card guidance, confirmed book metadata, clearer source filenames, and a 25-entry workshop log maintained from one JSON source. It also includes the separately versioned **0.1.0 local community preparation preview**. The **0.1.0** and **0.1.1** Interactive Tool downloads remain preserved. Fixes advance the patch number; features or new prompt layers advance the minor number, such as **0.2.0**. **1.0.0** will be a deliberate stable release.

See [version history](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/versions.html), the [changelog](CHANGELOG.md), and the [versioning policy](docs/VERSIONING.md). After browser QA, the snapshot command preserves the reviewed HTML and refuses to replace different contents under an existing version number. Selected releases can be archived in Zenodo; routine commits do not require a new DOI. Current verification and publication status is recorded in the [release checklist](docs/RELEASE-CHECKLIST.md).

The [public website](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/) is verified live at **0.1.2**, deployed from commit `8215b73e2f65f383e981c16a7949e1e430e99f3a` by successful [Pages workflow 39476840082](https://github.com/ashelizasmith-create/co-constructing-multispecies-futures/actions/runs/39476840082). The homepage, 25-entry Examples page, eight-image instruction guide, and correct 0.1.2 citation and forthcoming Routledge chapter text were checked. The hosted 57,290-byte standalone HTML matches the current source exactly. A citation-selection/manual-copy improvement passed local verification, including exact clipboard readback, and awaits deployment; copying on the earlier public page remains unverified. Image resizing and preparation of the explicit ZIP link passed, while the actual ZIP browser download remains unverified. The saved [GitHub v0.1.2 release draft](https://github.com/ashelizasmith-create/co-constructing-multispecies-futures/releases/edit/untagged-cf112a03683f19d6fbec) remains unpublished while the formal creator roster is settled. No release tag or Zenodo DOI has been created. See the [0.1.2 release draft notes](docs/RELEASE-NOTES-v0.1.2.md).

## Paper and tools

**Performing the What-If: Embodied Worldbuilding with More-than-Human Intelligences, from Roleplay to Emerging Technologies**  
**Ash Eliza Smith and Julia McQuillan**  
**Forthcoming chapter in *Strategic Handbook of Worldbuilding* (Routledge); not yet public.**

The chapter presents an artist-led account of embodied worldbuilding: people develop worlds by entering them through performance and play, alongside more-than-human others. Imagining, rehearsing, reflecting, and writing inform one another. Its overlapping modes—encountering, moving with, and becoming-with—describe different relations through which a scene can take shape.

The chapter identifies this Card Deck and Interactive Tool as shared tools for building and telling speculative scenes. The repository provides the tools and practical instructions; [the paper page](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/paper.html) provides a short conceptual overview and publication status. Use [the current Interactive Tool](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/interactive.html), [the guide](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/guide.html), or [version history](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/versions.html) from this entry point.

**Provisional chapter reference:**

> Smith, A. E., & McQuillan, J. (forthcoming). Performing the What-If: Embodied Worldbuilding with More-than-Human Intelligences, from Roleplay to Emerging Technologies. In *Strategic Handbook of Worldbuilding*. Routledge.

The book title and publisher were supplied by the project owner. Editors, publication year, page range, DOI, and public URL remain unspecified. The full unpublished manuscript is not included in this repository. Three owner-authorized figures appear separately in the Examples collection with their source context and credits.

**Deck and framework lineage:**

- Candy, S., & Watson, J. (2014). *The thing from the future* [Card game]. Situation Lab.
- Smith, A. E., Leadabrand, M., Lichtman, D., Bendix, S., PytlikZillig, L. M., & McQuillan, J. (in press). Rehearsing realities: A dramaturgy for co-creating preferable futures. *TDR/The Drama Review*.

These are the two foundations explicitly named for the deck and interactive site in the chapter. The wider performance and design lineages described above form the surrounding practice. Chapter authors, cited framework authors, and toolkit creators are distinct attribution questions.

### Citing the toolkit

Use this interim title-first reference for the current development edition:

> *Co-Constructing Multispecies Futures: Card Deck and Interactive Tool.* (2026). Version 0.1.2 (development edition). https://github.com/ashelizasmith-create/co-constructing-multispecies-futures

The [About & cite page](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/paper.html#cite) provides a copyable reference and the separate chapter citation. The formal toolkit creator list is being confirmed. Narrative project credits are preserved below; framework and chapter authorship remain separate.

Record the exact Interactive Tool version or Card Deck PDF edition used, along with the date of use. A numbered HTML download preserves the tool version; a session export preserves the prompts and notes made with it. GitHub–Zenodo integration is enabled for selected published releases. No toolkit DOI has been issued yet. Once an archival release exists, use its specific version DOI when citing that release. See the [Zenodo draft](docs/ZENODO-DRAFT.md) for the prepared archival metadata.

## Credits

Created by **Ash Eliza Smith**, developed in the **Speculative Devices Lab** with **Julia McQuillan** and **Sam Bendix**, following the supplied interactive source's attribution. The source materials also document a Speculative Devices Lab × Edgeworks development context.

The two primary deck/framework references are credited above. Workshop activity credits and formal release creator order are recorded separately in [provenance](docs/PROVENANCE.md) and the [Zenodo draft](docs/ZENODO-DRAFT.md); a workshop or chapter author list does not automatically become the toolkit's creator list.

## License

The repository retains its existing [CC0 1.0 Universal dedication](LICENSE) unchanged. Credit and provenance remain documented with the materials. Licensing scope for added release components is included in the [release checklist](docs/RELEASE-CHECKLIST.md). Gallery images retain their individual source and reuse information; permission to display them does not establish a new blanket image license. The full unpublished chapter is not part of the toolkit's distributed files.

## Contributing and support

Use the [project repository](https://github.com/ashelizasmith-create/co-constructing-multispecies-futures) to share issues, propose changes, or contribute a pull request. Include the tool version or PDF filename, what happened, and what you expected. For card-text corrections, include the source card/page; for printing problems, include the paper size and print settings.

Explain what a change makes possible and how it was checked. Preserve original source files and attribution, keep previous numbered snapshots, and update the changelog for user-visible changes. Keep unpublished manuscripts and participant records out of public contributions. See [publishing guidance](docs/PUBLISHING.md) and the [release checklist](docs/RELEASE-CHECKLIST.md) before preparing a release.

Planned editorial work is recorded in [development notes](docs/DEVELOPMENT-NOTES.md), including a review of anthropomorphism, partial perspectives, and the distinction between participants' feelings and claims about another being's experience.
