# Collatinus

| | |
|---|---|
| Authors | Yves Ouvrard and Philippe Verkerk |
| Nature | lemmatiser and morphological analyser for Latin, with scansion; free software and online service |
| Licence | GPL 3 (software) |
| Sources | <https://github.com/biblissima/collatinus>; online: <https://outils.biblissima.fr/fr/collatinus-web/> |

## Principles

- **Context-free analysis**: for a given form, Collatinus returns every possible lemma, each with all its morphological analyses. It does not choose: the user, or a downstream tool, decides in context.
- **Lexicon with quantities**: lemmas and forms carry vowel quantities, which are used for scansion.
- **Dictionary lemmas**: the lexicon is built on the major dictionaries (Gaffiot, Lewis & Short, Georges…), whose translations are displayed with the analysis.
- **No syntax**.

Collatinus is not an annotation standard in the treebank sense, but it is a widely used lemmatisation reference, especially in teaching. The [adnotationes-latinae](adnotationes.md) project uses it as an aid: the lemmas it allows for each form are offered to the model.
