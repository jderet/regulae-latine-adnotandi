# Coordination with *-que*

*Senatus populusque Romanus*, *Lauiniaque uenit litora*: the enclitic *-que* coordinates by attaching to the first word of the second conjunct. For *et*, the UD treebanks agree: the first conjunct is the head, the following ones are `conj`, and the conjunction is `cc` on the conjunct it introduces. *-que* raises two further questions. Should it be split from its host, and how? Should it attach to its host, or to the head of the conjunct, which is not always the same word?

## Summary

| Standard | Splitting of *-que* | *-que* attached to | *neque*, *nec* |
|---|---|---|---|
| [CIRCSE](../normes/circse.md), [ITTB](../normes/ittb.md), [UDante](../normes/udante.md) | multiword token (`4-5 uirumque` → `uirum` + `que`) | the head of the conjunct (*Lauiniaque uenit*: *que* → *uenit*) | one word |
| [Perseus](../normes/perseus.md) | multiword token | **its host**, even when the host is not the head of the conjunct | split (*nec* → *ne* + *c*) |
| [PROIEL (UD)](../normes/proiel-ud.md) | separate token, no range line | the head of the conjunct | split (*ne* + *que*) |
| [LLCT](../normes/llct.md) | separate token, since *que* is often written apart in the charters; otherwise multiword token | the head of the conjunct | sometimes split |
| [LDT](../normes/ldt.md) | separate word, written `-que` | *-que* is the **head of the coordination** (`COORD`), and the conjuncts depend on it with the `_CO` suffix | |
| [PROIEL](../normes/proiel.md) | separate word | *que* is the **head of the coordination**, and the conjuncts carry the relation of the group | split |
| [adnotationes-latinae](../normes/adnotationes.md) | multiword token | the head of the conjunct, as in CIRCSE | one word |

The original formats make the conjunction the head of the coordination. UD makes it a dependent of the following conjunct. The conversion must therefore choose which word of the second conjunct *-que* attaches to. The UD rule is to attach the conjunction to the head of the conjunct.

### Points of divergence

- **Host or head of the conjunct.** In *Confremuere omnes studiisque ardentibus ausum talia deposcunt* (Perseus), the second conjunct is *studiis … deposcunt*, whose head is *deposcunt*. Perseus nevertheless attaches *que* to *studiis*, its host, and the coordination can then be read only from the `conj` relation of *deposcunt*. Share of *-que* attached to a host that is not the head of its conjunct:

  | CIRCSE | Perseus | PROIEL | ITTB | LLCT | UDante |
  |---:|---:|---:|---:|---:|---:|
  | 3 % | 65 % | 2 % | 0 % | 0 % | 7 % |

- **Splitting.** This is a tokenisation difference, not a syntactic one. It still matters for evaluation: a parser trained on PROIEL produces a *que* token where the CIRCSE gold text expects a multiword token.
- ***neque* split.** PROIEL splits *neque* into *ne* + *que* (754 cases), and Perseus splits *nec* into *ne* + *c* (100 cases). CIRCSE, ITTB and UDante keep a single word (CCONJ). These cases are excluded from the frequencies below.

## Frequencies

Each *-que* with `cc` (excluding *neque*): splitting (MWT: multiword token; token: separate word), then the word it attaches to (host or other word) and that word's relation.

--8<-- "coordinatio-frequences.en.md"

## Examples

The coloured words are *que*, the word it attaches to and, if different, its host.

--8<-- "coordinatio-exemples.en.md"
