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
- **Traits** : dans les tragédies, *Degree=Pos* est marqué et les prépositions portent `AdpType=Prep` ; la *Germanie* suit d'autres conventions (ci-dessous).

## Deux conventions : Sénèque et Tacite

Les deux auteurs n'ont pas été annotés selon les mêmes conventions. La *Germanie* (299 phrases, 5 674 mots, réparties entre train, dev et test) s'écarte des tragédies (1 673 phrases, 23 381 mots) sur les traits et plusieurs catégories. Un analyseur entraîné sur l'ensemble apprend donc les deux usages, et un score calculé sur la seule partie de Tacite mesure en partie l'accord avec ces conventions. Comptes faits sur UD 2.18, les trois parties réunies.

### Traits

| Trait | Sénèque | Tacite |
|---|---|---|
| `AdpType=Prep` sur les prépositions | 100 % de 598 | 0 % de 341 |
| `Degree` sur les adjectifs | 100 % de 3 334 | 18 % de 540 |
| `Degree` sur les participes | 100 % de 1 129 | 0 % de 234 |
| `Degree` sur les adverbes | 81 % de 1 116 | 14 % de 375 |
| `AdvType` sur les adverbes | 1 % | 38 % |
| `Case=Loc` sur un adverbe | jamais | *hic*, *hinc* (`AdvType=Loc\|Case=Loc\|PronType=Dem`) |

### Catégories

| Mots | Sénèque | Tacite |
|---|---|---|
| Peuples | PROPN (*Phryges*, *Danai*) | **NOUN** (*Chatti*, *Suebi*) |
| *Oceanus*, *Penates* | PROPN | NOUN |
| Ethniques employés comme noms (*Germani*, *Galli*) | — | ADJ, lemmes *germanus*, *gallus* |
| *is, ea, id* | rare (DET 2, PRON 2) | **PRON** (44), y compris en `det` |
| *et* adverbe (« aussi, même ») | ADV, `advmod` (29) | **CCONJ**, `advmod` (29) |
| *ceterus* | ADJ (2) | DET (16), ADJ (1) |
| *unus* | NUM (40), DET (7) | DET (11) |

Hors début de phrase, les mots à majuscule sont NOUN 140 fois chez Tacite (110 PROPN, 69 ADJ), une seule fois chez Sénèque (830 PROPN, 235 ADJ).

### Lemmes

Les lemmes suivent les mêmes conventions chez les deux auteurs. Les peuples sont au pluriel, comme les vedettes des dictionnaires (*chatti*, *suebi*, *semnones* ; *phryges*, *pelasgi*) ; seule leur catégorie diffère. Les ethniques que Tacite emploie pour le peuple sont lemmatisés comme des adjectifs (*germanus*, *gallus*, *batauus*).

### Syntaxe

La syntaxe suit les mêmes règles, mais la prose de Tacite les met à l'épreuve plus souvent :

- **propositions sans verbe** : 23 % des phrases de la *Germanie* en contiennent une, contre 2 % chez Sénèque. Ce qui serait l'attribut est tête, même au datif ou adverbe (*hic Suebiae finis* : *hic*). Voir [Proposition sans verbe](../phaenomena/sine-verbo.md) ;
- **ellipse du verbe dans le premier membre** : *raro armis nostris, saepius pecunia iuuantur* (*armis* racine, *raro* `orphan`, *iuuantur* `conj`). `orphan` fait 1,2 % des relations de Tacite, 0,2 % de celles de Sénèque. Voir [Ellipse du verbe](../phaenomena/ellipsis.md).

Quelques analyses de la *Germanie* ne se déduisent d'aucune règle générale : *ea uis numini nomen Alcis* (*ea* racine, *numini* `conj`), *illuc usque* (*usque* `case` de *illuc*), *multum… rationis* (*multum* `det:numgov`), *in consensum uertit* (*consensum* `obj` malgré la préposition).

## Voir aussi

Les fiches de [phénomènes](../phaenomena/index.md), où CIRCSE est toujours donné en premier, et la [norme adnotationes-latinae](adnotationes.md), qui en dérive et suit partout les conventions de Sénèque.
