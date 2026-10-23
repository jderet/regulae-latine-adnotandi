# UD_Latin-Perseus

| | |
|---|---|
| Producteur | Perseus Project (Tufts) et université de Leipzig ; conversion UD par G. Celano |
| Textes | extraits d'Auguste (*Res gestae*), Cicéron (*Catilinaires*), Virgile (*Énéide* VI), Ovide (*Métamorphoses* I), Pétrone, Phèdre, Properce, Salluste (*Catilina*), Suétone (*Auguste*), Tacite (*Histoires*), de la Vulgate |
| Taille (UD 2.18) | 2 273 phrases, 29 223 mots |
| Origine | conversion automatique du [Latin Dependency Treebank 2.1](ldt.md) |
| Licence | CC BY-NC-SA 2.5 (le LDT 2.1 est sous CC BY-SA 3.0) |
| Dépôt | <https://github.com/UniversalDependencies/UD_Latin-Perseus> |

## Caractéristiques

- **Héritier du LDT** : l'XPOS est l'étiquette LDT à 9 positions (`v3spia---`), et MISC garde l'identifiant de lemme LDT avec son numéro d'homonyme (`LId=mando1`). Chaque `sent_id` donne le fichier et le numéro de phrase du LDT (`phi0690.phi003.perseus-lat1.tb.xml@43`). On retrouve ainsi l'analyse d'origine, comme le font les fiches de ce site.
- **Lemmes en v**, noms propres en majuscule.
- **Moins de sous-types** que CIRCSE : pas d'`obl:agent`, ni d'`obl:lmod` / `obl:tmod`, ni de relatives sans antécédent en `:relcl`.
- **Gérondif et adjectif verbal** : la conversion les rend par `VerbForm=Part` avec `Aspect=Prosp`, alors que le LDT les distinguait par le mode (`g` adjectif verbal, `d` gérondif).
- La coordination, tête de la structure dans le LDT (`COORD`), est reconstruite selon UD : premier conjoint tête, `cc` sur le conjoint suivant.
- Ensemble petit mais varié, poésie comprise : c'est le seul treebank UD qui couvre Virgile et Ovide.

## Conventions comparées à CIRCSE

UD Perseus et CIRCSE ont presque la même taille (29 223 et 29 055 mots) et couvrent tous deux la littérature classique, mais ils n'annotent pas de la même façon. Un analyseur qui suit CIRCSE perd des points sur Perseus sans faire de vraie erreur. Les écarts ci-dessous ont été relevés en évaluant la chaîne [adnotationes-latinae](adnotationes.md) sur les *Catilinaires* de Cicéron, le *Catilina* de Salluste et des extraits de Properce, Phèdre, Ovide et Virgile, puis comptés sur tout le treebank (UD 2.18).

### Catégories

| Mots | Perseus | CIRCSE |
|---|---|---|
| *qui* adjectif interrogatif (*quem ad finem*) | *qui* DET (56) | *quis* PRON en `det` (85) |
| *is, ea, id* | PRON (194), DET (39) | PRON chez Tacite ; DET dans la norme adnotationes-latinae |
| *ne* négatif | ADV (99) | PART (56) |
| *ceterus* | DET (20) | DET chez Tacite, ADJ chez Sénèque |
| *verum* « mais » | SCONJ ou ADV, lemme *verus* | — |
| *nemo* | NOUN (21) | PRON (24) |
| *quisquam* | DET (17) | PRON (12) |
| *senex* | ADJ (7), NOUN (5) | NOUN (22) |
| *ecce* | PART (7) | INTJ (18) |
| *an*, *quin* | SCONJ (10, 6) | PART (31, 15) |
| *igitur*, *ergo* | PART `discourse` (15), ADV `discourse` (25) | partagé : CCONJ `cc` (2), PART `discourse` (2) |
| *itaque* | lemme *ita*, ADV `advmod` (23 sur 25) | absent |
| *ne* de *neque* découpé | ADV `advmod` (90), SCONJ `mark` (10) | *neque* non découpé |
| *quo*, *ubi* subordonnants | ADV `mark` (9 et 6), SCONJ sinon | SCONJ `mark` |
| *quasi* | ADV `advmod` (8), SCONJ (5) | SCONJ |
| Adjectifs substantivés au pluriel | NOUN à lemme propre, parfois : *omnia* (11), *omnes* (8), *multa*, *pauca* ; *omnis* DET (81) le plus souvent | DET ou ADJ |
| *Kalendae*, *December* | PROPN | — |
| *unus* sur un nom | ADJ `amod` (15), NUM `nummod` (12) | NUM `nummod` (31) |
| *inuicem* | PRON (4) | ADV |
| *o* devant un vocatif | PART `advmod:emph` (8), INTJ `discourse` (3) | PART `advmod:emph` (36) |
| Adjectifs et participes substantivés | sous l'adjectif ou le verbe (*malus*, *ferus*, *iubeo*) | NOUN sous le nom (*malum*, *fera*) ; voir [Substantivés](../phaenomena/substantiuum.md) |

