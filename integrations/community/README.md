# Community preparation preview · v0.2.0

Open `Co-Constructing_Multispecies_Futures_Community_Prototype.html` in a browser. It is a self-contained preparation prototype, with no external dependencies, fonts, requests, accounts, upload endpoint, or persistent storage. It prepares local downloads only; it is not connected to an intake service. The matching website download is `site/downloads/Co-Constructing_Multispecies_Futures_Community_Preparation_v0.2.0.html`. The earlier v0.1.0 download is preserved unchanged. The Interactive Tool has its own version number.

Version 0.2.0 adds workshop planning and facilitation inquiries alongside the existing example/image route. The draft revision is `workshop-intake-2026-10-20`; exported records use schema version `1.1`.

## Working behavior

- Choose **Share an example**, **Plan a workshop**, or **Ask for facilitation help**. The page accepts only these allowlisted deep-link values: `?intent=share-example`, `?intent=plan-workshop`, and `?intent=ask-help`. An unknown value leaves the default example route selected.
- A workshop plan asks for a working name, broad location or online setting, and audience/context. Timing defaults to **Still exploring — no date yet**; a possible date, period, or year can be added. Participant estimates and tool/deck edition are optional. Planning does not book or confirm an event.
- A help-only inquiry requires a question, with workshop name, location, context, and timing optional. A workshop plan can also request help. Optional support choices cover materials, access, adaptation, facilitation, and collaboration; free text can describe another need. Workshop/help drafts require no media.
- Optional reply name, organization, and email are kept in a distinct `privateContact` object and in a clearly marked private section of the downloaded notes. They are not used as public display credit. The default is a private inquiry, with a separate, unchecked public-history permission. A chosen public workshop credit is required only if that permission is selected. The preview does not publish anything under either setting.
- Choose a JPEG, PNG, or WebP image, or record a media URL. URLs remain text; the page does not fetch or embed them. HEIC/HEIF receives a clear instruction to export a JPEG/PNG copy first.
- Prepare a still image with its aspect ratio preserved, a longest side of at most 1,600 pixels, and no crop or upscaling. Quality and, when needed, dimensions are reduced toward a 200,000-byte target. Exact output dimensions and bytes are shown; the target is not a guarantee for every image.
- Preserve actual transparency using WebP or PNG. Choosing JPEG for an image with transparent pixels uses WebP instead, with PNG fallback when WebP export is unavailable. Canvas re-encoding does not copy the original EXIF metadata.
- Add a title, description/reflection, optional workshop/year, prompts, tool version or deck edition, display credit, image alt text, an optional media URL, and a permission acknowledgement.
- See a local draft preview. No public-gallery mock or invented contribution is included; the actual examples collection is maintained separately.
- Select **Prepare package (.zip)** to build a real ZIP containing the prepared image (when included), UTF-8 notes, and structured JSON. Then select the visible **Download prepared package (.zip)** link to save it. The ZIP is not automatically downloaded when asynchronous preparation finishes. Individual image, text, and JSON downloads remain available. The ZIP uses standard uncompressed entries without a library or CDN.
- Any input change, image replacement/removal, or draft reset invalidates the prepared package. A new preparation replaces the previous link. A token also prevents an older in-progress ZIP from becoming available after the inputs change. The package's object URL remains usable for repeated clicks until invalidation or page exit; it is not revoked immediately after downloading.
- Replace or remove an image without retaining old preview object URLs. Draft data exists only in page memory; closing or reloading loses it unless downloaded.
- Changing routes preserves the local fields for convenience but exports only the active route. A previously prepared example image, media URL, and example credit are excluded from workshop/help exports. Switching routes also invalidates any prepared ZIP link. Clearing the draft restores the example route and unchecked permissions.

## Boundaries

This is a preview of the intake flow, not a submission service. It does not send, book, moderate, review, publish, or store anything on a server. Permission choices record the participant's statements in their downloaded notes; they do not create a completed publication agreement or select a content license. The notes and JSON include any optional private reply details the participant entered, so these complete exports belong with the private inquiry rather than the public history.

The intended next stage is a private intake form with an example-review queue and a workshop/support register. Selected examples can enter the public collection after review. Only workshop details with explicit listing permission can enter the history; proposed sessions must remain labeled as planned until completion is confirmed. Those components, retention settings, publishing permissions, and final contributor wording require their own implementation. Do not replace the download button with a simulated successful submission.

## Connected form plan

[FORM-COPY.txt](FORM-COPY.txt) contains ready-to-enter Tally copy and conditional field settings for all three routes. The recommended setup has no respondent login and a 10 MB maximum per uploaded file on the example branch. The owner account and form URL are not configured. Workshop planning and help inquiries are valid without uploads. The specification separates private reply details, public example credit, and optional public workshop-history credit and consent.

Permission covers displaying the contribution with credit after review and necessary technical resizing. It does not dedicate submissions to CC0, transfer ownership, or authorize relicensing. The existing toolkit license remains separate from each contribution's rights.

1. Create and test the form in the owner's account, including upload limits, conditional required fields, the private response view, and the owner's contact/retention wording. Use the “Received for review — not public yet” confirmation only after an actual successful submission.
2. Keep original submissions, optional contact, permission evidence, and review decisions outside the public repository. Review material, captions, credit, and alt text before promotion. Keep workshop/inquiry tracking private, with inquiry status separate from activity status; receiving a plan does not establish that a workshop took place.
3. When the gallery is implemented, maintain approved entries in a single proposed `site/data/community-contributions.json` source. Publish only an explicit set of public fields and approved images with accurate contribution-specific rights. Never expose raw responses, contact details, private upload links, or administrative notes in the page, JSON, Git history, or downloads.
4. For approved workshop listings, use the existing canonical `site/data/workshops.json` and its CSV exporter. Include only the agreed public fields; exclude reply details, support correspondence, tracking IDs, and private notes. Label planned activity accurately and confirm completion separately.
5. Link the configured form from the site after checking the complete receive/review flow. Keep stable public IDs and provider-independent field names so a later form or backend can feed the same reviewed records.

This preparation creates neither an account nor a form, enables no automation, and publishes no contributions. The local HTML continues to prepare downloadable files only.

## Verification

The v0.2.0 inline JavaScript was syntax-checked, and form IDs and labels were checked for uniqueness and valid targets. Focused browser checks of the new workshop/help branches belong to the parent website workflow. Image preparation and ZIP construction are unchanged: earlier QA prepared a 2,334 × 2,000 image as a 1,600 × 1,371 JPEG of 167,110 bytes and downloaded readable notes; ZIP construction passed a text-and-binary round trip through Python's standard ZIP reader. Browser monitoring of the actual ZIP download remains unverified, while package preparation exposes an explicit Blob download link. The prototype makes no network requests by design; its content-security policy also disables connections, form actions, embedded media, and external assets.
