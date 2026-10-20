# Release checklist

This checklist covers current development version **0.1.1**, with **0.1.0** preserved. It separates completed preparation from publication steps that still require verification. An unchecked item is not a claim that it has failed.

## Source preparation

- [x] Inventory the original repository files and retain their filenames.
- [x] Record original and supplied PDF page counts, sizes, and SHA-256 checksums.
- [x] Distinguish the general multispecies deck from the PLF workshop variant.
- [x] Identify different export geometry in similarly named PDFs.
- [x] Map the multispecies deck to 94 general activity cards, 10 contextual speculation cards, and 18 facilitator cards.
- [x] Create the 94-card general selection from the original print master and retain a page mapping.
- [x] Retain the existing CC0 1.0 `LICENSE` unchanged.
- [x] Identify source-supported team credit candidates without inventing final citation metadata.
- [x] Keep working notes, personal contact information, and meeting transcripts out of public copy.
- [x] Read the complete supplied *Performing the What-If* manuscript and use it to guide the public method description.
- [x] Include both *The Thing From The Future* and *Rehearsing Realities* in the deck's methodological lineage.
- [x] Preserve encountering, moving with, and becoming-with, with embodied rehearsal and reflection feeding the next iteration.
- [x] Keep the manuscript outside the public repository and separate chapter/framework authorship from deck credits.
- [x] Describe the related paper as a forthcoming, not-yet-public book chapter with its exact supplied title and authors.
- [x] Add a paper overview and publication metadata with unknown book, publisher, year, URL, and DOI fields left empty.
- [x] Give the README a durable `paper-and-tools` heading linking the chapter context to the current tool, guide, and version history.
- [ ] Complete a final card-text review against the selected PDF sources, including instructions and page references.
- [ ] Review the browser adaptation's spatial/temporal split and optional layers against the intended play method.
- [x] Receive and inspect the original standalone interactive HTML; record its checksum and source credits.
- [x] Choose the supplied app as the primary interactive experience, alongside the original-card browser.
- [x] Verify that the preserved original HTML exactly matches the supplied file; record its historical identity in provenance.
- [x] Use Co-Constructing Multispecies Futures as the active project name, with Card Deck and Interactive Tool format labels.
- [x] Give the Interactive Tool the stable `site/interactive.html` path, beginning at 0.1.0 and advancing to current version 0.1.1.
- [x] Integrate `site/interactive.html` under the requested project title, preserving source-supported credit names; complete the browser checks listed below.
- [ ] Confirm exact creator names, author order, roles, and any designer/illustrator credit.
- [ ] Resolve the differing Lisa PytlikZilig credit drafts and confirm Sam/Samantha Bendix's preferred release name.
- [ ] Review exercise and theoretical lineage acknowledgements separately from the creator roster.
- [ ] Confirm which historical workshop acknowledgements belong to this release.
- [ ] Confirm licensing scope for newly added material while preserving the existing dedication.

## Print and download checks

- [x] Select and label the original print masters and the general selection; retain source checksums and page mappings.
- [x] Complete the requested Letter and A4 editions in single-sided fold and duplex formats; label them with actual print settings.
- [x] Verify every general card's front/back coverage and layout geometry; confirm long-edge duplex column mirroring.
- [x] Inspect representative first and last sheets and both separate instruction/calibration PDFs.
- [x] Verify all 188 Letter fold artwork placements against the original source by independent raster comparison.
- [x] Document paper size, actual-size / 100% printing, cutting and folding, long-edge duplex, and the separate 1-inch calibration square.
- [ ] Make a physical proof with the intended printer and check front/back registration before a full print run.
- [x] Clearly distinguish a live-text PDF from editable design source; do not describe a PDF as an Illustrator source file.
- [ ] Check every download name, file size, and link in the final site.
- [ ] Check that accessible card text and use instructions accompany outlined-only artwork.

## Interactive checks

