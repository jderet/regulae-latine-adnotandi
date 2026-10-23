# UD_Latin-CIRCSE

| | |
|---|---|
| Producteur | Centre de recherche CIRCSE, Università Cattolica del Sacro Cuore, Milan |
| Textes | Sénèque, *Hercule furieux*, *Agamemnon*, *Œdipe*, *Phéniciennes* ; Tacite, *Germanie* |
| Taille (UD 2.18) | 1 972 phrases, 29 055 mots |
| Origine | tokenisation, lemmes et morphologie reçus du corpus *Opera Latina* du [LASLA](lasla.md) ; syntaxe annotée à la main, directement en UD |
| Licence | CC BY-SA 4.0 |
| Dépôt | <https://github.com/UniversalDependencies/UD_Latin-CIRCSE> |

## Caractéristiques

- **C'est la norme UD la plus récente pour le latin classique**, et la plus riche en sous-types : `advcl:abs`, `advcl:pred`, `obl:arg`, `obl:agent`, `obl:lmod`, `advmod:tmod`, les relatives sans antécédent en `:relcl` (`csubj:relcl`…), `ccomp:reported` et `parataxis:reporting` pour le discours rapporté.
- **Lemmes en minuscules et en u/i**, noms propres compris (*cocytus*, *iuppiter*). L'XPOS reprend le code de catégorie du LASLA (`A3` : nom de la 3e déclinaison, `B2` : verbe de la 2e conjugaison, `M` : adverbe).
- **Pas de ponctuation** : les textes sont fournis sans signes de ponctuation.
- **Gérondif et adjectif verbal** distingués (`VerbForm=Ger`, `VerbForm=Gdv`). Dans la périphrase obligative (*habenda est*), *sum* est `aux:pass` et l'adjectif verbal est tête.
- **MISC** : `LASLAVariant` (indice qui distingue les homonymes dans le lexique du LASLA), `LiLaflcat` (catégorie flexionnelle de [LiLa](lila.md)). Les tragédies indiquent le personnage qui parle (`# speaker`).
- *Degree=Pos* est marqué ; dans les tragédies, les prépositions portent `AdpType=Prep`.

## Voir aussi

Les fiches de [phénomènes](../phaenomena/index.md), où CIRCSE est toujours donné en premier, et la [norme adnotationes-latinae](adnotationes.md), qui en dérive.
