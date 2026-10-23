# Adjectif prédicatif

*Laetus uenit*, *nudus asto*, *satis uiuus peruenero*, *abeunt securi domum* : l'adjectif s'accorde avec le sujet (ou l'objet), mais il dit dans quel état se trouve celui-ci au moment de l'action. Ce n'est ni une épithète, ni l'attribut d'un verbe d'état (*fio*, *uideor*). UD n'a pas de relation propre pour ce prédicatif libre : faut-il le rattacher au verbe ou au nom, en `xcomp`, en `advcl`, ou avec le sous-type `advcl:pred` ?

## En bref

| Norme | *nudus asto* | Rattachement | Attribut d'un verbe d'état (*fit nudus*) |
|---|---|---|---|
| UD (règle générale) | `xcomp` ou `advcl` ; sous-type `advcl:pred` permis | le verbe | `xcomp` |
| [CIRCSE](../normes/circse.md) | **`advcl:pred`** (90 %) | le verbe | `xcomp` |
| [Perseus](../normes/perseus.md) | **`xcomp`** | **le verbe ou le nom** (49 % et 45 %), selon le LDT | `xcomp` |
| [PROIEL (UD)](../normes/proiel-ud.md) | `xcomp` ou `advcl` | le verbe le plus souvent ; `acl` sur le nom | `xcomp` |
| [ITTB](../normes/ittb.md) | `xcomp` sur le verbe, ou `advcl:pred` sur le nom | les deux | `xcomp` |
| [LLCT](../normes/llct.md) | `xcomp` | le verbe | `xcomp` |
| [UDante](../normes/udante.md) | `advcl:pred` (60 %), `xcomp` sinon | le verbe | `xcomp` |
| [LDT](../normes/ldt.md) | `ATV` (sur le nom) ou `AtvV` (sur le verbe) | les deux | `PNOM` |
| [PROIEL](../normes/proiel.md) | `xadv` (adverbial) ou `xobj`, avec une arête secondaire `xsub` vers le nom | le verbe | `xobj` |
| [adnotationes-latinae](../normes/adnotationes.md) | `advcl:pred` (décision 25), comme CIRCSE | le verbe | `xcomp` (décision 28) |

### Points de divergence

- **`advcl:pred` ou `xcomp`.** CIRCSE a introduit `advcl:pred` pour le prédicatif libre, et UDante l'a repris. Les treebanks convertis en restent à `xcomp`, la relation que UD donne d'abord aux compléments prédicatifs contrôlés : Perseus (94 % de ses prédicatifs), LLCT (99 %), PROIEL et ITTB (environ la moitié). CIRCSE garde `xcomp` pour l'attribut des verbes d'état et de l'objet (*fit*, *uidetur*, *reddit*).
- **Verbe ou nom (Perseus).** Le LDT distingue l'attribut prédicatif rattaché au nom (`ATV`, *miserae… mihi*) de celui qui est rattaché au verbe (`AtvV`). La conversion garde ces deux têtes et met `xcomp` dans les deux cas : un prédicatif de Perseus sur deux dépend du nom ou du pronom (*forsan et miserae mihi* : *miserae* `xcomp` de *mihi*). Ailleurs, le prédicatif dépend presque toujours du verbe, sauf dans ITTB, qui met en `advcl:pred` sur le nom un tiers de ses prédicatifs.
- **Prédicatif ou épithète.** La frontière est floue, surtout en poésie (*tardas adverterit auris*, *perpetuum deducite carmen*). Une épithète (`amod`) n'est pas comptée ici ; un prédicatif qu'un treebank aurait annoté en `amod` ne l'est donc pas non plus.
- **Participes.** Le participe apposé pose la même question : voir la fiche [Participe](participium.md), où CIRCSE emploie `advcl:pred` pour 22 % de ses participes.

## Fréquences

Chaque adjectif (ADJ) en `advcl:pred`, `xcomp`, `advcl` ou `acl`, sans copule, dont la tête n'est pas un verbe d'état ou à attribut de l'objet (*sum*, *fio*, *uideor*, *uideo*, *maneo*, *appello*, *uoco*, *nomino*, *dico*, *existimo*, *puto*, *iudico*, *reputo*, *aestimo*, *arbitror*, *credo*, *censeo*, *habeo*, *reddo*, *facio*, *efficio*, *creo*, *declaro*, *duco*, *nascor*, *euado*, *exsisto*, *appareo*, *praesto*, *ostendo*, *sentio*, *inuenio*, *relinquo*, *nuncupo*). Analyse : relation de l'adjectif et catégorie de sa tête.

--8<-- "praedicatiuum-frequences.fr.md"

## Exemples

Les mots en couleur sont l'adjectif et sa tête. Le dernier exemple, tiré de Phèdre, montre un prédicatif que Perseus rattache au pronom.

--8<-- "praedicatiuum-exemples.fr.md"
