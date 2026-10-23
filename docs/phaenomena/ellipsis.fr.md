# Ellipse du verbe

*Libera patriam metu, luctu parentes* ; *lamenta ac lacrimas cito, dolorem et tristitiam tarde ponunt* : dans une coordination, le verbe n'est souvent écrit qu'une fois. Le membre qui l'a perdu (le *gapping* de la grammaire anglaise) garde des restes, ici *luctu* et *parentes*, qui n'ont plus de tête. Le latin, qui place volontiers le verbe en fin de phrase, l'omet aussi **dans le premier membre**, et non seulement dans les suivants.

## En bref

| Norme | Membre elliptique | Restes | Verbe absent du premier membre |
|---|---|---|---|
| UD (règle générale) | le reste le plus central (sujet > objet > oblique) est promu tête | les autres restes en `orphan` de ce reste | le premier membre, tête promue, porte la coordination ; le membre qui a le verbe en dépend en `conj` |
| [CIRCSE](../normes/circse.md) | règle UD | `orphan` | règle UD (Tacite) |
| [Perseus](../normes/perseus.md) | presque jamais `orphan` (8 cas) : les restes sont rattachés en `conj`, `parataxis`… | | |
| [PROIEL (UD)](../normes/proiel-ud.md) | règle UD, appliquée aussi **hors coordination** (*non in die festo* : verbe sous-entendu d'après le contexte) | `orphan` | règle UD |
| [ITTB](../normes/ittb.md) | règle UD, très employée aussi dans les comparatives (*sicut…*) en `advcl` | `orphan` | presque jamais |
| [LLCT](../normes/llct.md) | rare (14 cas) | `orphan` | — |
| [UDante](../normes/udante.md) | règle UD | `orphan` | règle UD |
| [LDT](../normes/ldt.md) | pas de nœud vide : les restes sont rattachés au nœud supérieur (coordination, racine) avec le suffixe `ExD` | `SBJ_ExD_PRED`, `OBJ_ExD_PRED`… | même traitement |
| [PROIEL](../normes/proiel.md) | un **nœud vide ∅V**, tête du membre ; les restes en dépendent avec leur vraie relation (`sub`, `obj`, `adv`) | relation ordinaire | même traitement |
| [adnotationes-latinae](../normes/adnotationes.md) | règle UD (décision 50) | `orphan` | règle UD, comme CIRCSE (décision 50 précisée) |

UD n'ajoute pas de nœud pour le verbe absent dans l'arbre de base : il élit l'un des restes, et `orphan` signale que les autres ne dépendent pas vraiment de lui. PROIEL, à l'inverse, rétablit le verbe, et le LDT garde sa trace dans le suffixe `ExD` (*external dependency*).

### Points de divergence

- **Verbe absent du premier membre.** Dans *partem tributorum Sarmatae, partem Quadi… imponunt*, seul le second membre a son verbe. UD et CIRCSE font du premier membre, privé de verbe, la tête de toute la phrase : *Sarmatae* est racine, le premier *partem* son `orphan`, et *imponunt* est `conj` de *Sarmatae*. La structure suit l'ordre des membres, non la présence du verbe. Ce cas est propre à la prose : dans CIRCSE, 18 des 54 propositions elliptiques de Tacite sont des premiers membres, contre une seule des 54 de Sénèque, où le verbe manque presque toujours dans un membre suivant.

  | Phrase (Tacite) | Racine | `orphan` | Verbe |
  |---|---|---|---|
  | *raro armis nostris, saepius pecunia iuuantur* | *armis* | *raro* | *iuuantur* `conj` |
  | *iuxta Hermunduros Naristi ac deinde Marcomani et Quadi agunt* | *Naristi* | *Hermunduros* | *agunt* `conj` |
  | *ita sede finibusque in sua ripa, mente animoque nobiscum agunt* | *ripa* | *ita*, *sede* | *agunt* `conj` |

- **Fréquence.** `orphan` est rare dans les treebanks convertis du LDT (Perseus, LLCT), dont le format ne distinguait pas l'ellipse par un nœud. Il est courant dans PROIEL, dont les nœuds vides ∅V (3 007 dans le treebank d'origine) deviennent des restes promus, et dans UDante (7,2 propositions elliptiques pour 1 000 mots). Dans CIRCSE, il est quatre fois plus fréquent chez Tacite que chez Sénèque (9,5 contre 2,3 propositions elliptiques pour 1 000 mots).

- **Ellipse hors coordination.** PROIEL rétablit un verbe chaque fois que la phrase en suppose un, y compris dans une réponse ou une phrase isolée (*Petrus autem ad eam* ; *non in die festo, ne…*). La conversion en fait un reste promu racine sans membre coordonné : c'est l'analyse la plus fréquente de PROIEL (39 %), rare ailleurs.

- **Comparatives.** Dans ITTB, près d'une proposition elliptique sur trois est une subordonnée (`advcl`, `advcl:cmp`), introduite surtout par *sicut* (234 cas sur 368), puis *ut* et *quam*.

## Fréquences

Chaque mot qui a au moins un dépendant `orphan`, c'est-à-dire chaque proposition elliptique, avec sa place : premier membre (racine qui a un `conj`), membre suivant (`conj`), proposition seule (racine sans `conj`) ou autre relation.

--8<-- "ellipsis-frequences.fr.md"

## Exemples

Les mots en couleur sont le reste promu tête et ses `orphan`. Le dernier exemple, tiré de la *Germanie*, montre un verbe absent du premier membre.

--8<-- "ellipsis-exemples.fr.md"
