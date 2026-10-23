# Governed ablative, genitive and dative

*Abutere patientia nostra*, *obliuiscere caedis*, *parcere subiectis*: some verbs govern a case other than the accusative. Their complement is an argument, just like a direct object, but it does not have that form. UD reserves `obj` for the direct object (in Latin, the accusative) and classes other complements as obliques (`obl`), sometimes marked by the subtype `obl:arg`. Should these complements be `obj`, `obl:arg` or plain `obl`?

## At a glance

| Standard | *utor*, *careo* + abl. | *obliuiscor* + gen. | *parco*, *impero* + dat. | Recipient of *do*, *dico* |
|---|---|---|---|---|
| UD (general rule) | `obl` (subtype `obl:arg` allowed) | `obl` | `obl` or `iobj` | `iobj` or `obl` |
| [CIRCSE](../normes/circse.md) | `obl:arg` | `obl:arg` | `obl:arg` | `obl:arg` |
| [Perseus](../normes/perseus.md) | **`obj`** | **`obj`** | `obl` | mostly `obl:arg`, otherwise `obl` |
| [PROIEL (UD)](../normes/proiel-ud.md), [ITTB](../normes/ittb.md), [UDante](../normes/udante.md) | `obl:arg` | `obl:arg` | `obl:arg` | `obl:arg` |
| [LLCT](../normes/llct.md) | rare (`obl`) | — | `obl:arg` | `obl:arg` |
| [LDT](../normes/ldt.md) | `OBJ`, like the accusative | `OBJ` | `OBJ` | `OBJ` |
| [PROIEL](../normes/proiel.md) | `obl` (oblique argument, distinct from `adv`) | `obl` | `obl` | `obl` |
| [adnotationes-latinae](../normes/adnotationes.md) | `obl:arg` if the valency list gives the verb this case, `obl` otherwise | `obl:arg` | `obl:arg` | `obl:arg` (decision 21) |

`iobj` is almost absent from Latin treebanks: 8 in CIRCSE, 4 in Perseus, 6 in ITTB, 28 in LLCT, 1 in UDante, none in PROIEL. The recipient dative is an oblique like the others.

### Points of divergence

- **`obj` outside the accusative (Perseus).** The LDT does not distinguish cases in its `OBJ` relation, which also covers 1,301 ablatives and 101 genitives in LDT 2.1. The conversion to UD keeps `obj` for the ablative and the genitive: UD Perseus has 198 ablative and 34 genitive `obj` out of 2,501, against 2 and 2 out of 2,772 in CIRCSE. In the *Catilinarians*: *abutere patientia nostra*, *obliuiscere caedis*, and even *meis praesidiis circumclusum*, which is not a governed complement.
- **Dative of intransitive verbs.** Perseus makes the dative of *parco*, *impero*, *noceo* `obl`, but most recipients of *do* and *dico* `obl:arg` (50 out of 72). The other UD treebanks mostly make both `obl:arg`.
- **Argument or adjunct.** `obl:arg` requires knowing which cases the verb governs. PROIEL takes this from its original format, which separates the governed oblique (`obl`) from the adjunct (`adv`). The adnotationes-latinae standard relies on a valency list (Latin-VALLEX, CIRCSE, Lewis & Short) and uses `obl:arg` only when the verb has that case there: a dative or ablative depending on an adjective (*carus*, *dignus*) stays `obl` or `nmod`.

## Frequencies

Each noun, pronoun, determiner or adjective without a preposition, in the ablative, genitive or dative, depending on a verb that governs that case: *utor*, *abutor*, *fruor*, *fungor*, *potior*, *uescor*, *careo*, *egeo*, *indigeo* (ablative); *obliuiscor*, *memini*, *reminiscor*, *misereor* (genitive); *parco*, *impero*, *noceo*, *faueo*, *pareo*, *resisto*, *obsequor*, *studeo*, *inuideo*, *ignosco*, *persuadeo*, *obtempero*, *subuenio*, *medeor* (dative). Analysis: case and relation.

--8<-- "obliqui-frequences.en.md"

## Examples

The highlighted words are the verb and its complement.

--8<-- "obliqui-exemples.en.md"
