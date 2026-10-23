# UD_Latin-ITTB

| | |
|---|---|
| Producteur | CIRCSE (Università Cattolica, Milan) et ÚFAL (Prague) |
| Textes | Thomas d'Aquin, *Summa contra Gentiles* ; concordances du mot *forma* dans l'*Index Thomisticus* |
| Taille (UD 2.18) | 26 977 phrases, 450 517 mots : le plus grand treebank latin |
| Origine | conversion automatique de l'[Index Thomisticus Treebank](it-tb.md), au style de Prague ; d'abord via HamleDT (UD 1.2, 2015), conversion refaite en UD 2.3 (Cecchini et al. 2018), harmonisée en UD 2.13 |
| Licence | CC BY-NC-SA 3.0 |
| Dépôt | <https://github.com/UniversalDependencies/UD_Latin-ITTB> |

## Caractéristiques

- **Latin scolastique** : le phénomène le plus visible est la proposition infinitive sujet d'un verbe impersonnel (*oportet*, *necesse est*) : l'infinitif y est `csubj`, plus souvent que `ccomp` (voir la [fiche](../phaenomena/accusativus-cum-infinitivo.md)).
- **Lemmes en minuscules et en u/i**. L'XPOS reprend le code morphologique de l'*Index Thomisticus* de R. Busa (`C1|grn1|casD|gen2`). MISC ajoute `TraditionalMood` et `TraditionalTense`, les noms latins des modes et des temps.
- **Gérondif et adjectif verbal** sont rendus par `VerbForm=Part` avec `Aspect=Prosp` et `Voice=Pass`, sans distinction entre les deux.
- **Sous-types de l'harmonisation** : `advcl:abs`, `advcl:pred`, `obl:arg`, `obl:agent`, `obl:lmod`, relatives sans antécédent en `:relcl`, ainsi que des sous-types propres (`cop:outer`, `nsubj:outer`, `csubj:cleft`).
- Les découpages *dev* et *test* sont pris dans la *Summa contra Gentiles*.

## Références

- Cecchini, F. M., Passarotti, M., Marongiu, P., Zeman, D. (2018). *Challenges in Converting the Index Thomisticus Treebank into Universal Dependencies*. UDW 2018.
