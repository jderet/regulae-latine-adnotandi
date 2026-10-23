# Verbless clauses

*Omnia praeclara rara*, *hic Suebiae finis*, *paucis loricae*: Latin often leaves out *sum*, especially in historians' prose and in maxims. The clause then has neither a verb nor a copula. Should it be analysed as if *sum* were written, and which word is its head when the predicate is not a nominative adjective but a dative of possession, a genitive or an adverb of place?

## At a glance

| Standard | Head of *hic Suebiae finis* | Subject | What is missing |
|---|---|---|---|
| UD (general rule) | what would be the predicate if *sum* were written | `nsubj` of the predicate | nothing is added; since the copula has no dependents, nothing needs reattaching |
| [CIRCSE](../normes/circse.md) | the predicate, **even a dative, a genitive or an adverb**: *hic*, *genti* (*duriora genti corpora*), *omnium* (*sordes omnium*) | `nsubj` | — |
| [Perseus](../normes/perseus.md) | almost never a nominal head with a subject (5 cases): LDT ellipsis is converted to `conj`, `parataxis` or `vocative` | | |
| [PROIEL (UD)](../normes/proiel-ud.md) | the predicate when the empty verb had an `xobj` (*beatus venter*); otherwise a remnant of the verb, with `orphan` (see [Verb ellipsis](ellipsis.md)) | `nsubj` | |
| [ITTB](../normes/ittb.md), [LLCT](../normes/llct.md) | rare (12 and 3 cases) | | |
| [UDante](../normes/udante.md) | the predicate, often an ablative or a prepositional phrase | `nsubj` | |
| [LDT](../normes/ldt.md) | no empty node: predicate and subject attach to the node above with the `ExD` suffix (`PNOM_ExD_PRED`, `SBJ_ExD_PRED`) | `SBJ_ExD_…` | the verb, marked by `ExD` |
| [PROIEL](../normes/proiel.md) | an **empty node ∅V** (`pred`); the predicate depends on it as `xobj` | `sub` of ∅V, with a secondary `xsub` edge from the predicate | the verb, restored as a node |
| [adnotationes-latinae](../normes/adnotationes.md) | as in CIRCSE: analysed "as if *sum* were written" (decision 68) | `nsubj` | — |

In UD, a clause without a copula raises no question of principle: since *sum* depends on the predicate anyway, its absence only removes a leaf from the tree. The difficulty is to say **what the predicate is** when it does not look like an adjective.

### Points of divergence

- **Tacitus and Seneca in CIRCSE.** The *Germania* uses nominal sentences constantly. By the criteria below, 23% of its sentences contain a clause with neither verb nor copula, against 2% in Seneca's tragedies (17 cases per 1,000 words against 2). CIRCSE applies the rule of the written copula: the head is what would be the predicate, whatever its form.

  | Sentence (Tacitus) | Head in CIRCSE | Subject |
  |---|---|---|
  | *rari excursus et fortuita pugna* | *rari* | *excursus* |
  | *hic Suebiae finis* | *hic* (adverb) | *finis* |
  | *duriora genti corpora* | *genti* (dative of possession) | *corpora* (*duriora* `amod`) |
  | *sordes omnium ac torpor procerum* | *omnium* (genitive) | *sordes* |
  | *paucis loricae* | *paucis* (dative of possession) | *loricae* |

  This is the rule Seneca follows when *est* is written (*cui ultima est fortuna*: *cui* head, *fortuna* `nsubj`). Dative, accusative and adverbial heads thus make up a quarter of Tacitus's cases (25 out of 98).

- **Empty node or promotion.** PROIEL restores the missing verb as an empty node ∅V, whether it is *sum* or a full verb. The conversion to UD removes this node and promotes one of its dependents: the predicate (`xobj`) if there is one, which becomes the head with an `nsubj`; otherwise the most core remnant, with the others as `orphan`. The LDT, which has no empty nodes, keeps a trace of the verb in the `ExD` suffix; the Perseus conversion almost never turns it into a nominal clause.

- **Ellipsis or verbless clause.** When the verb is written in a neighbouring conjunct (*frumentum robustius, sed mensurae minus refundet*), this is not a nominal sentence but the ellipsis of a full verb: see [Verb ellipsis](ellipsis.md). Such cases are left out of the frequencies below.

## Frequencies

Each word that is neither VERB nor AUX, has no `cop` or `aux` among its dependents, has an `nsubj` dependent and stands in a clause position (`root`, `conj`, `parataxis`, `ccomp`, `csubj`, `advcl`, `acl`), excluding the ablative absolute (`advcl:abs`) and the first conjunct of a coordination whose later conjunct carries the verb and shares the subject. Analysis: part of speech of the head, and its case if not nominative.

--8<-- "sine-verbo-frequences.en.md"

In CIRCSE, 98 of the 142 occurrences come from Tacitus (5,674 words), 44 from Seneca (23,381 words).

## Examples

The highlighted words are the head of the clause and its subject. The last example, from the *Germania*, shows a head in the dative of possession.

--8<-- "sine-verbo-exemples.en.md"