### Lemmes

- **Adverbes sous l'adjectif** : 226 adverbes sur 1 851 (12 %) ont pour lemme un adjectif du treebank (*facile* → *facilis*, *parum* → *parvus*, *longe* → *longus*, *male* → *malus*) ; 11 sur 1 491 dans CIRCSE.
- ***vos*, *vobis*** sous *tu* ; *mehercle* sous *Hercules* (INTJ).
- **Pluriels** : *castrum* (8) à côté de *castra* (3), *comitium*, *locum* pour *loca*.
- **Interrogatif adjectif** sous *qui*, non sous *quis* ; quelques relatifs de liaison sous *quis* (*quibus mihi videntur*).
- **Adverbes figés** sous le mot d'origine : *facile* sous *facilis* (14), *primum* sous *primus* (10), *merito* sous *mereo* (7), *paulo* sous *paulum* NOUN.
- **Praenomina abrégés** : lemme *L*, *C*, *M*…, sans développement ; *uti*, *sicuti* gardent leur lemme.

### Traits

| Trait | Perseus | CIRCSE |
|---|---|---|
| `Degree` sur les adjectifs | 8 % | 88 % (100 % chez Sénèque) |
| `Polarity=Neg` sur *non* | 3 sur 262 | 251 sur 251 |
| `Reflex=Yes` sur *suus* | jamais (129) | toujours (98) |
| `PronType` des déterminants *qui*, *quidam*, *nullus* | toujours `Ind` | `Neg` (*nullus*) ou `Ind` (*quidam*) |
| `PronType=Int` sur *cur*, *ubi*, *quando*… | jamais | 42 |

La convention de Perseus est proche de celle de Tacite dans CIRCSE (voir [CIRCSE](circse.md#deux-conventions-seneque-et-tacite)) : peu de traits « par défaut ».

### Syntaxe

- **`obj` hors de l'accusatif** : 198 `obj` à l'ablatif et 34 au génitif (*abutere patientia nostra*, *obliviscere caedis*), hérités de l'`OBJ` du LDT. Voir [Compléments régis](../phaenomena/obliqui.md).
- **Participes** : `advcl` (28 %), `nmod` (24 %) ou `amod` (23 %), selon que le LDT avait `ADV` ou `ATR` ; `acl` est rare. Voir [Participe](../phaenomena/participium.md).
- **Nom attribut d'un pronom** : *nos consules perferemus*, *te imperatorem… desiderant* : le nom est `xcomp` du pronom. Perseus a 72 noms en `xcomp`, CIRCSE 42, surtout après *videor* et *fio*.
- ***iam pridem*, *iam diu*** : chaîne d'adverbes (*pridem* `advmod:tmod` du verbe), non expression figée.
- **Infinitif sans sujet propre** (*malo dicere*, *statui parare*) : `ccomp` 56 fois (CIRCSE : 14), `xcomp` 312 fois. Voir [Proposition infinitive](../phaenomena/accusativus-cum-infinitivo.md).
- **Relative sans antécédent** : jamais de sous-type `:relcl` hors d'`acl:relcl` (*quae mente agitavi, audistis* : `acl:relcl` de *audistis*). Voir [Relative](../phaenomena/relativa.md).
- **Complétive en *ut* et *ne*** : `advcl` le plus souvent, comme CIRCSE. Voir [Complétive en *ut*](../phaenomena/ut-completiva.md).
- **Adverbe sur un nom** : `nmod` (12 cas : *privatim … liberalitate*) ; CIRCSE n'en a aucun.
- **Adjectif prédicatif** : `xcomp`, rattaché au verbe ou au nom selon le LDT (`AtvV` ou `ATV`), presque jamais `advcl:pred`. Voir [Adjectif prédicatif](../phaenomena/praedicatiuum.md).
- **Proposition à copule en position d'objet** (*ne solus esset studui*) : la tête attribut garde la relation d'un nom, `obj` (3), là où CIRCSE met `advcl` ou `ccomp`.
- ***domum* de direction** : `obj` (10), comme dans CIRCSE (16 `obj`, 3 `obl:lmod`).

