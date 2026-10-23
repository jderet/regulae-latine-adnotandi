# Proposition sans verbe

*Omnia praeclara rara*, *hic Suebiae finis*, *paucis loricae* : le latin omet souvent *sum*, surtout dans la prose d'historien et dans les sentences. La proposition n'a alors ni verbe ni copule. Faut-il l'analyser comme si *sum* était écrit, et quel mot en est la tête quand l'attribut n'est pas un adjectif au nominatif, mais un datif de possession, un génitif ou un adverbe de lieu ?

## En bref

| Norme | Tête de *hic Suebiae finis* | Sujet | Ce qui manque |
|---|---|---|---|
| UD (règle générale) | ce qui serait l'attribut si *sum* était écrit | `nsubj` de l'attribut | rien n'est ajouté ; la copule n'ayant pas de dépendants, rien n'est à reprendre |
| [CIRCSE](../normes/circse.md) | l'attribut, **même au datif, au génitif ou adverbe** : *hic*, *genti* (*duriora genti corpora*), *omnium* (*sordes omnium*) | `nsubj` | — |
| [Perseus](../normes/perseus.md) | presque jamais une tête nominale avec sujet (5 cas) : l'ellipse du LDT est convertie en `conj`, `parataxis` ou `vocative` | | |
| [PROIEL (UD)](../normes/proiel-ud.md) | l'attribut quand le verbe vide avait un `xobj` (*beatus venter*) ; sinon un reste du verbe, en `orphan` (voir [Ellipse](ellipsis.md)) | `nsubj` | |
| [ITTB](../normes/ittb.md), [LLCT](../normes/llct.md) | rare (12 et 3 cas) | | |
| [UDante](../normes/udante.md) | l'attribut, souvent un ablatif ou un groupe prépositionnel | `nsubj` | |
| [LDT](../normes/ldt.md) | pas de nœud vide : l'attribut et le sujet sont rattachés au nœud supérieur avec le suffixe `ExD` (`PNOM_ExD_PRED`, `SBJ_ExD_PRED`) | `SBJ_ExD_…` | le verbe, signalé par `ExD` |
| [PROIEL](../normes/proiel.md) | un **nœud vide ∅V** (`pred`) ; l'attribut en dépend en `xobj` | `sub` de ∅V, arête secondaire `xsub` depuis l'attribut | le verbe, rétabli comme nœud |
| [adnotationes-latinae](../normes/adnotationes.md) | comme CIRCSE : analyse « comme si *sum* était écrit » (décision 68) | `nsubj` | — |

Pour UD, la proposition sans copule ne pose pas de problème de principe : *sum* étant de toute façon dépendant de l'attribut, son absence ne retire qu'une feuille de l'arbre. La difficulté est de dire **ce qui est l'attribut** quand il n'a pas la forme d'un adjectif.

### Points de divergence

- **Tacite et Sénèque dans CIRCSE.** La *Germanie* fait un usage constant de la phrase nominale. D'après les critères ci-dessous, 23 % de ses phrases contiennent une proposition sans verbe ni copule, contre 2 % dans les tragédies de Sénèque (17 cas pour 1 000 mots contre 2). CIRCSE y applique la règle de la copule écrite : la tête est ce qui serait l'attribut, quelle que soit sa forme.

  | Phrase (Tacite) | Tête dans CIRCSE | Sujet |
  |---|---|---|
  | *rari excursus et fortuita pugna* | *rari* | *excursus* |
  | *hic Suebiae finis* | *hic* (adverbe) | *finis* |
  | *duriora genti corpora* | *genti* (datif de possession) | *corpora* (*duriora* `amod`) |
  | *sordes omnium ac torpor procerum* | *omnium* (génitif) | *sordes* |
  | *paucis loricae* | *paucis* (datif de possession) | *loricae* |

  C'est la règle que suit Sénèque quand *est* est écrit (*cui ultima est fortuna* : *cui* tête, *fortuna* `nsubj`). Les têtes au datif, à l'accusatif ou adverbiales représentent ainsi un quart des cas de Tacite (25 sur 98).

- **Nœud vide ou promotion.** PROIEL rétablit le verbe manquant sous forme d'un nœud vide ∅V, qu'il s'agisse de *sum* ou d'un verbe plein. La conversion vers UD supprime ce nœud et promeut l'un de ses dépendants : l'attribut (`xobj`) s'il y en a un, qui devient tête avec un `nsubj` ; sinon le reste le plus central, avec les autres en `orphan`. Le LDT, qui n'a pas de nœud vide, garde la trace du verbe dans le suffixe `ExD` ; la conversion de Perseus n'en tire presque jamais de proposition nominale.

- **Ellipse ou proposition sans verbe.** Quand le verbe est écrit dans un membre voisin (*frumentum robustius, sed mensurae minus refundet*), il ne s'agit pas d'une phrase nominale, mais de l'ellipse d'un verbe plein : voir la fiche [Ellipse du verbe](ellipsis.md). Ces cas sont exclus des fréquences ci-dessous.

## Fréquences

Chaque mot qui n'est ni VERB ni AUX, n'a ni `cop` ni `aux` parmi ses dépendants, a un dépendant `nsubj` et occupe une place de proposition (`root`, `conj`, `parataxis`, `ccomp`, `csubj`, `advcl`, `acl`), hors ablatif absolu (`advcl:abs`) et hors premier membre d'une coordination dont un membre suivant porte le verbe et partage le sujet. Analyse : catégorie de la tête, et son cas s'il n'est pas le nominatif.

--8<-- "sine-verbo-frequences.fr.md"

Dans CIRCSE, 98 des 142 occurrences viennent de Tacite (5 674 mots), 44 de Sénèque (23 381 mots).

## Exemples

Les mots en couleur sont la tête de la proposition et son sujet. Le dernier exemple, tiré de la *Germanie*, montre une tête au datif de possession.

--8<-- "sine-verbo-exemples.fr.md"
