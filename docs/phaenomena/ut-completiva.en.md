# Completive *ut* and *ne* clauses

*Rogabat eum ut daemonium eiceret*, *decreuit ne quid res publica detrimenti caperet*, *timui ne… descenderet*: after verbs of asking, ordering, striving and fearing, a clause with *ut* or *ne* and the subjunctive states what is asked, ordered or feared. It stands in place of an object, like the infinitive after *iubeo*; but it has the form of a purpose clause (*ut* + subjunctive), which UD classes among adverbial clauses. Is it `ccomp` or `advcl`?

## At a glance

| Standard | *rogo ut*, *impero ut*, *timeo ne* | Purpose clause (*uenit ut uideret*) |
|---|---|---|
| UD (general rule) | `ccomp`: the clause is an argument of the verb | `advcl` |
| [CIRCSE](../normes/circse.md) | **`advcl`**, like a purpose clause (`ccomp` almost never) | `advcl` |
| [Perseus](../normes/perseus.md) | mostly `advcl`, otherwise `ccomp` | `advcl` |
| [PROIEL (UD)](../normes/proiel-ud.md) | **`ccomp`** (83%) | `advcl` |
| [ITTB](../normes/ittb.md), [UDante](../normes/udante.md) | split (few cases) | `advcl` |
| [LLCT](../normes/llct.md) | `ccomp` (76%) | `advcl` |
| [LDT](../normes/ldt.md) | the conjunction (`AuxC`) is the head; the verb below it bears the function of the clause, `OBJ` or, most often, `ADV` (*timui ne… descenderet*) | `ADV` |
| [PROIEL](../normes/proiel.md) | the conjunction is the head, as `comp` (completive), distinct from `adv`; the verb depends on it as `pred` | `adv` |
| [adnotationes-latinae](../normes/adnotationes.md) | **`ccomp`**, like UD and PROIEL, but against CIRCSE | `advcl` |

### Points of divergence

- **CIRCSE against UD.** The UD guidelines make the completive clause `ccomp`, and PROIEL, which already distinguished `comp` from `adv` in its original format, keeps to this. CIRCSE makes every *ut* or *ne* clause with the subjunctive `advcl`: 75 `advcl` against 1 `ccomp` in the whole treebank, whatever the verb. Form prevails over function.
- **The adnotationes-latinae standard departs from CIRCSE here.** It prescribes `ccomp` for *ut* clauses after verbs of asking, ordering and fearing. The choice is defensible (it is UD's), but it counts as errors, on CIRCSE and on Perseus, analyses that follow these treebanks: 9 differences on Sallust's *Catiline* (*effecerat ut… proderet*, *decreuit… ne quid… caperet*). The question remains open.
- **Perseus.** In the LDT, the verb under the conjunction bears the function of the whole clause: `OBJ` for a completive, `ADV` for an adverbial clause. *ut* clauses are mostly `ADV` there (under *ut*, 287 `ADV` verbs against 28 `OBJ` in LDT 2.1), even after a verb of fearing. The conversion keeps this trace (`advcl` against `ccomp`).
- **Little data.** Outside PROIEL (296 cases), the completive clauses found here are rare: 9 in CIRCSE, 28 in Perseus, fewer than 20 in ITTB, LLCT and UDante. The percentages for these treebanks are therefore fragile.

## Frequencies

Each subjunctive verb whose `mark` is *ut*, *uti* or *ne* and which depends on a verb of asking, ordering, striving or fearing: *rogo*, *oro*, *postulo*, *precor*, *obsecro*, *flagito*, *exoro*, *impetro*, *impero*, *praecipio*, *edico*, *decerno*, *statuo*, *moneo*, *admoneo*, *hortor*, *persuadeo*, *suadeo*, *efficio*, *perficio*, *curo*, *caueo*, *permitto*, *timeo*, *metuo*, *uereor*. The search is lexical: a purpose clause depending on one of these verbs is counted too. Analysis: relation of the clause.

--8<-- "ut-completiva-frequences.en.md"

## Examples

The highlighted words are the main verb, the conjunction and the verb of the completive clause.

--8<-- "ut-completiva-exemples.en.md"
