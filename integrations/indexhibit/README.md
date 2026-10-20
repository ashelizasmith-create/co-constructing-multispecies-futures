# Indexhibit exhibit integration

Prepared exhibit text, quick links, and an additive image insert for the existing exhibit:

https://asheveryday.com/index.php/worldbuilding-community/co-constructing-multispecies-futures/

On **20 October 2026**, Ash reported applying the prepared text to Indexhibit, then approved the published image-layout preview with clear project links. **Complete v0.1** now combines that approved introduction, navigation, three credited photographs, background, and lineage into one paste-ready fragment. The live Indexhibit text has not been independently verified or modified by this work. Earlier versioned component inserts remain available.

## Install the complete approved layout

Use **`Co-Constructing_Multispecies_Futures_Indexhibit_Complete_v0.1.txt`** for the approved layout in one file. Copy the full content into the exhibit text/source editor, replacing the exhibit text after keeping a copy of any edits you wish to retain. Keep the native card-image gallery and its settings. The three practice photographs are included through hosted URLs; no uploads are required.

This complete fragment already contains the Quick Links and Images blocks. Install it once; do not also paste the older component inserts. It excludes the preview sidebar, status banner, footer, and native tabletop photograph. The canonical unversioned HTML/TXT files now match Complete v0.1.

See `Co-Constructing_Multispecies_Futures_Indexhibit_Complete_README.txt` for the full installation instructions. The following component instructions remain useful for selective additions to an existing exhibit.

## Give visitors two clear destinations

Use this order: **introduction → quick links → images → context and further links**. Both main destinations appear before the photographs.

Open `Co-Constructing_Multispecies_Futures_Indexhibit_Quick_Links_v0.1.txt` and copy the complete block, including its scoped styles. Paste it immediately after the introductory paragraph's closing `</p>`, before the image insert. It presents:

- **Open project website ↗** — Interactive Tool, printable cards and facilitation guides. This is the primary black button.
- **View GitHub repository ↗** — Source files, documentation and version history. This is the outlined button.
- A smaller row for **Try the Interactive Tool**, **Print the Card Deck**, and **How to cite**.

The two destinations stack on narrow screens. Links open in the same tab, with visible keyboard focus. The block needs no JavaScript, new assets, or global template changes.

**Use one installation method:** add the small Quick Links insert to the already-edited page, **or** use the refreshed canonical full-text HTML/TXT fragment. The full-text fragment already contains the block; installing both would duplicate it. The small insert preserves Ash's latest text edits. If using it, remove the repeated Interactive Tool, Print the Card Deck, and About & cite links from the old lower row, leaving Lead a Session, Workshops & development, Examples, and Versions as contextual links.

See `Co-Constructing_Multispecies_Futures_Indexhibit_Quick_Links_README.txt` for paste instructions and destinations.

## Add the images below the quick links

Open `Co-Constructing_Multispecies_Futures_Indexhibit_Images_v0.1.txt` and copy the complete block, including its scoped styles. Paste it after the Quick Links block and before the contextual body text. If the images are already installed, place Quick Links immediately before their `<style>` block. Keep the rest of the current text and the native card-image gallery.

The insert presents **Gestures with a robotic arm** as the lead, then **Moving with a drone** and **Making with materials**. It uses existing public toolkit image URLs, so no image upload or new Indexhibit media tags are required. Each image retains its full frame, a caption, a credit, alt text, and a link to its gallery context. On narrow screens the supporting images stack in one column.

The source images are unchanged WebPs, each below 200,000 bytes: robot (46,632 bytes), drone (170,140 bytes), and fabric (69,098 bytes). The ZIP contains those exact files as optional copies. The existing native card photo is not duplicated.

See `Co-Constructing_Multispecies_Futures_Indexhibit_Images_README.txt` for current placement instructions and the complete image/source credits. The versioned Images v0.1 HTML/TXT files and ZIP remain unchanged; their earlier placement instructions are superseded by the order above.

## Files

- `Co-Constructing_Multispecies_Futures_Indexhibit_Complete_v0.1.html` and identical `.txt`: the complete approved exhibit fragment, including all three practice photographs.
- `Co-Constructing_Multispecies_Futures_Indexhibit_Complete_README.txt`: instructions for installing the complete fragment once.

