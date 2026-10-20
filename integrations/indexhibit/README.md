# Indexhibit exhibit integration

This is a prepared text update for the existing exhibit:

https://asheveryday.com/index.php/worldbuilding-community/co-constructing-multispecies-futures/

The live exhibit has not been modified. The files are ready to copy into its existing text field when the website owner is ready to apply the update.

## Files

- `Co-Constructing_Multispecies_Futures_Indexhibit.html`: HTML fragment with styles scoped to `#ccmf-exhibit`.
- `Co-Constructing_Multispecies_Futures_Indexhibit.txt`: the identical fragment in a plain-text file for copying.
- [Preview page](../../site/indexhibit-preview.html): a separate, clearly labeled visual preview with local toolkit links. It is not the live Indexhibit page or a replacement for its template.

## Apply to the existing exhibit

1. Open the existing **Co-Constructing Multispecies Futures** exhibit in Indexhibit. Keep a copy of the current exhibit text so it can be restored.
2. Open the fragment as source text. Copy the complete fragment, including its scoped `<style>` block. Do not copy the preview page's sidebar, document shell, or image.
3. In the exhibit text/source editor, replace the existing “Interactive link coming soon” text with the fragment. This is an HTML fragment, so it belongs in the exhibit text rather than the site's global template.
4. Preserve the exhibit's existing image, image order, width, and gallery settings. Do not import or upload the image again.
5. Save when ready and use Indexhibit's preview to check the exhibit. Confirm there is one existing image, the text is readable, and the project links lead to their intended destinations. Check a narrow screen as well.

The existing image address is retained exactly:

`https://asheveryday.com/files/gimgs/397_SDL_WB_Engagement.png`

The current image width is 480 pixels. The fragment leaves image rendering to the existing Indexhibit gallery, so it does not duplicate the image or gallery controls. The standalone preview shows that image once using the same address.

## Link destinations

Until the hosted toolkit address is verified, the paste fragment's public action links point to the existing repository quickstart:

https://github.com/ashelizasmith-create/co-constructing-multispecies-futures#quickstart

Each link carries a `data-ccmf-path` value so the verified hosted destinations can be substituted consistently:

| Action | Path beneath the verified toolkit URL |
| --- | --- |
| Play with the Interactive Tool | `interactive.html` |
| Print the Card Deck | `index.html#print` |
| Workshops and development | `workshops.html` |
| Paper and tools | `paper.html` |
| Versions | `versions.html` |

Once the public base URL is verified, replace each action's `href` with that base URL plus the corresponding path, in **both** the HTML and TXT fragments. Keep the two fragments identical. The preview already uses these local paths so the sample can be explored now.

## Content and status

The fragment uses **Co-Constructing Multispecies Futures** as the project name, with **Card Deck** and **Interactive Tool** as the formats. It follows the supplied chapter's embodied-worldbuilding framing and credits both *The Thing From The Future* and *Rehearsing Realities* as the deck's foundations.

The chapter is described as forthcoming and not yet public. No manuscript, book title, publisher, publication year, or DOI has been invented or included. The current Interactive Tool label is **v0.1.1 · Development edition**.

This integration requires no JavaScript, new image imports, or changes to Indexhibit's automatic gallery controls. Its styles apply only within the fragment's own wrapper.
