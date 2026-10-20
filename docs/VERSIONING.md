# Versioning

The project is **Co-Constructing Multispecies Futures**, offered as **Card Deck** and **Interactive Tool**. The current source version is **0.1.2**; **0.1.0** and **0.1.1** remain preserved. Public deployment of the current source is recorded separately in the release checklist. These numbers identify the toolkit and website; they do not assign a new creation date or historical version to the original deck exports.

## Keep a current tool and preserved versions

| Item | Purpose |
| --- | --- |
| `site/interactive.html` | Stable path for **Play online**. It serves the current deployed Interactive Tool. |
| `site/downloads/Co-Constructing_Multispecies_Futures_Interactive_v0.1.0.html` | Preserved, reviewed first standalone snapshot. Keep its bytes unchanged as later versions become current. |
| `site/downloads/Co-Constructing_Multispecies_Futures_Interactive_v0.1.1.html` | Preserved navigation and citation edition. |
| `site/downloads/Co-Constructing_Multispecies_Futures_Interactive_v0.1.2.html` | Snapshot matching the current 0.1.2 source, with book metadata and an Examples link. |
| `VERSION` and `site/version.json` | Current version information used by the project and website. Keep it consistent with the tool's visible version and export filenames. |
| [CHANGELOG.md](../CHANGELOG.md) | Human-readable account of changes and publication status for each tracked version. |
| Git history and reviewed release tags | Source history connecting each release to its exact code, card data, guidance, and print files. |
| [Provenance](PROVENANCE.md) and download manifests | Original identities, selected PDF pages, derivative layouts, and file checksums. |

The supplied original HTML stays byte-preserved, with its historical filename and titles documented in provenance. Current branding is used for new files and public navigation.

A saved session and a saved tool version are different things. A session export records the prompts and notes produced during play. A numbered HTML download preserves the tool used to produce them. The Interactive Tool's current session exports include the project version in their filenames.

## Version numbers

Use a `major.minor.patch` convention. During development:

| Example | Use it for |
| --- | --- |
| **0.1.0** | The first tracked development baseline. |
| **0.1.1, 0.1.2** | Corrections within the same experience: broken links, layout or accessibility fixes, export repairs, or small wording corrections. |
| **0.2.0** | Added features, prompt layers, materially expanded content, or a substantial change in the play experience. |
| **1.0.0** | A deliberate stable release after the project owner considers the method, content, credits, formats, and supported behavior ready. |

After 1.0.0, patch versions continue to identify fixes, minor versions identify compatible additions, and a major version identifies a change that makes an established workflow or saved-data format incompatible. Record the actual change in the changelog; the number alone is not enough to understand a release.

## Prepare a version

1. Make changes in the current source and write a short changelog entry explaining their effect on use.
2. Update the current version consistently in project metadata, the visible tool, and session-export filenames.
3. Verify the changed behavior, relevant print or card data, and affected download links. Record known limits, including any physical printing checks still needed.
4. After QA, copy the reviewed standalone tool to a filename containing its version. Record the snapshot's checksum and verify that it matches the reviewed current tool.
5. Keep earlier published numbered downloads. If a published snapshot needs a correction, prepare a new version instead of replacing the bytes behind its old name.
6. When deliberately releasing, create the corresponding Git tag/release, record its commit, and update the site's version history and download links.
7. Deploy the reviewed current files to the stable online address. Verify the deployed tool before describing that version as live.

The 0.1.0, 0.1.1, and 0.1.2 snapshots have been preserved, with checksums in [PROVENANCE.md](PROVENANCE.md). Further changes to the Interactive Tool belong to a later version. Before creating its snapshot, complete the relevant checks; once preserved, do not replace its bytes. A version assignment or snapshot alone does not mean the website or an archival record has been published.

The saved GitHub release draft identifies **v0.1.2** and remains unpublished; its intended tag name does not establish a created Git tag. The public website is verified live at **0.1.2**, and its hosted standalone download matches the current 57,290-byte source and recorded SHA-256. The citation-selection improvement is deployed and verified: all 189 reference characters are selected and the live page reports “Citation copied.” Website image, history, and intake-draft corrections are tracked separately from the unchanged Interactive Tool snapshot. Community Preparation has its own version series: v0.2.0 adds workshop-plan and help routes while the original v0.1.0 download stays unchanged. Neither component version changes the Interactive Tool v0.1.2 snapshot or establishes an archival release. See [PUBLISHING.md](PUBLISHING.md) for the verified deployment and follow-up records.

### Snapshot command

Check consistency without creating a file:

```sh
python scripts/snapshot_interactive.py --check
```

After browser QA, preserve the reviewed version:

```sh
python scripts/snapshot_interactive.py
```

The standard-library script checks `VERSION`, `site/version.json`, the tool's project/version/status/date constants, its visible version label, and its session-export filename convention. It copies the source bytes into the numbered download and reports the filename, byte count, and SHA-256 checksum. Repeating the command with identical bytes is a no-op. Different content under an existing version is refused; assign a new version consistently before creating another snapshot.

## Choose what to archive in Zenodo

Archive selected reviewed releases. A small code commit does not require a new DOI, and every development version need not become a Zenodo deposit.

GitHub–Zenodo integration is the chosen route and is enabled for this repository. Publishing a GitHub release triggers archiving; use routine commits or tags for work that is not intended as a new archival release. Keep the selected numbered HTML, print files, guidance, and metadata in the tagged source rather than relying on release attachments alone.

Keep archived updates in the same release series. A version DOI identifies one archived release; the concept DOI refers to the series. A manual deposit remains an alternative if deliberately selected before publication, not a duplicate record for the same release.

See [PUBLISHING.md](PUBLISHING.md) for the official GitHub and Zenodo guidance and [RELEASE-CHECKLIST.md](RELEASE-CHECKLIST.md) for completion status.
