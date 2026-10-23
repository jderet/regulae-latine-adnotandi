# Standards

The standards described here fall into three families. Sizes are those of UD release 2.18. A syntactic word is a word after enclitics have been split: *uirumque* counts as two.

## Universal Dependencies treebanks

All of them use the CoNLL-U format and share the UD labels. They differ in origin (native UD annotation or conversion), relation subtypes, features and lemmas. See [Universal Dependencies for Latin](ud.md).

| Treebank | Texts | Period | Sentences | Words | Origin | Licence |
|---|---|---|---:|---:|---|---|
| [CIRCSE](circse.md) | Seneca (tragedies), Tacitus (*Germania*) | 1st c. | 1,972 | 29,055 | native UD annotation, LASLA lemmas and morphology | CC BY-SA 4.0 |
| [Perseus](perseus.md) | Augustus, Cicero, Virgil, Ovid, Petronius, Sallust, Vulgate… | 1st c. BC – 5th c. | 2,273 | 29,223 | converted from LDT 2.1 | CC BY-NC-SA 2.5 |
| [PROIEL](proiel-ud.md) | Vulgate (NT), Caesar, Cicero (*Att.*, *Off.*), Palladius | 1st c. BC – 5th c. | 18,689 | 205,566 | converted from PROIEL | CC BY-NC-SA 3.0 |
| [ITTB](ittb.md) | Thomas Aquinas | 13th c. | 26,977 | 450,517 | converted from the Index Thomisticus Treebank | CC BY-NC-SA 3.0 |
| [LLCT](llct.md) | charters from Tuscany | 774–897 | 9,023 | 242,411 | converted from the LDT format | CC BY-SA 4.0 |
| [UDante](udante.md) | Dante (Latin works) | 14th c. | 1,723 | 55,553 | native UD annotation | CC BY-NC-SA 3.0 |

## Original formats

These are the standards the UD treebanks were converted from. They are still in use, and their choices explain many peculiarities of the UD versions.

- [LDT / AGDT](ldt.md): the Latin Dependency Treebank of the Perseus Project, with the 2007 *Guidelines*;
- [PROIEL](proiel.md): the University of Oslo format, with empty nodes and secondary edges;
- [Index Thomisticus Treebank](it-tb.md): the Prague style applied to Thomas Aquinas.

## Lexicon and morphology

These cover conventions for lemmas, categories and spelling: [LASLA](lasla.md), [LiLa](lila.md), [Collatinus](collatinus.md), and the [EvaLatin](evalatin.md) evaluation campaigns.

## Our standard

The standard followed by the [adnotationes-latinae](adnotationes.md) project to annotate the Perseus Latin corpus. It starts from CIRCSE and records where it departs from it.