- [x] Verify draw/hold behavior and optional layers.
- [x] Verify custom duplicate prompts, literal treatment of entered text, and unlocking after prompt removal.
- [x] Verify modal keyboard behavior.
- [x] Decode all 244 WebP card images successfully.
- [x] Verify the 0.1.1 homepage → About & cite → Copy citation path and the exact title-first clipboard text.
- [x] Verify the app's five-item navigation, current-page label, and new-tab links that preserve the app session.
- [ ] Verify that prompts have the intended deck provenance and that no workshop-specific prompt is silently relabeled as universal.
- [x] Document that the app's 84 default options are an adapted bank, separate from the physical-card corpus.
- [ ] Complete remaining narrow-screen, general keyboard/focus, readable-text, and reduced-motion checks beyond the verified modal behavior.
- [ ] Verify any advertised copying, downloading, printing, local saving, and reset behavior.
- [ ] Test real microphone recording, permission denial, stop, playback, and audio export on supported browsers.
- [ ] Check whether the delivered HTML really works offline before calling it self-contained.
- [ ] Inspect final credit and citation wording on the site and in downloads.

## Publish GitHub Pages

- [x] Confirm connected GitHub account access with repository administration and push permissions.
- [ ] Push the reviewed `site/` files and Pages workflow to the intended branch.
- [x] Select **GitHub Actions** in repository **Settings → Pages**.
- [x] Deploy and verify private preview v3 at 16:41 UTC on October 20, 2026; keep it distinct from public Pages publication.
- [ ] Complete remaining binary asset uploads for public Pages publication.
- [ ] Confirm a successful workflow/deployment result.
- [ ] Open and verify the actual published URL and all downloads.
- [ ] Add the verified URL to the README and repository description.
- [ ] Link from the project owner's website, or verify a separately hosted/embedded copy.

## Preserve tracked versions

- [x] Record the first tracked development version, 0.1.0, and its changes in the changelog.
- [x] Document patch, minor, and stable-release conventions in `VERSIONING.md`.
- [x] Create the reviewed standalone `Co-Constructing_Multispecies_Futures_Interactive_v0.1.0.html` download.
- [x] Retain the 0.1.0 baseline unchanged at SHA-256 `5efdce2494d75c5f0c7e29a29ac6bd263d600a8a7a5378f28a8d5a8b40651254`.
- [x] Create the 57,084-byte `Co-Constructing_Multispecies_Futures_Interactive_v0.1.1.html` snapshot and confirm it matches the current tool; SHA-256 `fbc104a5a43dcebbd5c4d014f1aec251b1c8bfc7eabe551fc3bced0797c72ef2`.
- [x] Preserve the earlier numbered snapshot when advancing to 0.1.1.
- [ ] Create a corresponding Git tag/release when the reviewed package is deliberately released.

## Publish an archival release

- [x] Prepare a concrete [0.1.1 release draft](RELEASE-NOTES-v0.1.1.md), including contents, checks, known limits, and the interim title-first citation.
- [ ] Confirm final title, description, keywords, creators/order, licensing, and relevant funding acknowledgements.
- [ ] Choose the reviewed project version to archive and make its metadata, changelog, and deposited files agree.
- [ ] Prepare the reviewed files and source archive without private working documents.
- [x] Choose GitHub–Zenodo integration as the archival route; avoid a duplicate unrelated manual deposit.
- [x] Enable the repository in Zenodo and verify its “Repository synced successfully” confirmation.
- [ ] Finalize reviewed citation/Zenodo metadata and include all essential files in the selected tagged commit.
- [ ] Publish the selected GitHub release to trigger archiving.
- [ ] Verify the resulting Zenodo record, citation, license, archive files, and DOI.
- [ ] Add the actual version DOI and concept DOI in their appropriate places.
- [ ] Add validated `CITATION.cff` before the archival release; if `.zenodo.json` is used, keep its higher-priority metadata aligned.
- [ ] Record the final Git commit/tag and Zenodo record together.

See [PUBLISHING.md](PUBLISHING.md) for the deployment and archival steps. A private preview is verified; public Pages deployment and DOI publication remain unverified.
