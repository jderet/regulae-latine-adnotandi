# UD_Latin-LLCT

| | |
|---|---|
| Producer | T. Korkiakangas (Oslo, Helsinki) for the original annotation; UD conversion by F. M. Cecchini and M. Passarotti (LiLa) |
| Texts | 521 original charters written in Tuscany (Lucca) between 774 and 897: the *Late Latin Charter Treebank* 2 |
| Size (UD 2.18) | 9,023 sentences, 242,411 words |
| Origin | automatic conversion of an annotation in LDT format (the 2007 *Guidelines*, plus rules specific to the charters) |
| Licence | CC BY-SA 4.0 |
| Repository | <https://github.com/UniversalDependencies/UD_Latin-LLCT> |

## Characteristics

- **Non-standard Early Medieval Latin**, with its own spelling, morphology and syntax: *que* for *quae*, accusative after a preposition that governs the ablative (*de ipsum lignamen*), Germanic proper names. The text is kept as written, and the lemma gives the classical form (*Teopaldo* → *Teutpaldus*).
- **Documentary genre**: there are many formulae (dating clauses, subscriptions), which weigh on the frequencies. Most ablative absolutes are dating formulae (*regnante domno nostro…*) annotated as the root of a verbless sentence (see the [page](../phaenomena/ablativus-absolutus.md)).
- **Lemmas are spelled with u/i**, and proper nouns are capitalised. XPOS is a 10-position LDT-style tag separated by bars (`v|v|3|s|p|i|p|-|-|-`).
- **Enclitics**: *-que* is sometimes a multiword token and sometimes a separate word, as the scribe wrote it.
- 223 sentences of LLCT2 are left out of the UD version, pending a satisfactory conversion.

## References

- Cecchini, F. M., Korkiakangas, T., Passarotti, M. (2020). *A New Latin Treebank for Universal Dependencies: Charters between Ancient Latin and Romance Languages*. LREC 2020.
- Korkiakangas, T. (2021). *Late Latin Charter Treebank: contents and annotation*. *Corpora* 16.
