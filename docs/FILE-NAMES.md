# File names and retained source files

The project name is **Co-Constructing Multispecies Futures**. Use **Card Deck** and **Interactive Tool** for its formats. Workshop names identify a particular context or edition; USDA is one such workshop, not the name of the complete toolkit.

## Renamed source files

These changes organize the repository without changing the file contents. Earlier names remain in Git history and this provenance record.

| Earlier path | Current path | Bytes |
| --- | --- | ---: |
| `USDA_FullDeckwBleed_TextAsShapes_WithBleed.pdf` | `originals/Co-Constructing_Multispecies_Futures_Complete_Deck_Print.pdf` | 2,783,192 |
| `FullDeckNoBorder_WithBleed.pdf` | `originals/Co-Constructing_Multispecies_Futures_PLF_2025_Deck_Print.pdf` | 4,289,252 |
| `SDL_WB_Engagement.png` | `originals/Co-Constructing_Multispecies_Futures_Workshop_Image.png` | 177,454 |
| `originals/futures_machinenew.html` | `originals/Co-Constructing_Multispecies_Futures_Interactive_Imported.html` | 39,181 |

## Naming convention

Use `Co-Constructing_Multispecies_Futures_<Format>_<Edition>.<extension>` for newly organized source artifacts. Include a workshop name only for a workshop-specific edition, and include a version for a preserved Interactive Tool download.

Existing client-neutral public PDF download names remain stable so the links just published continue to work. For example, `Multispecies_Futures_General_Cards.pdf` is the general selection, while `PLF2025_Workshop_Deck.pdf` is explicitly a workshop edition. Future revised card contents should get an edition/version identifier; a simple source-file rename does not create new card artwork.

The card-data `source_file` field now points to the client-neutral live-text download. The historical upload filename is recorded once as `original_source_filename` and in [PROVENANCE.md](PROVENANCE.md).

## Byte preservation

| Current file | SHA-256 |
| --- | --- |
| `originals/Co-Constructing_Multispecies_Futures_Complete_Deck_Print.pdf` | `b6019dbd23e3290bd3114ec45316355e4c1ecae0934c7bc21b33a42c1693f8fa` |
| `originals/Co-Constructing_Multispecies_Futures_PLF_2025_Deck_Print.pdf` | `ab7ff4e7bd3fb64cf75c54490fe72e9fad0b7c3d2835ef1e61228c7d2afa6ad2` |
| `originals/Co-Constructing_Multispecies_Futures_Workshop_Image.png` | `186dcd603bcf514239078aa8f309225d44d33647a631cc2589850242383ba3c3` |
| `originals/Co-Constructing_Multispecies_Futures_Interactive_Imported.html` | `6dbd640be639547ff62324d8590faef132b7583b5f3d0b59735a54fdfc18c930` |
