# LiLa: Linking Latin

| | |
|---|---|
| Producer | ERC project *LiLa: Linking Latin* (no. 769994), CIRCSE, Università Cattolica del Sacro Cuore, Milan (M. Passarotti) |
| Content | a linked-data (RDF) knowledge base that connects Latin corpora, treebanks and lexicons through their lemmas |
| Core component | the *Lemma Bank*: an inventory of lemmas, each with its part of speech, inflectional class and spellings |
| Licence | Lemma Bank: CC BY-SA 4.0 |
| Website | <https://lila-erc.eu>; data: <https://github.com/CIRCSE/LiLa_Lemma-Bank> |

## Principles

- **One lemma, several spellings**: each lemma in the *Lemma Bank* has a canonical form and alternative written representations (*tempto* / *tento*). A resource links to LiLa through the lemma identifier, whatever its own spelling.
- **Part of speech and inflectional class**: the class (`n3`: third declension, `v2`: second conjugation) is the one [CIRCSE](circse.md) gives in MISC (`LiLaflcat`), and that the Milan UD treebanks express with the `InflClass` feature (`IndEurX`, `LatE`…).
- **Homonyms**: two lemmas with the same spelling but a different part of speech or inflection have two identifiers (*appello* of the first and of the third conjugation).
- The [ITTB](ittb.md), [UDante](udante.md) and [CIRCSE](circse.md) treebanks, the [LASLA](lasla.md) corpus and several dictionaries (including Lewis & Short) are linked to LiLa.
