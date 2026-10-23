# Predicative adjectives

*Laetus uenit*, *nudus asto*, *satis uiuus peruenero*, *abeunt securi domum*: the adjective agrees with the subject (or object), but says what state it is in at the time of the action. It is neither an attribute nor the complement of a verb of being (*fio*, *uideor*). UD has no relation of its own for this free predicative: should it attach to the verb or to the noun, as `xcomp`, as `advcl`, or with the `advcl:pred` subtype?

## At a glance

| Standard | *nudus asto* | Attachment | Complement of a verb of being (*fit nudus*) |
|---|---|---|---|
| UD (general rule) | `xcomp` or `advcl`; subtype `advcl:pred` allowed | the verb | `xcomp` |
| [CIRCSE](../normes/circse.md) | **`advcl:pred`** (90%) | the verb | `xcomp` |
| [Perseus](../normes/perseus.md) | **`xcomp`** | **the verb or the noun** (49% and 45%), following the LDT | `xcomp` |
| [PROIEL (UD)](../normes/proiel-ud.md) | `xcomp` or `advcl` | mostly the verb; `acl` on the noun | `xcomp` |
| [ITTB](../normes/ittb.md) | `xcomp` on the verb, or `advcl:pred` on the noun | both | `xcomp` |
| [LLCT](../normes/llct.md) | `xcomp` | the verb | `xcomp` |
| [UDante](../normes/udante.md) | `advcl:pred` (60%), otherwise `xcomp` | the verb | `xcomp` |
| [LDT](../normes/ldt.md) | `ATV` (on the noun) or `AtvV` (on the verb) | both | `PNOM` |
| [PROIEL](../normes/proiel.md) | `xadv` (adverbial) or `xobj`, with a secondary `xsub` edge to the noun | the verb | `xobj` |
| [adnotationes-latinae](../normes/adnotationes.md) | `advcl:pred` (decision 25), as in CIRCSE | the verb | `xcomp` (decision 28) |

### Points of divergence

- **`advcl:pred` or `xcomp`.** CIRCSE introduced `advcl:pred` for the free predicative, and UDante took it up. The converted treebanks stay with `xcomp`, the relation UD first gives to controlled predicative complements: Perseus (94% of its predicatives), LLCT (99%), PROIEL and ITTB (about half). CIRCSE keeps `xcomp` for the complement of verbs of being and of object complements (*fit*, *uidetur*, *reddit*).
- **Verb or noun (Perseus).** The LDT distinguishes a predicative attached to the noun (`ATV`, *miserae… mihi*) from one attached to the verb (`AtvV`). The conversion keeps both heads and uses `xcomp` in both cases: one Perseus predicative in two depends on the noun or pronoun (*forsan et miserae mihi*: *miserae* `xcomp` of *mihi*). Elsewhere the predicative almost always depends on the verb, except in ITTB, which makes a third of its predicatives `advcl:pred` on the noun.
- **Predicative or attribute.** The line is blurred, especially in poetry (*tardas adverterit auris*, *perpetuum deducite carmen*). An attribute (`amod`) is not counted here, so neither is a predicative that a treebank annotated as `amod`.
- **Participles.** The appositive participle raises the same question: see [Participles](participium.md), where CIRCSE uses `advcl:pred` for 22% of its participles.

## Frequencies

Each adjective (ADJ) as `advcl:pred`, `xcomp`, `advcl` or `acl`, without a copula, whose head is not a verb of being or a verb with an object complement (*sum*, *fio*, *uideor*, *uideo*, *maneo*, *appello*, *uoco*, *nomino*, *dico*, *existimo*, *puto*, *iudico*, *reputo*, *aestimo*, *arbitror*, *credo*, *censeo*, *habeo*, *reddo*, *facio*, *efficio*, *creo*, *declaro*, *duco*, *nascor*, *euado*, *exsisto*, *appareo*, *praesto*, *ostendo*, *sentio*, *inuenio*, *relinquo*, *nuncupo*). Analysis: relation of the adjective and part of speech of its head.

--8<-- "praedicatiuum-frequences.en.md"

## Examples

The highlighted words are the adjective and its head. The last example, from Phaedrus, shows a predicative that Perseus attaches to the pronoun.

--8<-- "praedicatiuum-exemples.en.md"
