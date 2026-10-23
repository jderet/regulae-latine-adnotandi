# UD_Latin-UDante

| | |
|---|---|
| Producteur | université de Pise (corpus DanteSearch) et projet LiLa (Università Cattolica, Milan) |
| Textes | Dante, *De vulgari eloquentia*, *Monarchia*, *Épîtres*, *Questio de aqua et terra*, *Églogues* (avec les pièces de Giovanni del Virgilio) |
| Taille (UD 2.18) | 1 723 phrases, 55 553 mots |
| Origine | catégories et morphologie de DanteSearch, revues ; syntaxe annotée à la main, directement en UD |
| Licence | CC BY-NC-SA 3.0 |
| Dépôt | <https://github.com/UniversalDependencies/UD_Latin-UDante> |

## Caractéristiques

- **Latin littéraire du XIVe siècle**, en prose (traités, lettres) et en vers (églogues). Graphies médiévales dans le texte (*Bononie*, *que* pour *quae*), lemmes normalisés.
- **Lemmes en minuscules et en u/i**, noms propres compris (*bononia*). L'XPOS est le code morphologique de DanteSearch (`snp2b`).
- **Annoté à Milan, comme CIRCSE**, et selon les mêmes principes : `advcl:abs`, `advcl:pred`, `obl:arg`, `obl:lmod`, relatives sans antécédent en `:relcl`, `ccomp:reported`. Il a en plus quelques sous-types propres (`nmod:poss`, `csubj:cleft`, `cop:outer`).
- **Gérondif et adjectif verbal** sont rendus par `VerbForm=Part` avec `Aspect=Prosp`, comme dans ITTB.
- `# citation_hierarchy` donne le livre et le paragraphe.

## Références

- Cecchini, F. M., Sprugnoli, R., Moretti, G., Passarotti, M. (2020). *UDante: First Steps Towards the Universal Dependencies Treebank of Dante's Latin Works*. CLiC-it 2020.
