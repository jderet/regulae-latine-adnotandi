# Copula: *sum*

*Gallia est omnis diuisa*, *uita breuis est*, *Caesar consul erat*: the verb *sum* links a subject to a predicate (adjective, noun, pronoun, prepositional phrase, adverb). It is also an auxiliary (*amatus est*, *delenda est*) and can have a full meaning (*est deus*, "God exists"). The question is which word heads the copular clause: the verb or the predicate.

## Summary

| Standard | Head of *Caesar consul erat* | *sum* | Predicate | Periphrasis *delenda est* |
|---|---|---|---|---|
| UD (all treebanks) | the predicate *consul* | `cop` | head (carries `nsubj`) | see below |
| [CIRCSE](../normes/circse.md), [Perseus](../normes/perseus.md), [ITTB](../normes/ittb.md), [UDante](../normes/udante.md) | predicate | `cop` | head | gerundive is the head, *sum* is `aux:pass` |
| [PROIEL (UD)](../normes/proiel-ud.md) | predicate | `cop` | head | gerundive is the head, *sum* is **`cop`** |
| [LDT](../normes/ldt.md), [IT-TB](../normes/it-tb.md) | ***sum*** (`PRED`) | head | `PNOM` | *sum* is the head, gerundive `PNOM` (measured in LDT 2.1) |
| [PROIEL](../normes/proiel.md) | ***sum*** (`pred`) | head | `xobj`, with a secondary `xsub` edge to the subject | *sum* is the head, gerundive `xobj` |
| [adnotationes-latinae](../normes/adnotationes.md) | predicate | `cop` | head | gerundive is the head, *sum* is `aux:pass` |

UD thus reverses the analysis of the original formats: where the LDT and PROIEL make *sum* the predicate, UD treats it as a function word that depends on the predicate. This choice, shared by all UD languages, aligns Latin with languages that have no overt copula (*omnia praeclara rara*).

### What varies between UD treebanks

- **Only *sum* is a copula.** Verbs of state (*fio*, *uideor*, *maneo*, *appellor*) are full verbs, and their predicate is `xcomp`. No treebank uses `cop` for any verb other than *sum*.
- **Obligative periphrasis** (*delenda est*, *seruandum est*): *sum* is `aux:pass` everywhere except PROIEL, where it stays `cop`. LLCT has almost no occurrences.
- **`aux` auxiliary**: PROIEL uses it for the perfect of deponents (*polliciti sunt*) and the future participle (*facturus est*); ITTB and LLCT mostly for the Late and Medieval Latin periphrasis *sum* + present participle (*est habens*).
- ***sum* as head**: when nothing can be the predicate (*est deus*, *sunt qui dicant*), *sum* heads its clause. This accounts for 10 to 20 % of occurrences in PROIEL, ITTB and LLCT, far fewer in CIRCSE and Perseus.

## Frequencies

Analysis of every occurrence of the lemma *sum*: the relation of *sum*, or "head" when it governs its clause.

--8<-- "copula-frequences.en.md"

## Examples

The coloured words are *sum* and its head.

--8<-- "copula-exemples.en.md"
