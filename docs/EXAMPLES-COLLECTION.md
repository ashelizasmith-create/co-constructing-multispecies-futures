# Examples collection

`site/data/examples.json` is the source of the public image collection. Run
`python scripts/export_examples.py` after editing it; `--check` verifies that the
page and data agree. Both commands also reject empty image files, compare their
checksums and dimensions with the record, and fully decode every image using
Pillow. The public page is `site/examples.html`.

## Initial collection

The first 25 images include all three embedded images in the supplied
*Performing the What-If* manuscript, selected MuMu playtest and Alliance workshop
documentation, Speculative Robotics Lab and LARRP images, Radio Play, The Middle,
and six examples from the Edgeland Futurism teaching portfolio. The full
unpublished manuscript and private slide decks are not included.

The collection shows the wider embodied, performance, and collaborative practice
that informs the toolkit. A related project is not automatically evidence that
the later Card Deck was used. Captions preserve that distinction. Unknown
photographers and capture dates remain unstated. Teaching images credit student
work and identify the instructors separately.

Seabreeze Bop City is a separate example of students working in the field with
community, as clarified by Ash Eliza Smith on 20 October 2026 and described on
the [project page](https://asheveryday.com/index.php/seabreeze-bop-city/seabreeze-bop-city/).
It belongs in the workshop and practice history. The reviewed project page is
text-only; no photographs have been assigned to it by inference. Add its actual
images with their context and credits when the source files are available.

## Image handling and credits

The project owner authorized these images for the toolkit on 20 October 2026.
Each public record retains its caption, alt text, source label, known image and
project credits, original dimensions, and source checksum. Public source links
are included where available. Private working-document links and local file
paths are excluded from the public data.

Web copies in `site/assets/examples/` preserve the complete frame and aspect
ratio. Photographs are at most 1,600 pixels on their longest side and are never
enlarged. The text-heavy manuscript table retains its native dimensions and has
a readable HTML equivalent on the page. No original source image is overwritten.

Permission to display an image and a license for others to reuse it are recorded
separately. An unspecified photograph license is not replaced with a new CC0
assertion. Keep source credits attached when adding or moving images.

## Future community contributions

The reviewed starter collection is public. The local image-preparation prototype
and proposed form copy are in `integrations/community/`; a live submission form
is not connected yet. Keep raw submissions, private contact information, and
review notes out of this repository. Add only approved public fields and prepared
images to the gallery, with the contributor's agreed credit and display permission.

The preparation draft also accepts workshop plans and facilitation questions.
These do not require an image. Approximate location and an exploratory timetable
are enough for a plan; a help request can start with a question alone. Keep reply
details private and request a separate opt-in before listing a proposed workshop
in the public history. A plan is not evidence that a workshop has taken place.

Useful public fields are a title, context/reflection, image or media URL, alt
text, credit, workshop/year when known, and prompts/tool version when supplied.
Do not infer a participant's identity, health status, in-game role, or image date
from appearance or filenames.
