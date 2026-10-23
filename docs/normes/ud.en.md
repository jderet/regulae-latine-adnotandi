# Universal Dependencies for Latin

[Universal Dependencies](https://universaldependencies.org) (UD) is an annotation framework shared by more than 150 languages. It defines 17 part-of-speech categories (UPOS), an inventory of morphological features and 37 universal dependency relations, which each language may refine with subtypes (`advcl:abs`, `obl:arg`…). Content words are heads and function words depend on them: a preposition depends on its noun (`case`), a subordinating conjunction on the verb of its clause (`mark`), the copula on its predicate (`cop`).

Latin has six UD treebanks. Three were converted from other formats: [Perseus](perseus.md) from the [LDT](ldt.md), [PROIEL](proiel-ud.md) from [PROIEL](proiel.md), and [ITTB](ittb.md) from the [Index Thomisticus Treebank](it-tb.md). [LLCT](llct.md) was converted from an LDT-style format, while [CIRCSE](circse.md) and [UDante](udante.md) were annotated directly in UD.

## The 2023 harmonisation

Until 2023, each treebank used its own subtypes and features. F. Gamba and D. Zeman then carried out a harmonisation (UD 2.13), described in [*Universalising Latin Universal Dependencies*](https://aclanthology.org/2023.udw-1.2/) and *Latin Morphology through the Centuries* (2023). It brought ITTB, LLCT, UDante and Perseus close to a common set of subtypes. PROIEL, automatically converted from its original format, remains the furthest from it.

## Relation subtypes

Presence of each subtype in the UD 2.18 data. ✓ means the subtype is used; — means it is not (the base relation is used instead).

| Subtype | Use | CIRCSE | Perseus | PROIEL | ITTB | LLCT | UDante |
|---|---|:-:|:-:|:-:|:-:|:-:|:-:|
| `advcl:abs` | ablative absolute | ✓ | ✓ | — | ✓ | ✓ | ✓ |
| `advcl:pred` | predicative (*laetus uenit*) | ✓ | ✓ | — | ✓ | ✓ | ✓ |
| `advcl:cmp`, `obl:cmp` | comparison | ✓ | ✓ (`advcl:cmp`, `obl:cmp`) | `advcl:cmp` | ✓ | `advcl:cmp` | ✓ |
| `obl:arg` | oblique governed by the verb | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `obl:agent` | agent | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| `obl:lmod`, `obl:tmod` | place, time | ✓ | — | — | ✓ | ✓ | ✓ |
| `advmod:neg`, `:tmod`, `:lmod`, `:emph` | negation, time, place, emphasis adverbs | ✓ | ✓ | — | ✓ | ✓ | ✓ |
| `acl:relcl` | relative clause | ✓ | ✓ | — (`acl`) | ✓ | ✓ | ✓ |
| `csubj:relcl`, `ccomp:relcl`, `advcl:relcl` | free relative | ✓ | — | — | ✓ | ✓ | ✓ |
| `ccomp:reported` | reported speech | ✓ | ✓ | — | ✓ | — | ✓ |
| `conj:expl` | explicative *et* | ✓ | ✓ | — | ✓ | ✓ | ✓ |

## Lemmas and features

| | CIRCSE | Perseus | PROIEL | ITTB | LLCT | UDante |
|---|---|---|---|---|---|---|
| Lemma spelling | u, i | v | v (and some j) | u, i | u, i | u, i |
| Proper nouns | lowercase (*cocytus*) | capitalised | capitalised | lowercase | capitalised | lowercase |
| Gerund, gerundive | `VerbForm=Ger`, `Gdv` (mostly) | `VerbForm=Part`, `Aspect=Prosp` | `VerbForm=Ger`, `Gdv` | `VerbForm=Part`, `Aspect=Prosp` | `VerbForm=Part`, `Aspect=Prosp` | `VerbForm=Part`, `Aspect=Prosp` |
| Inflectional class (`InflClass`) | yes | no | no | yes | rare | yes |
| Punctuation | absent (unpunctuated texts) | `punct` | `punct` | `punct` | `punct` | `punct` |
| Enclitics (*-que*, *-ne*, *-ue*) | multiword token | multiword token | separate token, no range line | multiword token | varies (in the charters *que* is often written apart) | multiword token |
| XPOS | LASLA codes | 9-position LDT tag | 2-letter PROIEL category | Index Thomisticus codes | 10-position LDT tag | DanteSearch codes |

Every cell was measured on the 2.18 files ([method](../methode.md)).

## References

- UD documentation for Latin: <https://universaldependencies.org/la/>
- Gamba, F. and Zeman, D. (2023). *Universalising Latin Universal Dependencies: a harmonisation of Latin treebanks in UD*. UDW 2023. <https://aclanthology.org/2023.udw-1.2/>
- Gamba, F. and Zeman, D. (2023). *Latin Morphology through the Centuries: Ensuring Consistency for Better Language Processing*. ALP 2023.
