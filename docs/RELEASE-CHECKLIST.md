# Release checklist

This checklist covers current source version **0.1.2**, with **0.1.0** and **0.1.1** preserved. Public-deployment checks below identify the exact baseline verified. It separates completed preparation from publication steps that still require verification. An unchecked item is not a claim that it has failed.

## Source preparation

- [x] Inventory the original repository files and retain their historical filenames in provenance.
- [x] Rename retained source artifacts with descriptive project names and verify unchanged bytes; record the map in `FILE-NAMES.md`.
- [x] Maintain the 26-entry sourced workshop log in JSON and verify its generated CSV/history page with `export_workshop_log.py --check`.
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
- [x] Keep the full manuscript outside the public repository and separate chapter/framework authorship from deck credits; present only the three owner-authorized figures separately with context and credits.
- [x] Describe the related paper as a forthcoming, not-yet-public chapter in *Strategic Handbook of Worldbuilding* (Routledge), with its exact supplied title and authors.
- [x] Add the owner-supplied book title and publisher to the paper overview and publication metadata; leave editors, year, pages, URL, and DOI unspecified.
- [x] Give the README a durable `paper-and-tools` heading linking the chapter context to the current tool, guide, and version history.
- [ ] Complete a final card-text review against the selected PDF sources, including instructions and page references.
- [ ] Review the browser adaptation's spatial/temporal split and optional layers against the intended play method.
- [x] Receive and inspect the original standalone interactive HTML; record its checksum and source credits.
- [x] Choose the supplied app as the primary interactive experience, alongside the original-card browser.
- [x] Verify that the preserved original HTML exactly matches the supplied file; record its historical identity in provenance.
- [x] Use Co-Constructing Multispecies Futures as the active project name, with Card Deck and Interactive Tool format labels.
- [x] Give the Interactive Tool the stable `site/interactive.html` path, beginning at 0.1.0 and advancing to current source version 0.1.2.
- [x] Integrate `site/interactive.html` under the requested project title, preserving source-supported credit names; complete the browser checks listed below.
- [ ] Confirm exact creator names, author order, roles, and any designer/illustrator credit.
- [ ] Resolve the differing Lisa PytlikZilig credit drafts and confirm Sam/Samantha Bendix's preferred release name.
- [ ] Review exercise and theoretical lineage acknowledgements separately from the creator roster.
- [ ] Confirm which historical workshop acknowledgements belong to this release.
- [ ] Confirm licensing scope for newly added material while preserving the existing dedication.

## Examples, facilitation, and local preparation

