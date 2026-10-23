# UD_Latin-UDante

| | |
|---|---|
| Producer | University of Pisa (DanteSearch corpus) and the LiLa project (Università Cattolica, Milan) |
| Texts | Dante, *De vulgari eloquentia*, *Monarchia*, *Letters*, *Questio de aqua et terra*, *Eclogues* (with the poems of Giovanni del Virgilio) |
| Size (UD 2.18) | 1,723 sentences, 55,553 words |
| Origin | DanteSearch categories and morphology, revised; syntax annotated by hand, directly in UD |
| Licence | CC BY-NC-SA 3.0 |
| Repository | <https://github.com/UniversalDependencies/UD_Latin-UDante> |

## Characteristics

- **Fourteenth-century literary Latin**, in prose (treatises, letters) and verse (eclogues). The text keeps medieval spellings (*Bononie*, *que* for *quae*), and the lemmas are normalised.
- **Lemmas are lowercase and spelled with u/i**, proper nouns included (*bononia*). XPOS is the DanteSearch morphological code (`snp2b`).
- **It was annotated in Milan, like CIRCSE**, and follows the same principles: `advcl:abs`, `advcl:pred`, `obl:arg`, `obl:lmod`, free relatives as `:relcl`, `ccomp:reported`. It adds a few subtypes of its own (`nmod:poss`, `csubj:cleft`, `cop:outer`).
- **Gerund and gerundive** are rendered as `VerbForm=Part` with `Aspect=Prosp`, as in ITTB.
- `# citation_hierarchy` gives the book and paragraph.

## References

- Cecchini, F. M., Sprugnoli, R., Moretti, G., Passarotti, M. (2020). *UDante: First Steps Towards the Universal Dependencies Treebank of Dante's Latin Works*. CLiC-it 2020.
