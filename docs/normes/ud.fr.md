# Universal Dependencies pour le latin

[Universal Dependencies](https://universaldependencies.org) (UD) est un cadre d'annotation commun à plus de 150 langues. Il fixe 17 catégories (UPOS), un inventaire de traits morphologiques et 37 relations de dépendance universelles, que chaque langue peut préciser par des sous-types (`advcl:abs`, `obl:arg`…). Les mots pleins sont têtes, et les mots grammaticaux en dépendent : la préposition dépend de son nom (`case`), la conjonction de subordination du verbe de la subordonnée (`mark`), la copule de son attribut (`cop`).

Le latin compte six treebanks UD. Trois ont été convertis d'autres formats : [Perseus](perseus.md) depuis le [LDT](ldt.md), [PROIEL](proiel-ud.md) depuis [PROIEL](proiel.md), [ITTB](ittb.md) depuis l'[Index Thomisticus Treebank](it-tb.md). [LLCT](llct.md) a été converti depuis un format LDT, et [CIRCSE](circse.md) et [UDante](udante.md) ont été annotés directement en UD.

## L'harmonisation de 2023

Jusqu'en 2023, chaque treebank suivait ses propres sous-types et traits. F. Gamba et D. Zeman ont alors mené une harmonisation (UD 2.13), décrite dans [*Universalising Latin Universal Dependencies*](https://aclanthology.org/2023.udw-1.2/) et *Latin Morphology through the Centuries* (2023). Elle a rapproché ITTB, LLCT, UDante et Perseus d'un même jeu de sous-types. PROIEL, converti automatiquement de son format d'origine, en reste le plus éloigné.

## Sous-types de relations

Présence de chaque sous-type dans les données UD 2.18. ✓ : le sous-type est employé ; — : il ne l'est pas (la relation de base est alors utilisée).

| Sous-type | Emploi | CIRCSE | Perseus | PROIEL | ITTB | LLCT | UDante |
|---|---|:-:|:-:|:-:|:-:|:-:|:-:|
| `advcl:abs` | ablatif absolu | ✓ | ✓ | — | ✓ | ✓ | ✓ |
| `advcl:pred` | prédicatif (*laetus uenit*) | ✓ | ✓ | — | ✓ | ✓ | ✓ |
| `advcl:cmp`, `obl:cmp` | comparaison | ✓ | ✓ (`advcl:cmp`, `obl:cmp`) | `advcl:cmp` | ✓ | `advcl:cmp` | ✓ |
| `obl:arg` | oblique régi par le verbe | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| `obl:agent` | complément d'agent | ✓ | — | ✓ | ✓ | ✓ | ✓ |
| `obl:lmod`, `obl:tmod` | lieu, temps | ✓ | — | — | ✓ | ✓ | ✓ |
| `advmod:neg`, `:tmod`, `:lmod`, `:emph` | adverbes de négation, de temps, de lieu, d'insistance | ✓ | ✓ | — | ✓ | ✓ | ✓ |
| `acl:relcl` | relative | ✓ | ✓ | — (`acl`) | ✓ | ✓ | ✓ |
| `csubj:relcl`, `ccomp:relcl`, `advcl:relcl` | relative sans antécédent | ✓ | — | — | ✓ | ✓ | ✓ |
| `ccomp:reported` | discours rapporté | ✓ | ✓ | — | ✓ | — | ✓ |
| `conj:expl` | *et* explicatif | ✓ | ✓ | — | ✓ | ✓ | ✓ |

## Lemmes et traits

| | CIRCSE | Perseus | PROIEL | ITTB | LLCT | UDante |
|---|---|---|---|---|---|---|
| Graphie des lemmes | u, i | v | v (et quelques j) | u, i | u, i | u, i |
| Noms propres | minuscule (*cocytus*) | majuscule | majuscule | minuscule | majuscule | minuscule |
| Gérondif, adjectif verbal | `VerbForm=Ger`, `Gdv` (en majorité) | `VerbForm=Part`, `Aspect=Prosp` | `VerbForm=Ger`, `Gdv` | `VerbForm=Part`, `Aspect=Prosp` | `VerbForm=Part`, `Aspect=Prosp` | `VerbForm=Part`, `Aspect=Prosp` |
| Classe flexionnelle (`InflClass`) | oui | non | non | oui | rare | oui |
| Ponctuation | absente (textes sans ponctuation) | `punct` | `punct` | `punct` | `punct` | `punct` |
| Enclitiques (*-que*, *-ne*, *-ue*) | mot multi-token | mot multi-token | token séparé, sans ligne de plage | mot multi-token | variable (charte : *que* souvent écrit à part) | mot multi-token |
| XPOS | codes LASLA | étiquette LDT à 9 positions | catégorie PROIEL à 2 lettres | codes de l'Index Thomisticus | étiquette LDT à 10 positions | codes de DanteSearch |

Les chiffres de chaque cellule ont été mesurés sur les fichiers de la version 2.18 ([méthode](../methode.md)).

## Références

- Documentation UD du latin : <https://universaldependencies.org/la/>
- Gamba, F. et Zeman, D. (2023). *Universalising Latin Universal Dependencies: a harmonisation of Latin treebanks in UD*. UDW 2023. <https://aclanthology.org/2023.udw-1.2/>
- Gamba, F. et Zeman, D. (2023). *Latin Morphology through the Centuries: Ensuring Consistency for Better Language Processing*. ALP 2023.
