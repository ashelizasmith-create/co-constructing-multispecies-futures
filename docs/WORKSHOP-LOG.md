# Keeping the workshop log

Keep the running record in [`site/data/workshops.json`](../site/data/workshops.json). This is the single editable source for workshops, development contexts, presentations, and related embodied practice around **Co-Constructing Multispecies Futures**.

The [public history page](../site/workshops.html) presents that record. [`site/data/workshops.csv`](../site/data/workshops.csv) is a generated download for reading in a spreadsheet or sharing with collaborators. Edit the JSON source, then regenerate those two views. Edits made directly to the CSV or the generated entries in the HTML page will be replaced by the next export.

USDA is recorded as one specific workshop. It is not the name of the project or the general deck, and its entry is separate from NIST and PLF. The project owner confirmed the USDA workshop on 20 October 2026; that confirmation date is not the event date. Its formal title, date, location, collaborators, and recipe are still open.

## Add or update a workshop

1. Open [`site/data/workshops.json`](../site/data/workshops.json). On GitHub, use the pencil / **Edit this file** action, or edit a local checkout.
2. Find the existing entry by its stable `id`, or copy an entry and give the new one a unique lowercase ID with hyphens. Keep the ID when correcting an entry so links to it continue to work.
3. Add only the details you can support. Include a source label, the workshop's particular recipe or iteration when known, and the details that still need confirmation.
4. Update the top-level `updated` date to the day the log was revised, in `YYYY-MM-DD` form. This is the log's update date, not a replacement for an unknown event date.
5. From the repository root, run:

   ```bash
   python3 scripts/export_workshop_log.py
   python3 scripts/export_workshop_log.py --check
   ```

   The first command regenerates the CSV and the entries, count, and update date on the public history page. The second verifies they match the source without changing files. The script uses Python's standard library and can also run from another directory if you give its full path.
6. Review the entry on the page, then include the JSON, CSV, and page together in the usual repository update. This script does not commit, push, or deploy anything. If you edit through GitHub's web interface, a maintainer still needs to run the export and publish the updated site.

The order within each category follows the JSON array. Dates that remain unknown can stay after the dated entries; do not manufacture a date to make sorting easier.

## Entry fields

| Field | What to record |
| --- | --- |
| `id` | A stable identifier such as `usda-workshop`. Use lowercase letters, numbers, and hyphens. |
| `title` | The supported event or project title. A descriptive label is fine when the formal title is unknown; say so in `unknowns`. |
| `connection_kind` | One of `workshop`, `development`, `presentation`, or `related`; see the distinctions below. |
| `date_label` | The date as a visitor should read it, including qualifications such as “Date to confirm” or “2024 project reference; workshop dates not given.” |
| `event_start`, `event_end` | A supported event date in `YYYY-MM-DD`, a known month in `YYYY-MM`, a known year in `YYYY`, or `null`. Use `null` for an unknown end date; do not invent January 1 for a known year. |
| `date_basis` | Explain whether a date comes from an event schedule, retrospective account, document filename, project reference, or owner confirmation. |
| `place` | The known city, venue, institution, or online format. Keep partial information and identify the missing portion. |
| `theme` | The workshop or project's subject, when known. Otherwise use a clear “Theme to confirm” label. |
| `iteration` | A short account of the workflow, deck, tool, or practice used or described. Preserve distinctions between an activity being planned, presented, and delivered. |
| `evidence_status` | A readable description such as “Dated workshop instructions,” “Retrospective workshop account,” or “Workshop confirmed by the project owner.” |
| `confidence` | A short provenance label, such as `documented`, `retrospective`, or `user-confirmed`. This describes the basis of the entry; it is not a numerical quality score. |
| `unknowns` | The important details still to confirm and any limits on the claim. An empty string is allowed when nothing material remains open. |
| `sources` | One or more objects with a `label` and, optionally, a verified public `url`. Identify the relevant section, page, tab, or confirmation date in the label. |

Keep the top-level `project_name`, `status`, `scope`, and release metadata consistent with the repository. Adding a workshop does not by itself require changing the Interactive Tool's version.

## Distinguish the connection to the toolkit

