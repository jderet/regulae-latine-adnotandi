# PROIEL

| | |
|---|---|
| Producteur | université d'Oslo, projet *Pragmatic Resources in Old Indo-European Languages* (D. Haug, M. Jøhndal), 2008– |
| Textes latins | Vulgate (Nouveau Testament), César, Cicéron (*Lettres à Atticus*, *De officiis*), Palladius, *Peregrinatio Aetheriae* ; le même format sert au grec du NT, à Hérodote, au gotique, à l'arménien, au vieux slave |
| Format | XML (un élément `<token>` par mot, avec `head-id`, `relation`, `<slash>`) ; export CoNLL-X |
| Normes | D. Haug, *PROIEL guidelines for annotation* (syntaxe) |
| Licence | CC BY-NC-SA 3.0 (États-Unis) |
| Dépôt | <https://github.com/proiel/proiel-treebank> |

PROIEL a été conçu pour comparer des traductions anciennes de la Bible, ce qui explique sa grammaire de dépendance proche de la LFG et ses couches d'annotation supplémentaires (statut informationnel, alignement des traductions).

## Principes

- **Relations** : `pred`, `sub` (sujet), `obj`, `obl` (oblique, régi ou non), `ag` (agent), `adv`, `atr`, `apos`, `comp` (complétive), `xobj` et `xadv` (compléments à sujet contrôlé), `narg` (argument d'un nom), `part` (partitif), `aux` (mots grammaticaux et particules), `voc`, `parpred` (incise), `pid`, `per`.
- **La préposition est tête** de son groupe, et la coordination a pour tête la conjonction (les conjoints portent la relation du groupe).
- **Arêtes secondaires** (`<slash>`) : un second lien, hors de l'arbre, indique le sujet partagé d'un prédicat contrôlé (`xsub`), par exemple le sujet de l'attribut ou de l'infinitif dépendant.
- **Nœuds vides** : un verbe elliptique (`V`) ou une coordination sans conjonction (`C`) reçoivent un nœud sans forme, qui porte la structure.
- **Copule** : *sum* est tête (`pred`), et l'attribut est `xobj`, avec une arête secondaire vers le sujet.
- **Morphologie** : catégorie à 2 lettres (`Nb`, `Ne`, `V-`, `A-`, `Df`, `R-`) et étiquette à 10 positions (personne, nombre, temps, mode, voix, genre, cas, degré, *strength*, flexion). Le mode distingue gérondif (`d`) et adjectif verbal (`g`).
- **Lemmes** avec numéro d'homonyme quand il le faut (`quod#1`).

## Dans les fiches

Chaque fiche montre, sous l'exemple de [UD_Latin-PROIEL](proiel-ud.md), la même phrase dans le PROIEL d'origine. Les nœuds vides y sont notés ∅ et placés en fin de phrase, et les arêtes secondaires sont tracées en pointillés sous la ligne.

## Références

- Haug, D. et Jøhndal, M. (2008). *Creating a Parallel Treebank of the Old Indo-European Bible Translations*. LaTeCH 2008.
- Haug, D. (2010). *PROIEL guidelines for annotation*. <http://folk.uio.no/daghaug/syntactic_guidelines.pdf>
- Syntacticus, interface de consultation des treebanks PROIEL : <https://syntacticus.org>