- `Co-Constructing_Multispecies_Futures_Indexhibit_Quick_Links_v0.1.html` and identical `.txt`: compact additive destination links, with CSS scoped to `#ccmf-quick-links`.
- `Co-Constructing_Multispecies_Futures_Indexhibit_Quick_Links_README.txt`: placement instructions and destination URLs.
- `Co-Constructing_Multispecies_Futures_Indexhibit_Images_v0.1.html` and identical `.txt`: additive three-image insert, with CSS scoped to `#ccmf-practice-images`.
- `Co-Constructing_Multispecies_Futures_Indexhibit_Images_README.txt`: placement instructions, credits, source URLs, and image sizes.
- `Co-Constructing_Multispecies_Futures_Indexhibit_Images_v0.1.zip`: the insert, instructions, and unchanged copies of the three images in `images/`.

- `Co-Constructing_Multispecies_Futures_Indexhibit.html`: canonical complete exhibit text, matching Complete v0.1 with introduction, quick links, photographs, context, and credits.
- `Co-Constructing_Multispecies_Futures_Indexhibit.txt`: the identical fragment in a plain-text file for copying.
- [Preview page](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/indexhibit-preview.html): a clearly labeled proposed layout with quick links before the photographs, prepared exhibit text, and local assets. It does not verify or reproduce Ash's latest live edits.

## Full-text installation option (retained for reference)

Ash reports completing the earlier text update. The additive instructions above preserve those edits. Use the refreshed full-text option only when intentionally replacing the exhibit text; do not also add the Quick Links insert.

1. Open the existing **Co-Constructing Multispecies Futures** exhibit in Indexhibit. Keep a copy of the current exhibit text so it can be restored.
2. Open the fragment as source text. Copy the complete fragment, including its scoped `<style>` block. Do not copy the preview page's sidebar, document shell, or image.
3. In the exhibit text/source editor, replace the intended exhibit text with the fragment. This is an HTML fragment, so it belongs in the exhibit text rather than the site's global template. Both the Quick Links and three-photo image blocks are already included; do not add them again.
4. Preserve the exhibit's existing image, image order, width, and gallery settings. Do not import or upload the image again.
5. Save when ready and use Indexhibit's preview to check the exhibit. Confirm there is one existing image, the text is readable, and the project links lead to their intended destinations. Check a narrow screen as well.

The existing image address is retained exactly:

`https://asheveryday.com/files/gimgs/397_SDL_WB_Engagement.png`

The current image width is 480 pixels. The fragment leaves image rendering to the existing Indexhibit gallery, so it does not duplicate the image or gallery controls. The standalone preview shows that image once using the retained local `assets/examples/tabletop-card-prompts.webp` copy; it does not fetch the image from asheveryday.com.

## Link destinations

The project website is the public toolkit. GitHub is the source repository:

https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/

| Action | Destination |
| --- | --- |
| Open project website | `https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/index.html#start` |
| View GitHub repository | `https://github.com/ashelizasmith-create/co-constructing-multispecies-futures` |
| Try the Interactive Tool | `https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/interactive.html` |
| Print the Card Deck | `https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/index.html#print` |
| How to cite | `https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/paper.html#cite` |
| Lead a Session | `https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/guide.html` |
| Workshops and development | `https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/workshops.html` |
| Examples | `https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/examples.html` |
| Versions | `https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/versions.html` |

Each HTML/TXT pair is identical. The `data-ccmf-path` values preserve toolkit destinations if the toolkit is hosted elsewhere later. The preview uses local toolkit links and image assets, with the real GitHub destination kept distinct. It is a proposed layout, not a live-site verification.

## Content and status

The fragment uses **Co-Constructing Multispecies Futures** as the project name, with **Card Deck** and **Interactive Tool** as the formats. It follows the supplied chapter's embodied-worldbuilding framing and credits both *The Thing From The Future* and *Rehearsing Realities* as the deck's foundations.

The chapter is described as forthcoming in *Strategic Handbook of Worldbuilding* (Routledge), using the project owner's supplied publication metadata. It is not yet public. Editors, publication year, pages, DOI, and public URL remain unspecified; the manuscript is not included. The current Interactive Tool label is **v0.1.2 · Development edition**.

The text, quick links, and image inserts require no JavaScript, new image imports, or changes to Indexhibit's automatic gallery controls. Each insert scopes its styles to its own wrapper.
