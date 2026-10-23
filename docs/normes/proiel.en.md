# PROIEL

| | |
|---|---|
| Producer | University of Oslo, *Pragmatic Resources in Old Indo-European Languages* project (D. Haug, M. Jøhndal), 2008– |
| Latin texts | Vulgate (New Testament), Caesar, Cicero (*Letters to Atticus*, *De officiis*), Palladius, *Peregrinatio Aetheriae*; the same format serves NT Greek, Herodotus, Gothic, Armenian and Old Church Slavonic |
| Format | XML (one `<token>` element per word, with `head-id`, `relation`, `<slash>`); CoNLL-X export |
| Standard | D. Haug, *PROIEL guidelines for annotation* (syntax) |
| Licence | CC BY-NC-SA 3.0 (United States) |
| Repository | <https://github.com/proiel/proiel-treebank> |

PROIEL was designed to compare ancient Bible translations. This explains its LFG-inspired dependency grammar and its additional annotation layers (information status, alignment of translations).

## Principles

- **Relations**: `pred`, `sub` (subject), `obj`, `obl` (oblique, governed or not), `ag` (agent), `adv`, `atr`, `apos`, `comp` (complement clause), `xobj` and `xadv` (complements with a controlled subject), `narg` (argument of a noun), `part` (partitive), `aux` (function words and particles), `voc`, `parpred` (parenthetical), `pid`, `per`.
- **The preposition is the head** of its phrase, and coordination is headed by the conjunction (the conjuncts carry the relation of the whole group).
- **Secondary edges** (`<slash>`): a second link, outside the tree, marks the shared subject of a controlled predicate (`xsub`), for instance the subject of a predicate adjective or of a dependent infinitive.
- **Empty nodes**: an elided verb (`V`) or a coordination without a conjunction (`C`) receives a node with no form, which carries the structure.
- **Copula**: *sum* is the head (`pred`), and the predicate is `xobj`, with a secondary edge to the subject.
- **Morphology**: a 2-letter part of speech (`Nb`, `Ne`, `V-`, `A-`, `Df`, `R-`) and a 10-position tag (person, number, tense, mood, voice, gender, case, degree, strength, inflection). The mood position distinguishes gerund (`d`) and gerundive (`g`).
- **Lemmas** carry a homograph number when needed (`quod#1`).

## In the phenomenon pages

Each page shows, under the [UD_Latin-PROIEL](proiel-ud.md) example, the same sentence in the original PROIEL. Empty nodes are written ∅ and placed at the end of the sentence, and secondary edges are drawn dotted below the line.

## References

- Haug, D. and Jøhndal, M. (2008). *Creating a Parallel Treebank of the Old Indo-European Bible Translations*. LaTeCH 2008.
- Haug, D. (2010). *PROIEL guidelines for annotation*. <http://folk.uio.no/daghaug/syntactic_guidelines.pdf>
- Syntacticus, a browsing interface for the PROIEL treebanks: <https://syntacticus.org>
