# Index Thomisticus Treebank (IT-TB)

| | |
|---|---|
| Producer | CIRCSE, Università Cattolica del Sacro Cuore, Milan (M. Passarotti), from 2006 |
| Texts | works of Thomas Aquinas, taken from R. Busa's *Index Thomisticus* (nearly 11 million words, lemmatised and analysed from 1949 onwards) |
| Format | analytical style of the *Prague Dependency Treebank* |
| Standard | the same *Guidelines* as the [LDT](ldt.md) (2007), written jointly |
| Browsing | <https://itreebank.marginalia.it> |

## Principles

- **The same relations as the LDT** (`PRED`, `SBJ`, `OBJ`, `ATR`, `ADV`, `PNOM`, `AuxP`, `AuxC`, `COORD`…), with the same choices: function words are heads, and *sum* heads a copular clause.
- **Morphology of the *Index Thomisticus***: Busa's original classification is inflectional and tripartite (nominal inflection, verbal inflection, invariable words). UD parts of speech had to be reconstructed during the conversion, as described in Cecchini et al. (2018).
- The morphological code (`C1|grn1|casD|gen2|vgr1`) is kept as XPOS in [UD_Latin-ITTB](ittb.md).

The pages of this site show only the UD version of the IT-TB.

## References

- Cecchini, F. M., Passarotti, M., Marongiu, P., Zeman, D. (2018). *Challenges in Converting the Index Thomisticus Treebank into Universal Dependencies*. UDW 2018.
