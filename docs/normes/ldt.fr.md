# Latin Dependency Treebank (LDT / AGDT)

| | |
|---|---|
| Producteur | Perseus Project (Tufts University), puis université de Leipzig ; D. Bamman, G. Crane, G. Celano |
| Textes (LDT 2.1) | Auguste, César (*BG* II, extraits), Cicéron (*Catilinaires*), Jérôme (Vulgate), Virgile (*Énéide* VI), Ovide (*Métamorphoses* I), Pétrone, Phèdre, Properce, Salluste, Suétone, Tacite |
| Format | XML, un élément `<word>` par mot, avec `form`, `lemma`, `postag`, `head`, `relation` |
| Normes | *Guidelines for the Syntactic Annotation of Latin Treebanks* v1.3 (Bamman, Passarotti, Crane, Raynaud, 2007) |
| Licence | CC BY-SA 3.0 (États-Unis) |
| Dépôt | <https://github.com/PerseusDL/treebank_data/tree/master/v2.1/Latin> |

Le LDT est le premier treebank latin (2006). Son équivalent grec, l'*Ancient Greek Dependency Treebank* (AGDT), suit la même norme. Les *Guidelines* de 2007 ont été écrites en commun avec l'équipe de l'[Index Thomisticus Treebank](it-tb.md). Elles adaptent au latin la couche analytique du *Prague Dependency Treebank*. Le format LDT reste celui de l'éditeur Arethusa, de [LLCT](llct.md) et de nombreux projets d'annotation.

## Principes

- **Les mots grammaticaux sont têtes**, à l'inverse d'UD : la préposition domine son nom (`AuxP`), la conjonction de subordination son verbe (`AuxC`), et la conjonction de coordination ses conjoints (`COORD`). Les conjoints portent alors le suffixe `_CO` (`PRED_CO`, `OBJ_CO`).
- **Le verbe *sum* est tête** de la phrase copulative (`PRED`), et l'attribut est `PNOM`.
- **Relations fonctionnelles** : `PRED`, `SBJ`, `OBJ`, `ATR`, `ADV`, `ATV`/`AtvV` (complément prédicatif), `PNOM`, `OCOMP`, `APOS`, `ExD` (élément dont la tête est élidée), et les auxiliaires `AuxP`, `AuxC`, `AuxY` (adverbes de phrase, coordonnants secondaires), `AuxZ` (particules d'insistance), `AuxV` (*sum* auxiliaire), `AuxX` (virgule), `AuxK` (ponctuation finale), `AuxG`.
- **Une seule relation par mot** : le rôle du nom à l'ablatif absolu (`SBJ` du participe) ou de l'accusatif de la proposition infinitive (`SBJ` de l'infinitif) se lit dans la structure.
- **Étiquette morphologique à 9 positions** : catégorie, personne, nombre, temps, mode, voix, genre, cas, degré (`v3spia---` : verbe, 3e personne, singulier, présent, indicatif, actif). Le mode distingue gérondif (`d`) et adjectif verbal (`g`).
- **Lemmes avec numéro d'homonyme** (`sum1`, `hic1`, `-que1`), tirés de l'analyseur Morpheus. Les enclitiques sont des mots séparés écrits avec un tiret (`-que`).

## Dans les fiches

Chaque fiche montre, sous l'exemple de [UD_Latin-Perseus](perseus.md), la même phrase dans le LDT 2.1.

## Références

- Bamman, D., Passarotti, M., Crane, G., Raynaud, S. (2007). *Guidelines for the Syntactic Annotation of Latin Treebanks (v. 1.3)*. <http://hdl.handle.net/10427/42683>
- Bamman, D. et Crane, G. (2006). *The Design and Use of a Latin Dependency Treebank*. TLT 2006.
