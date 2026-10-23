# Accusative and infinitive

*Dico te errare*, *oportet deum esse*, *sinite paruulos uenire*: an infinitive with an accusative subject forms a complement clause. It is the object of a verb of saying, thinking or wanting, or the subject of an impersonal verb. Two questions arise: which relation links the infinitive to its verb, and what does the accusative depend on?

## Summary

| Standard | Infinitive → verb | Accusative → |
|---|---|---|
| [CIRCSE](../normes/circse.md), [Perseus](../normes/perseus.md), [PROIEL (UD)](../normes/proiel-ud.md), [LLCT](../normes/llct.md), [UDante](../normes/udante.md) | `ccomp` (object); `csubj` when the clause is a subject (*necesse est*, *oportet*) | the infinitive, as `nsubj` (`nsubj:pass` if the infinitive is passive) |
| [ITTB](../normes/ittb.md) | same rule, but `csubj` is the most frequent case, because of the impersonals of scholastic argument (*oportet*, *manifestum est*, *necesse est*) | same |
| [LDT](../normes/ldt.md) | `OBJ` (`SBJ` when the clause is a subject) | the infinitive, as `SBJ` |
| [PROIEL](../normes/proiel.md) | `comp` | the infinitive, as `sub` |
| [adnotationes-latinae](../normes/adnotationes.md) | `ccomp`, and `csubj` for the subject of an impersonal | the infinitive, as `nsubj` or `nsubj:pass` |

All standards therefore make the accusative the subject of the infinitive, not the object of the main verb. The accusative and infinitive is treated as a full clause. This is not the case for the infinitive complement of *possum*, *uolo* or *incipio*, which has no subject of its own (`xcomp` in UD).

### Points of divergence

- **Subject or object**: the infinitive is `ccomp` or `csubj` depending on the function of the clause. The split depends mostly on the genre of the texts. `csubj` accounts for 59 % of cases in ITTB, 30 % in UDante, 13 % in CIRCSE, and 5 % or less in Perseus, PROIEL and LLCT.
- **Verbs of ordering and permitting** (*iubeo*, *sino*, *cogo*, *ueto* + infinitive): this is the real divergence between treebanks. The accusative can be the object of the main verb, which controls the subject of the infinitive (`xcomp`). It can also be the subject of an accusative-and-infinitive clause (`ccomp`). Perseus and PROIEL mostly choose `ccomp` (*sinite paruulos uenire*: *paruulos* is `nsubj` of *uenire*). CIRCSE, ITTB and LLCT mostly choose `xcomp`.

  | | CIRCSE | Perseus | PROIEL | ITTB | LLCT | UDante |
  |---|---:|---:|---:|---:|---:|---:|
  | `xcomp` | 29 | 9 | 33 | 23 | 12 | 4 |
  | `ccomp` | 8 | 45 | 119 | 7 | 4 | 5 |

- **Infinitive as root** (13 % in Perseus, 8 % in PROIEL): this covers continuous indirect speech, whose introducing verb is in an earlier sentence, and the historical infinitive.

## Frequencies

Infinitives with an accusative subject: relation of the infinitive and relation of the accusative.

--8<-- "accusativus-cum-infinitivo-frequences.en.md"

## Examples

The coloured words are the infinitive and its accusative subject.

--8<-- "accusativus-cum-infinitivo-exemples.en.md"
