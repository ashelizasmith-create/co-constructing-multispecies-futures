# Co-Constructing Multispecies Futures v0.1.2

**DRAFT — archival release pending remaining interaction checks, the formal creator roster, and archival metadata.** Prepared October 20, 2026. Version 0.1.2 is verified live on the [public website](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/) and preserved as a numbered standalone download. The saved [GitHub v0.1.2 release draft](https://github.com/ashelizasmith-create/co-constructing-multispecies-futures/releases/edit/untagged-cf112a03683f19d6fbec) has the 0.1.2 title, intended tag, and body. API verification identifies release `418649128` as `draft: true` with `published_at: null`. Website deployment has not published that archival release: no release tag or Zenodo DOI has been created.

## What changed and why

- **Confirmed publication context:** the chapter reference now names *Strategic Handbook of Worldbuilding* and Routledge, using the project owner's supplied metadata. This information appears in the Interactive Tool's credits as well as the paper overview and publication metadata. *Performing the What-If* remains a forthcoming, not-yet-public chapter by Ash Eliza Smith and Julia McQuillan; no editors, year, pages, DOI, or public chapter URL are inferred.
- **Examples with context:** a 25-image collection shows all three owner-authorized manuscript figures, MuMu, The Middle, workshop and robotic practice, and six teaching images. Captions, credits, image descriptions, source context, and reuse information accompany the images. Related embodied practice is distinguished from evidence of a card-deck session.
- **A visually guided homepage:** collective workshop practice leads the page, alongside complete drone and robotic-arm images. Visual cues make the Interactive Tool, printing, and facilitation routes easier to recognize and link into the Examples collection.
- **Original facilitation material:** the expanded guide presents eight original instruction-card images with verbatim text and PDF references, plus an index of all 18 facilitator cards. It distinguishes the original five-deck recipe from the current modular Spatial + Temporal route.
- **Connection to examples:** the Interactive Tool adds an Examples navigation link. Like its other toolkit links, it opens in a new tab to preserve the session and uses the public site address from a downloaded standalone file.
- **Local community preparation preview:** the separately versioned 0.2.0 draft prepares images, credit, alt text, and reflection for individual or ZIP download. It preserves the original v0.1.0 download and adds planning and facilitation-help routes that work without media, allow approximate places and exploratory timing, and separate private reply details from an optional public workshop listing. No form account, upload endpoint, or public submission service is configured.
- **Clearer source organization:** retained original PDFs, the workshop image, and the imported interactive file use descriptive project filenames. Their bytes are unchanged; [FILE-NAMES.md](FILE-NAMES.md) records both names and checksums. Existing public PDF download paths remain stable.
- **A maintained workshop log:** 26 sourced entries distinguish workshops, presentations, development contexts, and related embodied practice. `site/data/workshops.json` is the editable source; `scripts/export_workshop_log.py` generates the CSV and the marked entries on the history page. [WORKSHOP-LOG.md](WORKSHOP-LOG.md) explains how to update it without treating unknown event dates as known or related practice as proof of deck use.
- **Preserved versions:** current labels, the interim title-first citation, and download links identify 0.1.2. The 0.1.0 and 0.1.1 HTML snapshots remain unchanged.

Both primary lineages, *The Thing From The Future* and *Rehearsing Realities*, remain explicit. Chapter/framework authorship remains separate from toolkit creator metadata. The future review of anthropomorphism remains planned in [DEVELOPMENT-NOTES.md](DEVELOPMENT-NOTES.md); this update does not claim a completed prompt-bank rewrite.

## Proposed contents

The package retains the 94-card general selection; professional and Letter/A4 home-print editions; separate print instructions; the complete 122-card multispecies source and 100-card PLF variant; accessible card data and original artwork; and the Interactive Tool with its adapted 84-option bank. It includes the visually guided homepage, expanded source-card facilitation guide, 25-image Examples collection, 26-entry workshop history, citation guidance, source manifests, version/release documentation, and local community preparation preview under `integrations/community/`.

The app uses the current `site/interactive.html` path, with a preserved standalone HTML file for each tracked version. Its supplied original remains separately identifiable under its descriptive filename. The current source does not change the card artwork or default prompt bank in this patch.

The existing CC0 1.0 dedication remains unchanged. Final creator names/order, contributor roles, applicable funding, and licensing scope for added materials remain archival metadata decisions. The full unpublished manuscript, participant records, full working transcripts, and private working documents are excluded; its three owner-authorized figures are presented separately with context and credits. Gallery display permission is not a new blanket reuse license. The community prototype provides local preparation only; receiving, reviewing, and publishing submissions remain outside the implemented release scope.

## Exact Interactive Tool snapshot

File: `site/downloads/Co-Constructing_Multispecies_Futures_Interactive_v0.1.2.html`  
Size: **57,290 bytes**  
SHA-256: `0601ce6479e0144607a408f3edc77169e45ab559da7b2769adc4817b98d8c4bb`

This snapshot matches the current source byte for byte. Earlier snapshots retain their original checksums:

| Version | Bytes | SHA-256 |
| --- | ---: | --- |
| 0.1.0 | 55,421 | `5efdce2494d75c5f0c7e29a29ac6bd263d600a8a7a5378f28a8d5a8b40651254` |
| 0.1.1 | 57,084 | `fbc104a5a43dcebbd5c4d014f1aec251b1c8bfc7eabe551fc3bced0797c72ef2` |

## Verification

**0.1.2 source checks:** the snapshot script verified project/version/status/date consistency and visible version/export conventions. The current app's diff against 0.1.1 is limited to version labels, two book-credit sentences, and the Examples link; functional JavaScript is unchanged apart from `APP_VERSION`. Both older HTML hashes were rechecked. The Indexhibit HTML/TXT fragments remain identical. The workshop export check confirms 26 matching entries in JSON, CSV, and the generated history page. The 25 gallery assets now pass full decoding, dimension, and checksum checks after the two empty exports were rebuilt. The guide's eight source-body comparisons and local link/anchor checks passed; the homepage retains the card browser's IDs, scripts, and download links.

**Original preparation-preview checks:** JavaScript syntax and ZIP text/binary round-trip checks passed. Browser preparation produced a 1,600 × 1,371 JPEG of 167,110 bytes from a 2,334 × 2,000 image, and readable notes downloaded. After the asynchronous automatic ZIP download proved unreliable, the flow was changed to a separate user-clicked download link; its invalidation and object-URL lifecycle were reviewed. On the public HTTPS preview, resizing again produced the expected 167,110-byte JPEG and the explicit ZIP link became ready. The download-event monitor then timed out and reset the browser, leaving the actual ZIP download unverified; this does not establish that downloading is broken or blocked.

**Community Preparation v0.2.0 checks:** local browser checks prepared a ZIP download link for a workshop plan with title, approximate place, and context but no image, and for a help-only question with blank name, place, and context. Public-history permission is unchecked by default; timing, support, and history-credit controls reveal correctly. An export contract check confirms that help-only records omit stale image, media, alt text, credit, prompts, and year values, while keeping reply details and the support question in private fields. The question is stored only in `workshopPlan.supportDetails`, without duplication in the generic description. The current source and numbered download are **57,477 bytes**, SHA-256 `3aafa6d8b8dfcb32248189e0914ef1343350cea5cea5dd1e9c56ef215d01f9b2`. The original Community Preparation v0.1.0 download and Interactive Tool v0.1.2 snapshot are unchanged. These checks establish package preparation; the actual ZIP browser download remains unverified.

**Earlier browser and print baseline:** draw/hold, optional layers, custom duplicate prompts, literal treatment of entered text, unlocking after prompt removal, and modal keyboard behavior passed. All 244 WebP card sides decoded. Version 0.1.1 navigation and exact citation copying passed on the public site. Its live Letter Fold PDF matched the local 173,930-byte file. Home-print geometry, complete card coverage, front/back pairing, representative sheets, and all 188 Letter-fold artwork placements were checked digitally.

**Public 0.1.2 deployment:** [Pages workflow 39478715228](https://github.com/ashelizasmith-create/co-constructing-multispecies-futures/actions/runs/39478715228) succeeded from commit `332ba263dd77ea13e323a2f1d68f3700ed958f11`, tree `1f462d1d9145e743fd31d7efee8450404140c97a`. All 341 remote paths and Git blob hashes matched the reviewed source. The live homepage, 25-record Examples page, eight-card guide with its 18-card index, and forthcoming Routledge chapter reference were checked. The hosted standalone HTML matches the current source exactly: 57,290 bytes, SHA-256 `0601ce6479e0144607a408f3edc77169e45ab559da7b2769adc4817b98d8c4bb`. Hash agreement alone did not detect the two empty gallery files described below.

**Citation improvement verified live:** the reference is selected immediately, with manual-copy instructions available while clipboard copying completes. On the public page, all 189 characters were selected and the status showed “Citation copied.” The earlier local check also returned the exact 0.1.2 reference on clipboard readback. The Interactive Tool and its numbered snapshot are unchanged.

**Prepared follow-up:** two empty gallery exports, `middle-map.webp` and `teaching-fabric-prop.webp`, have been rebuilt from their original images. All 25 gallery images now decode and match their recorded dimensions and checksums; the exporter rejects empty, undecodable, mismatched, or incorrectly sized images. A regression check confirms that a zero-byte image is rejected even when its checksum matches the record. Seabreeze Bop City adds a 26th history entry, framed as student fieldwork and community futuring with dates still open. Its actual photographs have not been located in the reviewed sources. The prepared Community Preparation v0.2.0 adds share-an-example, plan-a-workshop, and ask-for-help routes, preserving the original v0.1.0 download, with no media required for plans or questions, optional private reply details, and a separate unchecked opt-in for public workshop listing. These follow-up changes require their own deployment verification; no new deployment is asserted here.

**Remaining verification:** deployment and public checks of the prepared image/history/intake corrections, plus the actual ZIP browser download. The archival release remains a draft regardless of successful website deployments.

## Known limits

The last verified private preview remains v4, which succeeded at `2026-10-20T16:56:57.105973Z`, from source `5e997d4ad09f2289cd473e551b5f0e866ff795dd`. The prepared v5 has not been published: automatic approval review rejected the publishing helper’s access to a protected tool directory, and the permitted sandboxed attempt could not reach the deployment service. The public website and the owner-private preview are separate deployments.

- Comprehensive narrow-viewport UI testing has not been performed; this is a testing limit, not a gate for the current website publication.
- Real microphone recording and physical printer registration have not been tested. Print the calibration sheet and a first sheet or duplex pair before a full run.
- The Interactive Tool's prompt bank is an adaptation, separate from the complete physical-card corpus. Notes, prompt edits, and recordings remain in the page session; save them before closing or refreshing.
- The workshop log is a sourced working record. Its qualifications distinguish event dates from document dates, planned activities from demonstrated delivery, and related projects from confirmed card use.
- The local community preview does not upload or preserve drafts on a server. Closing or reloading loses unsaved work. The curated Examples collection is separate from any future public submission flow.
- GitHub–Zenodo integration is enabled and synced. A published GitHub release will trigger archiving; no toolkit DOI exists yet. The saved draft and final metadata must agree on the selected version before publication.

## Interim development citation

> Co-Constructing Multispecies Futures: Card Deck and Interactive Tool. 2026. Version 0.1.2 (development edition). https://github.com/ashelizasmith-create/co-constructing-multispecies-futures

Identify the exact HTML version or Card Deck PDF edition used. The title-first citation avoids inventing an unresolved creator roster. Once the selected release is archived, use its version DOI for the exact archive; the forthcoming chapter has a separate reference.

See [PUBLISHING.md](PUBLISHING.md), [RELEASE-CHECKLIST.md](RELEASE-CHECKLIST.md), and [ZENODO-DRAFT.md](ZENODO-DRAFT.md) for the concrete archival preparation.
