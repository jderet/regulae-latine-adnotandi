# Normes

Les normes décrites ici forment trois familles. Les tailles sont celles de la version UD 2.18. Un mot syntaxique est un mot après découpage des enclitiques : *uirumque* compte pour deux.

## Treebanks Universal Dependencies

Ils sont tous au format CoNLL-U et partagent les étiquettes UD. Ils diffèrent toutefois par leur origine (annotation native en UD ou conversion), leurs sous-types de relations, leurs traits et leurs lemmes. Voir [Universal Dependencies pour le latin](ud.md).

| Treebank | Textes | Période | Phrases | Mots | Origine | Licence |
|---|---|---|---:|---:|---|---|
| [CIRCSE](circse.md) | Sénèque (tragédies), Tacite (*Germanie*) | Ier s. | 1 972 | 29 055 | annotation native UD, lemmes et morphologie LASLA | CC BY-SA 4.0 |
| [Perseus](perseus.md) | Auguste, Cicéron, Virgile, Ovide, Pétrone, Salluste, Vulgate… | Ier s. av. – Ve s. | 2 273 | 29 223 | conversion du LDT 2.1 | CC BY-NC-SA 2.5 |
| [PROIEL](proiel-ud.md) | Vulgate (NT), César, Cicéron (*Att.*, *Off.*), Palladius | Ier s. av. – Ve s. | 18 689 | 205 566 | conversion de PROIEL | CC BY-NC-SA 3.0 |
| [ITTB](ittb.md) | Thomas d'Aquin | XIIIe s. | 26 977 | 450 517 | conversion de l'Index Thomisticus Treebank | CC BY-NC-SA 3.0 |
| [LLCT](llct.md) | chartes de Toscane | 774–897 | 9 023 | 242 411 | conversion du format LDT | CC BY-SA 4.0 |
| [UDante](udante.md) | Dante (œuvres latines) | XIVe s. | 1 723 | 55 553 | annotation native UD | CC BY-NC-SA 3.0 |

## Formats d'origine

Ce sont les normes dont les treebanks UD ont été convertis. Elles restent en usage, et leurs choix expliquent bien des particularités des versions UD.

- [LDT / AGDT](ldt.md) : le Latin Dependency Treebank du Perseus Project, avec les *Guidelines* de 2007 ;
- [PROIEL](proiel.md) : le format de l'université d'Oslo, avec nœuds vides et arêtes secondaires ;
- [Index Thomisticus Treebank](it-tb.md) : le style de Prague appliqué à Thomas d'Aquin.

## Lexique et morphologie

Ce sont les conventions de lemmes, de catégories et de graphies : [LASLA](lasla.md), [LiLa](lila.md), [Collatinus](collatinus.md), et les campagnes d'évaluation [EvaLatin](evalatin.md).

## Notre norme

La norme suivie par le projet [adnotationes-latinae](adnotationes.md) pour annoter le corpus latin de Perseus. Elle part de CIRCSE et en note les écarts.
