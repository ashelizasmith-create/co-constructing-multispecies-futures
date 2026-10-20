# Community submission-flow preview

Open `Co-Constructing_Multispecies_Futures_Community_Prototype.html` in a browser. It is a self-contained, local preparation prototype, with no external dependencies, fonts, requests, accounts, upload endpoint, or persistent storage. It has not been published or connected to a public gallery.

## Working behavior

- Choose a JPEG, PNG, or WebP image, or record a media URL. URLs remain text; the page does not fetch or embed them. HEIC/HEIF receives a clear instruction to export a JPEG/PNG copy first.
- Prepare a still image with its aspect ratio preserved, a longest side of at most 1,600 pixels, and no crop or upscaling. Quality and, when needed, dimensions are reduced toward a 200,000-byte target. Exact output dimensions and bytes are shown; the target is not a guarantee for every image.
- Preserve actual transparency using WebP or PNG. Choosing JPEG for an image with transparent pixels uses WebP instead, with PNG fallback when WebP export is unavailable. Canvas re-encoding does not copy the original EXIF metadata.
- Add a title, description/reflection, optional workshop/year, prompts, tool version or deck edition, display credit, image alt text, an optional media URL, and a permission acknowledgement.
- See a local draft preview. No public-gallery mock or invented contribution is included; the actual examples collection is maintained separately.
- Select **Prepare package (.zip)** to build a real ZIP containing the prepared image (when included), UTF-8 notes, and structured JSON. Then select the visible **Download prepared package (.zip)** link to save it. The ZIP is not automatically downloaded when asynchronous preparation finishes. Individual image, text, and JSON downloads remain available. The ZIP uses standard uncompressed entries without a library or CDN.
- Any input change, image replacement/removal, or draft reset invalidates the prepared package. A new preparation replaces the previous link. A token also prevents an older in-progress ZIP from becoming available after the inputs change. The package's object URL remains usable for repeated clicks until invalidation or page exit; it is not revoked immediately after downloading.
- Replace or remove an image without retaining old preview object URLs. Draft data exists only in page memory; closing or reloading loses it unless downloaded.

## Boundaries

This is a preview of the submission flow, not a submission service. It does not send, moderate, review, publish, or store contributions on a server. The permission checkbox records the participant's statement in their downloaded notes; it does not create a completed publication agreement or select a content license.

The intended next stage is a private upload form, project-team review of the example and its credit, and an approved public gallery. Those components, retention settings, publishing permissions, and the final contributor wording require their own implementation. Do not replace the download button with a simulated successful submission.

## Connected form plan

[FORM-COPY.txt](FORM-COPY.txt) contains ready-to-enter Tally copy and field settings. The recommended setup has no respondent login and a 10 MB maximum per uploaded file. The owner account and form URL are not configured. The copy includes images or a media link, experience/reflection, workshop or independent context, optional year/prompts/version, public creator/photographer/collaborator credit, image descriptions, and an optional **private** contact email.

Permission covers displaying the contribution with credit after review and necessary technical resizing. It does not dedicate submissions to CC0, transfer ownership, or authorize relicensing. The existing toolkit license remains separate from each contribution's rights.

1. Create and test the form in the owner's account, including upload limits, conditional required fields, the private response view, and the owner's contact/retention wording. Use the “Received for review — not public yet” confirmation only after an actual successful submission.
2. Keep original submissions, optional contact, permission evidence, and review decisions outside the public repository. Review material, captions, credit, and alt text before promotion.
3. When the gallery is implemented, maintain approved entries in a single proposed `site/data/community-contributions.json` source. Publish only an explicit set of public fields and approved images with accurate contribution-specific rights. Never expose raw responses, contact details, private upload links, or administrative notes in the page, JSON, Git history, or downloads.
4. Link the configured form from the site after checking the complete receive/review flow. Keep stable public IDs and provider-independent field names so a later form or backend can feed the same reviewed gallery model.

This preparation creates neither an account nor a form, enables no automation, and publishes no contributions. The local HTML continues to prepare downloadable files only.

## Verification

The inline JavaScript was syntax-checked. ZIP construction was checked with a text-and-binary round trip through Python's standard ZIP reader and is unchanged by the explicit download-link fix. Browser QA prepared a 2,334 × 2,000 image as a 1,600 × 1,371 JPEG of 167,110 bytes and successfully downloaded readable notes. Asynchronous automatic ZIP downloading did not produce the expected browser download event, so package preparation now exposes a separate, user-clicked Blob download link. Its invalidation, in-flight token, and object-URL lifetime were reviewed; the parent website workflow will check that revised interaction in the browser. The prototype makes no network requests by design; its content-security policy also disables connections, form actions, embedded media, and external assets.
