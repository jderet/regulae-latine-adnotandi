# UD_Latin-ITTB

| | |
|---|---|
| Producer | CIRCSE (Università Cattolica, Milan) and ÚFAL (Prague) |
| Texts | Thomas Aquinas, *Summa contra Gentiles*; concordances of the word *forma* in the *Index Thomisticus* |
| Size (UD 2.18) | 26,977 sentences, 450,517 words: the largest Latin treebank |
| Origin | automatic conversion of the [Index Thomisticus Treebank](it-tb.md), in the Prague style; first through HamleDT (UD 1.2, 2015), conversion redone in UD 2.3 (Cecchini et al. 2018), harmonised in UD 2.13 |
| Licence | CC BY-NC-SA 3.0 |
| Repository | <https://github.com/UniversalDependencies/UD_Latin-ITTB> |

## Characteristics

- **Scholastic Latin**: the most visible phenomenon is the accusative and infinitive as subject of an impersonal verb (*oportet*, *necesse est*). There the infinitive is `csubj` more often than `ccomp` (see the [page](../phaenomena/accusativus-cum-infinitivo.md)).
- **Lemmas are lowercase and spelled with u/i**. XPOS holds the morphological code of R. Busa's *Index Thomisticus* (`C1|grn1|casD|gen2`). MISC adds `TraditionalMood` and `TraditionalTense`, the Latin names of moods and tenses.
- **Gerund and gerundive** are rendered as `VerbForm=Part` with `Aspect=Prosp` and `Voice=Pass`, with no distinction between the two.
- **Harmonisation subtypes**: `advcl:abs`, `advcl:pred`, `obl:arg`, `obl:agent`, `obl:lmod`, free relatives as `:relcl`, plus some subtypes of its own (`cop:outer`, `nsubj:outer`, `csubj:cleft`).
- The *dev* and *test* splits are taken from the *Summa contra Gentiles*.

## References

- Cecchini, F. M., Passarotti, M., Marongiu, P., Zeman, D. (2018). *Challenges in Converting the Index Thomisticus Treebank into Universal Dependencies*. UDW 2018.
