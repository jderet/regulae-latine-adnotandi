# Norme adnotationes-latinae

Le projet *adnotationes-latinae* annote automatiquement l'ensemble du corpus latin de Perseus (*canonical-latinLit*, environ 8,5 millions de mots), à l'aide d'un grand modèle de langue guidé par une norme écrite et par des aides (analyse proposée par UDPipe, lemmes admis par [Collatinus](collatinus.md), valences verbales). Sa norme part de [CIRCSE](circse.md), choisie pour être celle d'[EvaLatin 2024](evalatin.md) et la plus détaillée pour le latin classique. Elle s'en écarte sur les points ci-dessous, chaque fois par une décision motivée.

## Ce qui est repris de CIRCSE

- Les catégories : *sum* toujours AUX ; démonstratifs, possessifs et quantifieurs toujours DET ; *nam*, *enim*, *autem* PART en `discourse`.
- Les relations : `advcl:abs` pour l'ablatif absolu (le participe tête, le nom `nsubj` ou `nsubj:pass`), `advcl:pred` pour le prédicatif, `obl:arg` pour tout oblique régi (le datif de *parco* comme le destinataire de *do*), `obl:agent` (y compris le datif d'agent), les relatives sans antécédent en `:relcl`, `ccomp:reported` et `parataxis:reporting`.
- La copule : seul *sum* est `cop`. *fio*, *uideor*, *appellor* sont des verbes pleins, et leur attribut est `xcomp`. Dans la périphrase obligative (*delenda est*), *sum* est `aux:pass`.
- La coordination : *-que* est `cc` sur la tête du conjoint qui le porte ; les enclitiques sont des mots multi-tokens.
- L'ellipse : la [proposition sans verbe](../phaenomena/sine-verbo.md) est analysée comme si *sum* était écrit, l'attribut tête, même au datif, au génitif ou adverbe (*hic Suebiae finis* : *hic*) ; dans l'[ellipse du verbe](../phaenomena/ellipsis.md), le reste le plus central est tête et les autres `orphan`, y compris quand le verbe manque dans le premier membre (*raro armis nostris, saepius pecunia iuuantur* : *armis* racine, *iuuantur* `conj`). Ces deux règles, suivies par CIRCSE dans la *Germanie*, ont été écrites dans la norme après un essai sur Tacite.

## Ce qui s'en écarte

| Point | CIRCSE | adnotationes-latinae |
|---|---|---|
| Graphie des lemmes | u, i (*uenio*, *iam*) | v, j consonantiques, comme le Lewis & Short (*venio*, *jam*) ; la chaîne travaille en u/i et ne convertit qu'à la publication |
| Noms propres | minuscule (*cocytus*) | majuscule (*Cocytus*), comme le dictionnaire |
| Peuples | pluriel (*chatti*) ; PROPN chez Sénèque, NOUN chez Tacite | singulier (*Chattus*), avec `LS=` vers l'article du pluriel ; toujours PROPN |
| Référence lexicale | lexique du LASLA | vedettes du Lewis & Short, avec `LS=` (identifiant d'article) et `LiLa=` (lemme de la *Lemma Bank*) en MISC ; `Gaffiot=` pour les mots absents du L&S |
| Participes lexicalisés (*doctus*, *perditus*, *tacitus*) | VERB, lemme du verbe (1 331 participes VERB, 20 ADJ) | ADJ sous leur propre lemme s'ils ont un article dans le Lewis & Short (décision 10) |
| *propior*, *proximus* | lemme *propior* pour les deux | positif *propinquus*, comme les autres degrés (décision 6) |
| Comparatifs, superlatifs | positif | positif aussi (*maior* → *magnus*) ; le Gaffiot nomme en MISC les degrés qui ont une vedette à part |
| Ponctuation | absente | présente (`punct`), règles UD écrites dans la norme |
| Chiffres romains | — | NUM, `NumForm=Roman`, valeur en MISC ; ordinaux (*legio X*) `amod` et `NumType=Ord` |
| Abréviations | — | point collé au mot ; lemme développé (*M.* → *Marcus*), `Abbr=Yes` |
| Lieu figuré | — | `obl`, avec `LocFig=Yes` en MISC (*in animo*) |
| Prodélision | — | *certumst* découpé en *certum* + *st* (lemme *sum*) |

## Les deux conventions de CIRCSE

CIRCSE n'annote pas la *Germanie* de Tacite comme les tragédies de Sénèque (voir [CIRCSE](circse.md#deux-conventions-seneque-et-tacite)). La norme suit partout celle de Sénèque, qui couvre 80 % du treebank :

| Point | Sénèque et adnotationes-latinae | Tacite |
|---|---|---|
| Traits | `AdpType=Prep`, `Degree=Pos` marqué, pas d'`AdvType` | ni `AdpType` ni, le plus souvent, `Degree` ; `AdvType` fréquent |
| Peuples, *Oceanus*, *Penates* | PROPN | NOUN |
| *is, ea, id* | DET, comme les autres démonstratifs (Sénèque n'en a que 4, partagés) | PRON |
| *et* « aussi, même » | ADV | CCONJ |
| *ceterus*, *unus* | ADJ, NUM | DET |

Les scores calculés sur la partie de Tacite comptent donc comme erreurs des écarts de convention : la chaîne ne peut y dépasser 79 % d'accord sur les traits (98 % sur Sénèque).

## Questions ouvertes

L'évaluation sur les *Catilinaires* et le *Catilina* (UD Perseus) a fait apparaître des cas que la norme ne tranche pas encore, ou tranche autrement que CIRCSE :

- **nom attribut d'un pronom** (*nos consules perferemus*, *ego video consul*) : `xcomp` dans Perseus, et dans CIRCSE pour des noms après *videor* et *fio* ; `appos` est l'autre lecture ;
- ***iam pridem*, *iam diu*** : chaîne d'adverbes (Perseus) ou expression figée (`fixed`) ;
- **rattachement des adverbes** : au verbe, ou à l'adverbe, la préposition ou le nom qu'ils modifient, comme le fait souvent Perseus ;
- **complétive en *ut* et *ne*** après un verbe de demande, d'ordre ou de crainte : la norme écrit `ccomp`, comme UD et PROIEL ; CIRCSE et Perseus ont `advcl` (voir [Complétive en *ut*](../phaenomena/ut-completiva.md)) ;
- ***videor*** : la norme le nomme parmi les verbes pleins et lui donne son propre lemme ; CIRCSE et Perseus n'ont que *video* ;
- ***paucus*, *cunctus*, *reliquus*** : DET dans Perseus, ITTB et (pour les deux premiers) CIRCSE, ADJ dans PROIEL ; la liste des DET de la norme ne les nomme pas ;
- ***igitur*** : CCONJ `cc` dans la norme (décision 15, « comme CIRCSE »), mais CIRCSE n'en a que 4 occurrences, partagées entre `cc` et `discourse` ; Perseus, ITTB, LLCT et UDante le mettent en PART `discourse`, PROIEL en ADV `discourse`. *itaque* (décision 38) est dans le même cas.

Sur ces textes, Perseus suit en outre des conventions propres (catégories, traits, `obj` à l'ablatif, participes, relatives), décrites sur la [page de Perseus](perseus.md#conventions-comparees-a-circse).

## Statut

La norme est documentée dans le dépôt du projet. Ses annotations n'étant pas encore publiées, les fiches de ce site ne donnent pas d'exemple pour cette norme. Chaque fiche indique toutefois en quoi elle suit CIRCSE ou s'en écarte.
