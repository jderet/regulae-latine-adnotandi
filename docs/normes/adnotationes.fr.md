# Norme adnotationes-latinae

Le projet *adnotationes-latinae* annote automatiquement l'ensemble du corpus latin de Perseus (*canonical-latinLit*, environ 8,5 millions de mots), à l'aide d'un grand modèle de langue guidé par une norme écrite et par des aides (analyse proposée par UDPipe, lemmes admis par [Collatinus](collatinus.md), valences verbales). Sa norme part de [CIRCSE](circse.md), choisie pour être celle d'[EvaLatin 2024](evalatin.md) et la plus détaillée pour le latin classique. Elle s'en écarte sur les points ci-dessous, chaque fois par une décision motivée.

## Ce qui est repris de CIRCSE

- Les catégories : *sum* toujours AUX ; démonstratifs, possessifs et quantifieurs toujours DET ; *nam*, *enim*, *autem* PART en `discourse`.
- Les relations : `advcl:abs` pour l'ablatif absolu (le participe tête, le nom `nsubj` ou `nsubj:pass`), `advcl:pred` pour le prédicatif, `obl:arg` pour tout oblique régi (le datif de *parco* comme le destinataire de *do*), `obl:agent` (y compris le datif d'agent), les relatives sans antécédent en `:relcl`, `ccomp:reported` et `parataxis:reporting`.
- La copule : seul *sum* est `cop`. *fio*, *uideor*, *appellor* sont des verbes pleins, et leur attribut est `xcomp`. Dans la périphrase obligative (*delenda est*), *sum* est `aux:pass`.
- La coordination : *-que* est `cc` sur la tête du conjoint qui le porte ; les enclitiques sont des mots multi-tokens.

## Ce qui s'en écarte

| Point | CIRCSE | adnotationes-latinae |
|---|---|---|
| Graphie des lemmes | u, i (*uenio*, *iam*) | v, j consonantiques, comme le Lewis & Short (*venio*, *jam*) ; la chaîne travaille en u/i et ne convertit qu'à la publication |
| Noms propres | minuscule (*cocytus*) | majuscule (*Cocytus*), comme le dictionnaire |
| Référence lexicale | lexique du LASLA | vedettes du Lewis & Short, avec `LS=` (identifiant d'article) et `LiLa=` (lemme de la *Lemma Bank*) en MISC ; `Gaffiot=` pour les mots absents du L&S |
| Comparatifs, superlatifs | positif | positif aussi (*maior* → *magnus*) ; le Gaffiot nomme en MISC les degrés qui ont une vedette à part |
| Ponctuation | absente | présente (`punct`), règles UD écrites dans la norme |
| Chiffres romains | — | NUM, `NumForm=Roman`, valeur en MISC ; ordinaux (*legio X*) `amod` et `NumType=Ord` |
| Abréviations | — | point collé au mot ; lemme développé (*M.* → *Marcus*), `Abbr=Yes` |
| Lieu figuré | — | `obl`, avec `LocFig=Yes` en MISC (*in animo*) |
| Prodélision | — | *certumst* découpé en *certum* + *st* (lemme *sum*) |

## Statut

La norme est documentée dans le dépôt du projet. Ses annotations n'étant pas encore publiées, les fiches de ce site ne donnent pas d'exemple pour cette norme. Chaque fiche indique toutefois en quoi elle suit CIRCSE ou s'en écarte.