- [x] Prepare the 25-image Examples collection and its JSON inventory, including all three owner-authorized manuscript figures, MuMu, The Middle, workshop/robotic practice, and six teaching images.
- [x] Include captions, credits, image descriptions, source context, and reuse information; distinguish related practice from confirmed card-deck use.
- [x] Add a visually guided homepage with complete workshop, drone, and robotic-arm images and visual cues for its three starting routes; retain existing card-browser IDs, scripts, and download links.
- [x] Expand the guide with eight original instruction-card images, verbatim text, PDF references, and an index linking all 18 source cards; verify the eight text comparisons and local links/anchors.
- [x] Keep the original five-deck facilitation recipe distinct from the current Spatial + Temporal modular route.
- [x] Include the local-only community image-preparation preview v0.1.0 and its connected-form specification; state that no account, form URL, upload endpoint, or submission service is configured.
- [x] Verify preparation of a 2,334 × 2,000 image into a 1,600 × 1,371 JPEG of 167,110 bytes and a readable notes download; check JavaScript syntax and ZIP text/binary round trips.
- [x] Replace asynchronous automatic ZIP download with an explicit prepared-package link; review stale-input invalidation and object-URL lifetime.
- [x] Check the local Examples and guide views and the live 0.1.2 homepage, including all three hero images and layout without overflow.
- [x] Verify the public Examples route with 25 records, its featured image, and the preparation-preview link.
- [x] Verify the earlier public workshop-history baseline contains 25 entries.
- [x] Add Seabreeze Bop City as related student community fieldwork, retain unknown dates, and verify the prepared 26-entry JSON/CSV/history export.
- [x] Rebuild the empty `middle-map.webp` and `teaching-fabric-prop.webp` from originals; decode all 25 gallery assets and check dimensions and checksums.
- [x] Make the examples exporter reject empty, undecodable, mismatched, or incorrectly sized images; verify that a zero-byte file is rejected even with a matching recorded checksum.
- [x] Deploy the two-image repairs, 26-entry history, and Community Preparation v0.2.0 through successful [Pages workflow 39481709085](https://github.com/ashelizasmith-create/co-constructing-multispecies-futures/actions/runs/39481709085), commit `fa792bf5972b1b853fa1aa1a5307b7db36a58a2d`, tree `feb59296faaa02bd19871e41c82d18108f53dabd`; verify all 342 remote paths and hashes.
- [x] Verify the repaired gallery images publicly: `middle-map.webp` loads at 1600 × 1000 and `teaching-fabric-prop.webp` at 640 × 427; no failed loaded images were observed.
- [x] Check the public 26-entry history: searching for Seabreeze returns its student/community fieldwork entry, with dates explicitly open and source context retained.
- [x] Verify Community Preparation v0.2.0 locally: a plan without media and a help-only question both produce ready package-download links; optional controls reveal correctly and public-history opt-in starts unchecked.
- [x] Verify the help-only export excludes stale media/public-description fields and keeps reply details and the support question private, without duplicating the question into the generic description.
- [x] Match the v0.2.0 source and download at 57,477 bytes, SHA-256 `3aafa6d8b8dfcb32248189e0914ef1343350cea5cea5dd1e9c56ef215d01f9b2`; preserve the original community v0.1.0 download and Interactive Tool v0.1.2 snapshot unchanged.
- [x] Verify all three public Examples links target Community Preparation v0.2.0 intent routes; open the Plan link and verify Plan selection, Still exploring timing, optional private contact, unchecked public listing, the nothing-sent notice, and v0.2.0 footer. No submission endpoint is connected.
- [x] Verify image resizing on the public HTTPS preparation preview to the expected 167,110-byte JPEG and confirm the explicit ZIP link becomes ready.
- [ ] Verify the ZIP browser download; the event monitor timed out and reset the browser, so the download remains unverified rather than known broken or blocked.
- [x] Verify the live guide's eight expected source images, six session steps, and 18-card index, with no overflow.

The preparation preview is separate from the curated Examples collection. It does not receive or publish contributions. Connected submissions and review are future implementation, not enabled release features. Comprehensive narrow-viewport UI testing has not been performed; this is a recorded testing limit, not a gate for the current website publication.

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
- [x] Verify the 0.1.1 app's five-item navigation, current-page label, and new-tab links that preserve the app session.
- [ ] Verify that prompts have the intended deck provenance and that no workshop-specific prompt is silently relabeled as universal.
- [x] Document that the app's 84 default options are an adapted bank, separate from the physical-card corpus.
- [ ] Complete remaining narrow-screen, general keyboard/focus, readable-text, and reduced-motion checks beyond the verified modal behavior.
- [ ] Verify any advertised copying, downloading, printing, local saving, and reset behavior.
- [ ] Test real microphone recording, permission denial, stop, playback, and audio export on supported browsers.
- [ ] Check whether the delivered HTML really works offline before calling it self-contained.
- [ ] Inspect final credit and citation wording on the site and in downloads.

## Publish GitHub Pages

- [x] Confirm connected GitHub account access with repository administration and push permissions.
- [x] Push the reviewed 0.1.1 website files and Pages workflow; verify all 300 baseline repository paths against their exact Git blob hashes.
- [x] Select **GitHub Actions** in repository **Settings → Pages**.
- [x] Verify private preview v4 at `2026-10-20T16:56:57.105973Z`, source `5e997d4ad09f2289cd473e551b5f0e866ff795dd`; keep it distinct from public Pages publication.
- [x] Complete and hash-verify all 256 binary asset uploads.
- [x] Confirm successful [Pages workflow 39461638283](https://github.com/ashelizasmith-create/co-constructing-multispecies-futures/actions/runs/39461638283) from commit `26e11b445e600c6a3fa5c97b3c9abf33fa86d27d`.
- [x] Verify the [public website](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/), its verified 0.1.1 homepage, navigation routes, cards, and print section.
- [x] Verify live How to cite → Copy citation against the exact 0.1.1 text and use the live Print cards navigation.
- [x] Download the live Letter Fold PDF and confirm its 173,930 bytes match the local file byte for byte.
- [x] Add the verified public URL and hosted download links to the README.
- [x] Save the repository About description and website with the verified public URL.
- [x] Verify the saved About description and website link in the rendered repository page.
- [x] Deploy 0.1.2 with successful [Pages workflow 39476840082](https://github.com/ashelizasmith-create/co-constructing-multispecies-futures/actions/runs/39476840082), commit `8215b73e2f65f383e981c16a7949e1e430e99f3a`, tree `577499a3e8d4e224af410073ba3a74e6f7a183ad`.
- [x] Verify all 341 remote file paths and hashes against the reviewed 0.1.2 expected tree.
- [x] Verify the live 0.1.2 homepage version, loaded hero images, Examples navigation, and layout without overflow.
- [x] Verify the public About & cite page displays the correct 0.1.2 citation and forthcoming Routledge chapter text.
- [x] Download the hosted 0.1.2 standalone HTML over public HTTP and match its 57,290 bytes and SHA-256 `0601ce6479e0144607a408f3edc77169e45ab559da7b2769adc4817b98d8c4bb` to current source.
- [x] Prepare matching Indexhibit HTML/TXT fragments with six verified-site destinations; preserve the existing gallery image.
- [ ] Apply the prepared fragment to the existing Indexhibit exhibit; its live text has not been edited.

## Preserve tracked versions

- [x] Record the first tracked development version, 0.1.0, and its changes in the changelog.
- [x] Document patch, minor, and stable-release conventions in `VERSIONING.md`.
- [x] Create the reviewed standalone `Co-Constructing_Multispecies_Futures_Interactive_v0.1.0.html` download.
- [x] Retain the 0.1.0 baseline unchanged at SHA-256 `5efdce2494d75c5f0c7e29a29ac6bd263d600a8a7a5378f28a8d5a8b40651254`.
- [x] Create the 57,084-byte `Co-Constructing_Multispecies_Futures_Interactive_v0.1.1.html` snapshot and confirm it matched the 0.1.1 source; SHA-256 `fbc104a5a43dcebbd5c4d014f1aec251b1c8bfc7eabe551fc3bced0797c72ef2`.
- [x] Preserve the earlier numbered snapshot when advancing to 0.1.1.
- [x] Create the 57,290-byte 0.1.2 snapshot, verify that it matches current source, and recheck both earlier hashes; SHA-256 `0601ce6479e0144607a408f3edc77169e45ab559da7b2769adc4817b98d8c4bb`.
- [x] Restrict the app diff from 0.1.1 to the version, confirmed book credits, and Examples navigation; preserve functional JavaScript apart from `APP_VERSION`.
- [x] Verify the immediate citation-selection/manual-copy fallback locally: all 189 characters selected, “Citation copied.” status, and clipboard readback exactly matching the 0.1.2 reference.
- [x] Deploy the citation improvement through [Pages workflow 39478715228](https://github.com/ashelizasmith-create/co-constructing-multispecies-futures/actions/runs/39478715228), commit `332ba263dd77ea13e323a2f1d68f3700ed958f11`; verify all 189 characters selected and “Citation copied.” on the live page.
- [x] Deploy and verify the current 0.1.2 site, preserving the earlier 0.1.1 deployment checks as a historical baseline.
- [ ] Create a corresponding Git tag/release when the reviewed package is deliberately released.

## Publish an archival release

- [x] Retain the historical [0.1.1 release notes](RELEASE-NOTES-v0.1.1.md).
- [x] Prepare concrete [0.1.2 release notes](RELEASE-NOTES-v0.1.2.md), including contents, bounded checks, known limits, and the interim title-first citation.
- [x] Update the [saved v0.1.2 release draft](https://github.com/ashelizasmith-create/co-constructing-multispecies-futures/releases) to **Co-Constructing Multispecies Futures v0.1.2**, intended tag `v0.1.2`, and the body identifying 26 history entries and Community Preparation v0.2.0.
- [x] Verify release ID `418649128` through the API as `draft: true` and `published_at: null`; leave it unpublished pending the formal creator roster. No release tag has been created.
- [ ] Reconcile final reviewed contents and archival metadata with the saved v0.1.2 draft before publishing.
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

See [PUBLISHING.md](PUBLISHING.md) for the deployment and archival steps. Public GitHub Pages is verified live at 0.1.2; remaining interaction checks are listed above. The last verified private preview remains v4; v5 publishing is blocked by the automatic approval rejection and sandboxed network failure documented in `PUBLISHING.md`. The GitHub v0.1.2 release is a saved draft; no archival DOI has been issued.