- **`workshop`** — A workshop account, specific activity guide, or owner-confirmed use. A guide may document a planned activity; describe its evidence status clearly and avoid claiming delivery or participant outcomes from instructions alone.
- **`development`** — Prompt-bank, worksheet, or other method development where a particular delivered workshop is not established.
- **`presentation`** — A talk, slide set, or conference presentation that describes the approach. Slides showing cards do not establish that attendees used them.
- **`related`** — A project in the broader embodied worldbuilding practice. Its inclusion does not establish deck use at every rehearsal, performance, or playtest.

A workshop can be confirmed even when its exact date or place is unknown. Record that confirmation and leave the missing fields open. Keep event dates distinct from the date a document was drafted, revised, uploaded, or discussed. A fictional story horizon, such as 2046 or 2075, is not an event date.

## Repeated activity and partial dates

Use “Multiple sessions” only when a source describes repeated activity. Keep the type of activity clear: “Multiple playtests” or “Multiple community interviews” can be more accurate than “workshops.” Repeated activity does not automatically establish multiple venues or use of this particular card deck.

| What is supported | How to label it |
| --- | --- |
| A repeated series and its first year are established | `Multiple sessions · since YYYY`; record the supported year in `event_start` and explain its source in `date_basis`. |
| A dated account establishes that a repeated activity existed by a year, but its beginning is unknown | `Multiple sessions · documented by YYYY`; keep the unknown first-session date open. |
| The year comes only from workshop materials or their filename | `Multiple sessions · materials from YYYY`; identify that limited basis in `date_basis`. |
| Repeated activity is described, but the year belongs to the project reference | `Multiple playtests · YYYY project reference`, or name the appropriate activity; do not treat the reference year as the series' beginning. |
| Only one workshop is confirmed | Keep a single entry and its known date or `Date to confirm`. Do not infer recurrence from missing details. |

Preserve exact event dates already established. Where a month is known for documented activity, it can remain visible with that qualification. Explain in `unknowns` when the first or last session is still open, so the qualification appears on the public page as well as in the structured log.

For example, SciComm has repeated sessions and materials labeled 2024, while MuMu has roughly 20 playtests and a 2025 project reference. Neither source establishes the first session year. The Robotics Pop-Up has activity documented in January 2025 over a reported three-month period. Southern Devices has multiple community interviews and a 2024 project reference, with the beginning of its two-year development period still unspecified. USDA remains one confirmed workshop with its event date open.

## Sources and privacy

The JSON, CSV, and history page are public. Include event facts, concise method descriptions, public creator or facilitator credits when supported, and source references that readers can understand. The CSV keeps source labels and any public URLs together in its `sources` column.

Keep participant lists, email addresses, contact details, recordings, unapproved photographs, research consent material, private transcripts, and internal intellectual-property discussions outside the public repository. A source label can identify an internal guide without copying its contents or linking to a private document. Add a URL only when it is appropriate to publish and supports the entry.

Preserve uncertainty when sources disagree. Keep a concise public qualification in `unknowns`, and keep detailed reconciliation notes in the project's private research records. Do not infer a workshop's location, participants, or results from another event with a similar theme.

## Example: a confirmed workshop with missing details

The USDA entry demonstrates the intended pattern: `event_start` and `event_end` are `null`, `date_label` says “Date to confirm,” and the source names the project owner's confirmation on 20 October 2026. The confirmation establishes one workshop; it does not supply an event date or identify it with another event. Replace unknowns only as the project owner or another suitable source supplies the missing information.

Seabreeze Bop City is recorded separately as related student fieldwork and community futuring in Seabreeze, North Carolina. Its public project account and the owner's clarification establish that context; they do not establish a first year, session count, or card-deck use. Keep its fieldwork dates open and do not label it “Multiple” without further evidence. Seabreeze Bop City is one project title and is distinct from Edgeland Futurism.

## What the export preserves

The export checks required fields, unique stable IDs, date formats, category names, source labels, and HTTP(S) link formats. It escapes entry text before inserting it into the public page. It regenerates only the marked workshop-list block; the page's introduction, navigation, styling, and other content remain outside that block.

The export does not decide whether a source is public, whether an event happened, or whether a claim is supported. Those decisions remain part of maintaining the log. Review new entries and sources before publishing them.
