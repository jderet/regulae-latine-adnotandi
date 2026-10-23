# Verb ellipsis

*Libera patriam metu, luctu parentes*; *lamenta ac lacrimas cito, dolorem et tristitiam tarde ponunt*: in a coordination, the verb is often written only once. The conjunct that has lost it (gapping) keeps remnants, here *luctu* and *parentes*, which no longer have a head. Latin, which readily puts the verb last, also leaves it out **in the first conjunct**, not only in later ones.

## At a glance

| Standard | Elliptical conjunct | Remnants | Verb missing from the first conjunct |
|---|---|---|---|
| UD (general rule) | the most core remnant (subject > object > oblique) is promoted to head | the other remnants are `orphan` of that remnant | the first conjunct, with its promoted head, carries the coordination; the conjunct with the verb depends on it as `conj` |
| [CIRCSE](../normes/circse.md) | UD rule | `orphan` | UD rule (Tacitus) |
| [Perseus](../normes/perseus.md) | almost never `orphan` (8 cases): remnants are attached as `conj`, `parataxis`… | | |
| [PROIEL (UD)](../normes/proiel-ud.md) | UD rule, applied **outside coordination** as well (*non in die festo*: verb understood from the context) | `orphan` | UD rule |
| [ITTB](../normes/ittb.md) | UD rule, also widely used in comparative clauses (*sicut…*) as `advcl` | `orphan` | almost never |
| [LLCT](../normes/llct.md) | rare (14 cases) | `orphan` | — |
| [UDante](../normes/udante.md) | UD rule | `orphan` | UD rule |
| [LDT](../normes/ldt.md) | no empty node: remnants attach to the node above (coordination, root) with the `ExD` suffix | `SBJ_ExD_PRED`, `OBJ_ExD_PRED`… | same treatment |
| [PROIEL](../normes/proiel.md) | an **empty node ∅V**, head of the conjunct; remnants depend on it with their real relation (`sub`, `obj`, `adv`) | ordinary relation | same treatment |
| [adnotationes-latinae](../normes/adnotationes.md) | UD rule (decision 50) | `orphan` | UD rule, as in CIRCSE (decision 50, clarified) |

UD adds no node for the missing verb in the basic tree: it elects one of the remnants, and `orphan` signals that the others do not really depend on it. PROIEL, by contrast, restores the verb, and the LDT keeps a trace of it in the `ExD` (*external dependency*) suffix.

### Points of divergence

- **Verb missing from the first conjunct.** In *partem tributorum Sarmatae, partem Quadi… imponunt*, only the second conjunct has its verb. UD and CIRCSE make the verbless first conjunct the head of the whole sentence: *Sarmatae* is the root, the first *partem* its `orphan`, and *imponunt* is `conj` of *Sarmatae*. The structure follows the order of the conjuncts, not the presence of the verb. This case belongs to prose: in CIRCSE, 18 of Tacitus's 54 elliptical clauses are first conjuncts, against only one of Seneca's 54, where the verb is almost always missing from a later conjunct.

  | Sentence (Tacitus) | Root | `orphan` | Verb |
  |---|---|---|---|
  | *raro armis nostris, saepius pecunia iuuantur* | *armis* | *raro* | *iuuantur* `conj` |
  | *iuxta Hermunduros Naristi ac deinde Marcomani et Quadi agunt* | *Naristi* | *Hermunduros* | *agunt* `conj` |
  | *ita sede finibusque in sua ripa, mente animoque nobiscum agunt* | *ripa* | *ita*, *sede* | *agunt* `conj` |

- **Frequency.** `orphan` is rare in the treebanks converted from the LDT (Perseus, LLCT), whose format did not mark ellipsis with a node. It is common in PROIEL, whose empty ∅V nodes (3,007 in the original treebank) become promoted remnants, and in UDante (7.2 elliptical clauses per 1,000 words). In CIRCSE, it is four times as frequent in Tacitus as in Seneca (9.5 against 2.3 elliptical clauses per 1,000 words).

- **Ellipsis outside coordination.** PROIEL restores a verb whenever the sentence implies one, including in an answer or an isolated sentence (*Petrus autem ad eam*; *non in die festo, ne…*). The conversion turns it into a remnant promoted to root with no coordinated conjunct: this is PROIEL's most frequent analysis (39%), and a rare one elsewhere.

- **Comparative clauses.** In ITTB, nearly one elliptical clause in three is a subordinate clause (`advcl`, `advcl:cmp`), mostly introduced by *sicut* (234 cases out of 368), then *ut* and *quam*.

## Frequencies

Each word with at least one `orphan` dependent, that is each elliptical clause, with its position: first conjunct (a root with a `conj`), later conjunct (`conj`), standalone clause (a root with no `conj`) or another relation.

--8<-- "ellipsis-frequences.en.md"

## Examples

The highlighted words are the remnant promoted to head and its `orphan` dependents. The last example, from the *Germania*, shows a verb missing from the first conjunct.

--8<-- "ellipsis-exemples.en.md"
