# Compléments régis à l'ablatif, au génitif et au datif

*Abutere patientia nostra*, *obliuiscere caedis*, *parcere subiectis* : certains verbes régissent un autre cas que l'accusatif. Leur complément est un argument, au même titre qu'un objet direct, mais il n'en a pas la forme. UD réserve `obj` à l'objet direct (en latin, l'accusatif) et range les autres compléments parmi les obliques (`obl`), en les distinguant parfois par le sous-type `obl:arg`. Faut-il appeler ces compléments `obj`, `obl:arg` ou simplement `obl` ?

## En bref

| Norme | *utor*, *careo* + abl. | *obliuiscor* + gén. | *parco*, *impero* + dat. | Destinataire de *do*, *dico* |
|---|---|---|---|---|
| UD (règle générale) | `obl` (sous-type `obl:arg` permis) | `obl` | `obl` ou `iobj` | `iobj` ou `obl` |
| [CIRCSE](../normes/circse.md) | `obl:arg` | `obl:arg` | `obl:arg` | `obl:arg` |
| [Perseus](../normes/perseus.md) | **`obj`** | **`obj`** | `obl` | `obl:arg` le plus souvent, `obl` sinon |
| [PROIEL (UD)](../normes/proiel-ud.md), [ITTB](../normes/ittb.md), [UDante](../normes/udante.md) | `obl:arg` | `obl:arg` | `obl:arg` | `obl:arg` |
| [LLCT](../normes/llct.md) | rare (`obl`) | — | `obl:arg` | `obl:arg` |
| [LDT](../normes/ldt.md) | `OBJ`, comme l'accusatif | `OBJ` | `OBJ` | `OBJ` |
| [PROIEL](../normes/proiel.md) | `obl` (argument oblique, distinct de `adv`) | `obl` | `obl` | `obl` |
| [adnotationes-latinae](../normes/adnotationes.md) | `obl:arg` si la liste de valence donne ce cas au verbe, `obl` sinon | `obl:arg` | `obl:arg` | `obl:arg` (décision 21) |

`iobj` est presque absent des treebanks latins : 8 dans CIRCSE, 4 dans Perseus, 6 dans ITTB, 28 dans LLCT, 1 dans UDante, aucun dans PROIEL. Le datif du destinataire y est un oblique comme les autres.

### Points de divergence

- **`obj` hors de l'accusatif (Perseus).** Le LDT ne distingue pas les cas dans sa relation `OBJ`, qui couvre aussi 1 301 ablatifs et 101 génitifs dans le LDT 2.1. La conversion vers UD garde `obj` pour l'ablatif et le génitif : UD Perseus compte 198 `obj` à l'ablatif et 34 au génitif sur 2 501, contre 2 et 2 sur 2 772 dans CIRCSE. Dans les *Catilinaires* : *abutere patientia nostra*, *obliuiscere caedis*, et même *meis praesidiis circumclusum*, qui n'est pas un complément régi.
- **Datif des verbes intransitifs.** Perseus met en `obl` le datif de *parco*, *impero*, *noceo*, mais en `obl:arg` la plupart des destinataires de *do* et *dico* (50 sur 72). Les autres treebanks UD mettent le plus souvent les deux en `obl:arg`.
- **Argument ou circonstant.** `obl:arg` suppose de savoir quels cas le verbe régit. PROIEL le tire de son format d'origine, qui sépare l'oblique régi (`obl`) du circonstant (`adv`). La norme adnotationes-latinae s'appuie sur une liste de valence (Latin-VALLEX, CIRCSE, Lewis & Short) et ne met `obl:arg` que si le verbe y a ce cas : un datif ou un ablatif qui dépend d'un adjectif (*carus*, *dignus*) reste `obl` ou `nmod`.

## Fréquences

Chaque nom, pronom, déterminant ou adjectif sans préposition, à l'ablatif, au génitif ou au datif, qui dépend d'un verbe régissant ce cas : *utor*, *abutor*, *fruor*, *fungor*, *potior*, *uescor*, *careo*, *egeo*, *indigeo* (ablatif) ; *obliuiscor*, *memini*, *reminiscor*, *misereor* (génitif) ; *parco*, *impero*, *noceo*, *faueo*, *pareo*, *resisto*, *obsequor*, *studeo*, *inuideo*, *ignosco*, *persuadeo*, *obtempero*, *subuenio*, *medeor* (datif). Analyse : cas et relation.

--8<-- "obliqui-frequences.fr.md"

## Exemples

Les mots en couleur sont le verbe et son complément.

--8<-- "obliqui-exemples.fr.md"
