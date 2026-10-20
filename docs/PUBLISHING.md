# Publishing

## Where each part lives

| Destination | Purpose |
| --- | --- |
| GitHub repository | Maintained source, card data, print files, instructions, credits, and version history. |
| GitHub Pages / the owner's website | The live experience: browse, play, read, and download. |
| Zenodo | A citable archive of a deliberately selected release, linked to the current website. |

**Verified public website:** [Co-Constructing Multispecies Futures](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/) is live with **0.1.1**. [Pages workflow 39461638283](https://github.com/ashelizasmith-create/co-constructing-multispecies-futures/actions/runs/39461638283) completed successfully from commit `26e11b445e600c6a3fa5c97b3c9abf33fa86d27d`; the live homepage, routes, card browser, and print section were checked. Live citation copying returned the exact 0.1.1 text; Print cards navigation worked, and the downloaded Letter Fold PDF matched the local 173,930-byte file byte for byte. All 300 repository paths matched their expected Git blob hashes, including all 256 binary assets.

A [GitHub release draft for v0.1.1](https://github.com/ashelizasmith-create/co-constructing-multispecies-futures/releases/edit/untagged-6910634d001822073a33) is saved and awaits the formal creator roster. It has not been published, no release tag has been created, and no Zenodo DOI has been issued. GitHub–Zenodo integration is enabled and synced.

Private preview v4 also succeeded at `2026-10-20T16:56:57.105973Z`, from source `5e997d4ad09f2289cd473e551b5f0e866ff795dd`. The public website and the private preview are separate deployments.

The chosen archival route is **GitHub → Zenodo integration**. Use one release series for this toolkit; do not also create an unrelated manual record for the same first release.

## 1. Maintain the live website

The static site is in `site/`; its Actions workflow deploys that folder. The project title is **Co-Constructing Multispecies Futures**, with **Card Deck** and **Interactive Tool** as its formats. `interactive.html` is the current tool, while numbered downloads preserve reviewed versions.

For later website updates:

1. Push the reviewed files and supplied Pages workflow to the intended branch.
2. Run the Pages workflow, or let its push trigger run. The **GitHub Actions** source setting is already saved.
3. Open the URL reported by the successful deployment and verify navigation, card images, the tool, and downloads there.
4. Add that verified URL to the README, repository description, Indexhibit link fragment, and archival metadata.

The verified public address is `https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/`. Branch-based Pages can publish only from the branch root or `/docs`, so retain Actions for the `site/` folder. Use relative asset paths to support the repository subpath.

The existing Indexhibit exhibit has a prepared copy/paste package in `integrations/indexhibit/`; its preview is separate from the live exhibit. Preserve its existing gallery image and use the verified public website as the base for its toolkit links.

Keep the README's `paper-and-tools` heading stable: the forthcoming chapter points readers to this repository. The chapter itself is not public and must remain outside the site and release archive.

Official guidance: [About Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages) and [publishing sources](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

## 2. Archive the first selected release through GitHub

The integration is connected and the [v0.1.1 release draft](https://github.com/ashelizasmith-create/co-constructing-multispecies-futures/releases/edit/untagged-6910634d001822073a33) is saved. Publishing that draft remains a separate action after the formal creator roster is settled. A normal commit is not the archive trigger. While integration remains enabled, treat each published GitHub release as an archival action; use ordinary commits and tags for work that is not ready to archive.

1. Complete [RELEASE-CHECKLIST.md](RELEASE-CHECKLIST.md), especially formal creator names/order, contributor roles, and licensing scope. The existing CC0 1.0 dedication is retained; ensure added files are covered or carry their own accurate rights statements.
2. Finalize the title, description, keywords, resource type, version, and related URLs from [ZENODO-DRAFT.md](ZENODO-DRAFT.md). Describe the mixed Card Deck / Interactive Tool package accurately instead of treating every component as software.
3. Add reviewed `CITATION.cff` metadata. If `.zenodo.json` is used to control Zenodo-specific fields, keep the two consistent: Zenodo gives `.zenodo.json` precedence over `CITATION.cff`.
4. Put all essential files in the tagged repository: general and historical PDFs, Letter/A4 fold and duplex editions, separate print instructions, card data, use guide, provenance, and the numbered standalone Interactive Tool. Do not rely on GitHub Release attachments alone being archived. Exclude unpublished manuscripts, working transcripts, and participant records.
5. Verify the exact commit, tag, changelog, and release version, then publish the selected GitHub release. **0.1.1 is the current reviewed development version**; 0.1.0 remains preserved. The [0.1.1 release draft](RELEASE-NOTES-v0.1.1.md) makes the proposed contents and known limits reviewable before archival publication.
6. Check the resulting Zenodo record, creator citation, license, archive contents, links, and assigned DOI. Record the Git tag/commit with the Zenodo version DOI and concept DOI, then add the verified citation links to the site and repository.

The reviewed standalone `Co-Constructing_Multispecies_Futures_Interactive_v0.1.1.html` is **57,084 bytes** and matches the current tool. Its SHA-256 is `fbc104a5a43dcebbd5c4d014f1aec251b1c8bfc7eabe551fc3bced0797c72ef2`. The earlier 0.1.0 snapshot is unchanged; both checksums are recorded in [PROVENANCE.md](PROVENANCE.md). Preserve these snapshots and use a new version for later changes.

The package describes embodied worldbuilding, both *The Thing From The Future* and *Rehearsing Realities*, and the movement between speculative scenes, rehearsal, and reflection. Chapter/framework authorship remains separate from toolkit credits. The interactive prompt bank is an adaptation, separate from the full original-card corpus.

Home-print PDFs must retain actual-size / 100% instructions, long-edge duplex guidance, and separate calibration sheets. Digital geometry and artwork checks are complete; physical printer registration has not been tested.

Official guidance: [enable a repository](https://help.zenodo.org/docs/github/enable-repository/), [archive a release](https://help.zenodo.org/docs/github/archive-software/github-upload/), [metadata precedence](https://help.zenodo.org/docs/github/describe-software/), and the [release-asset issue](https://github.com/zenodo/zenodo/issues/1235).

## 3. Manual deposit is an alternative

Choose this route **instead of** the connected release route if individually listed Zenodo downloads or a DOI reserved before publication become a priority. Change the documented route before publishing to avoid duplicate unrelated records.

A manual upload can retain a draft, reserve a DOI, and accept separate PDF, HTML, and ZIP files. GitHub integration does not support DOI pre-reservation. A reserved DOI is not a published record.

Official guidance: [create an upload](https://help.zenodo.org/docs/deposit/create-new-upload/), [reserve a DOI](https://help.zenodo.org/docs/deposit/describe-records/reserve-doi/), and [GitHub DOI reservation FAQ](https://support.zenodo.org/help/en-gb/24-github-integration/73-can-i-pre-reserved-a-doi-before-a-github-release).

## 4. Maintain the release series

Archive chosen reviewed releases, not every development change. Keep numbered HTML downloads and Git history as the tool develops. A version DOI identifies an exact archived release; the concept DOI represents the archive's version series. Keep later archived releases in the same series and verify the relationship after archiving. Metadata corrections and new file versions are different operations.

See [VERSIONING.md](VERSIONING.md), Zenodo's [version management](https://help.zenodo.org/docs/deposit/manage-versions/), and [DOI versioning guidance](https://support.zenodo.org/help/en-gb/1-upload-deposit/97-what-is-doi-versioning). Zenodo remains the archival destination; the verified website remains the current browser experience.
