# Regulae Latine adnotandi

This site compares the **annotation standards for Latin**: lemmatisation, morphology and dependency syntax.
There are about ten of them today. Six treebanks in the Universal Dependencies (UD) format do not always agree with each other, and the formats they were converted from (LDT, PROIEL, Index Thomisticus) follow different principles. Lexical resources (LASLA, LiLa, Collatinus) also have their own lemma conventions.

The site is organised along two axes.

<div class="grid cards" markdown>

- **[Standards](normes/index.md)**: one page per standard, covering its origin, texts, format, licence and characteristic choices.
- **[Phenomena](phaenomena/index.md)**: one page per linguistic phenomenon (copula, ablative absolute, accusative and infinitive…), with a comparative table, the frequencies observed in each treebank, and one real example per standard.

</div>

## The examples

The examples are not hand-picked. A [script](methode.md) reads the treebanks at a fixed version (UD 2.18) and selects, for each one, a short sentence that follows **that treebank's most frequent analysis**. What you see is the ordinary practice of the standard, not a textbook case. Each sentence comes with its exact source (`sent_id`), its licence, a tree and the CoNLL-U lines.

For UD_Latin-Perseus and UD_Latin-PROIEL, the same sentence is also shown **in its original format** (LDT 2.1, PROIEL XML), so you can see what the conversion to UD changed.

## Status

Nine pages so far: [copula](phaenomena/copula.md), [ablative absolute](phaenomena/ablativus-absolutus.md), [accusative and infinitive](phaenomena/accusativus-cum-infinitivo.md), [gerund and gerundive](phaenomena/gerundium-gerundivum.md), [coordination with -que](phaenomena/coordinatio.md), [verbless clauses](phaenomena/sine-verbo.md), [verb ellipsis](phaenomena/ellipsis.md), [governed obliques](phaenomena/obliqui.md) and [participles](phaenomena/participium.md). The planned pages are listed under [Phenomena](phaenomena/index.md). Corrections and suggestions are welcome as issues or pull requests on [GitHub](https://github.com/jderet/regulae-latine-adnotandi).

## Licence

The texts and examples on this site are published under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). This licence is compatible with all the treebanks quoted, several of which (PROIEL, ITTB, UDante, UD Perseus) forbid commercial use. The code is under the MIT licence.
