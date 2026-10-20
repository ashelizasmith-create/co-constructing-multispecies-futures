# Indexhibit exhibit integration

Prepared exhibit text and an additive image insert for the existing exhibit:

https://asheveryday.com/index.php/worldbuilding-community/co-constructing-multispecies-futures/

On **20 October 2026**, Ash reported applying the prepared text to Indexhibit. That report is retained as the current status; the latest live text has not been independently verified. The new **image insert v0.1** is ready for Ash to paste into that existing text. It has not been applied to Indexhibit. The earlier full-text files are retained for reference.

## Add the images to the text already installed

Open `Co-Constructing_Multispecies_Futures_Indexhibit_Images_v0.1.txt` and copy the complete block, including its scoped styles. Paste it just after the introductory paragraph in the existing exhibit's text/source editor, after the closing `</p>`. Keep the rest of the current text and the native card-image gallery.

The insert presents **Gestures with a robotic arm** as the lead, then **Moving with a drone** and **Making with materials**. It uses existing public toolkit image URLs, so no image upload or new Indexhibit media tags are required. Each image retains its full frame, a caption, a credit, alt text, and a link to its gallery context. On narrow screens the supporting images stack in one column.

The source images are unchanged WebPs, each below 200,000 bytes: robot (46,632 bytes), drone (170,140 bytes), and fabric (69,098 bytes). The ZIP contains those exact files as optional copies. The existing native card photo is not duplicated.

See `Co-Constructing_Multispecies_Futures_Indexhibit_Images_README.txt` for paste instructions and the complete image/source credits.

## Files

- `Co-Constructing_Multispecies_Futures_Indexhibit_Images_v0.1.html` and identical `.txt`: additive three-image insert, with CSS scoped to `#ccmf-practice-images`.
- `Co-Constructing_Multispecies_Futures_Indexhibit_Images_README.txt`: placement instructions, credits, source URLs, and image sizes.
- `Co-Constructing_Multispecies_Futures_Indexhibit_Images_v0.1.zip`: the insert, instructions, and unchanged copies of the three images in `images/`.

- `Co-Constructing_Multispecies_Futures_Indexhibit.html`: HTML fragment with styles scoped to `#ccmf-exhibit`.
- `Co-Constructing_Multispecies_Futures_Indexhibit.txt`: the identical fragment in a plain-text file for copying.
- [Preview page](https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/indexhibit-preview.html): a clearly labeled proposed image insert in the earlier prepared exhibit copy, with local image assets and toolkit links. It does not verify or reproduce Ash's latest live edits.

## Earlier full-text installation instructions (retained for reference)

Ash reports completing this text update. Use the additive image instructions above for the current task; do not replace freshly edited text with the earlier full-text fragment.

1. Open the existing **Co-Constructing Multispecies Futures** exhibit in Indexhibit. Keep a copy of the current exhibit text so it can be restored.
2. Open the fragment as source text. Copy the complete fragment, including its scoped `<style>` block. Do not copy the preview page's sidebar, document shell, or image.
3. In the exhibit text/source editor, replace the existing “Interactive link coming soon” text with the fragment. This is an HTML fragment, so it belongs in the exhibit text rather than the site's global template.
4. Preserve the exhibit's existing image, image order, width, and gallery settings. Do not import or upload the image again.
5. Save when ready and use Indexhibit's preview to check the exhibit. Confirm there is one existing image, the text is readable, and the project links lead to their intended destinations. Check a narrow screen as well.

The existing image address is retained exactly:

`https://asheveryday.com/files/gimgs/397_SDL_WB_Engagement.png`

The current image width is 480 pixels. The fragment leaves image rendering to the existing Indexhibit gallery, so it does not duplicate the image or gallery controls. The standalone preview shows that image once using the retained local `assets/examples/tabletop-card-prompts.webp` copy; it does not fetch the image from asheveryday.com.

## Link destinations

The toolkit action links use the public toolkit address:

https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/

| Action | Destination |
| --- | --- |
| Try the Interactive Tool | `https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/interactive.html` |
| Print the Card Deck | `https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/index.html#print` |
| Lead a Session | `https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/guide.html` |
| Workshops and development | `https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/workshops.html` |
| About & cite | `https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/paper.html` |
| Versions | `https://ashelizasmith-create.github.io/co-constructing-multispecies-futures/versions.html` |

The HTML and TXT fragments are identical. Their `data-ccmf-path` values preserve each destination if the toolkit is hosted elsewhere later. The preview uses local toolkit links and is a sample of the proposed image insert within the earlier exhibit copy. It is not a live-site verification.

## Content and status

The fragment uses **Co-Constructing Multispecies Futures** as the project name, with **Card Deck** and **Interactive Tool** as the formats. It follows the supplied chapter's embodied-worldbuilding framing and credits both *The Thing From The Future* and *Rehearsing Realities* as the deck's foundations.

The chapter is described as forthcoming in *Strategic Handbook of Worldbuilding* (Routledge), using the project owner's supplied publication metadata. It is not yet public. Editors, publication year, pages, DOI, and public URL remain unspecified; the manuscript is not included. The current Interactive Tool label is **v0.1.2 · Development edition**.

The text and image inserts require no JavaScript, new image imports, or changes to Indexhibit's automatic gallery controls. Each insert scopes its styles to its own wrapper.
