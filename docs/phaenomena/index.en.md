# Phenomena

Every page follows the same plan:

1. **Summary**: a table giving, standard by standard, the analysis of the phenomenon, from the UD treebanks to the original formats and the adnotationes-latinae standard;
2. **Points of divergence**: what really separates the standards, with figures;
3. **Frequencies**: for each UD treebank, the most frequent analyses of the phenomenon, counted by the [script](../methode.md);
4. **Examples**: one sentence per treebank, following that treebank's most frequent analysis, with its tree and CoNLL-U lines. For Perseus and PROIEL, the same sentence is added in its original format.

## Pages

| Page | What diverges |
|---|---|
| [Copula: *sum*](copula.md) | which word is the head, *sum* or the predicate; *sum* in the obligative periphrasis |
| [Ablative absolute](ablativus-absolutus.md) | `advcl:abs` or `advcl`; dating formulae |
| [Accusative and infinitive](accusativus-cum-infinitivo.md) | `ccomp` or `csubj`; `xcomp` or `ccomp` after *iubeo*, *sino* |
| [Gerund and gerundive](gerundium-gerundivum.md) | morphological distinction; preposition `case` or `mark` |
| [Coordination with *-que*](coordinatio.md) | splitting; attachment to the host or to the head of the conjunct; *neque* |

## Coming next

- Relative clauses: `acl:relcl`, free relatives (`csubj:relcl`…)
- Comparison: *quam*, ablative of comparison (`obl:cmp`, `advcl:cmp`)
- Governed obliques: argument dative and ablative (`obl:arg`, `iobj`)
- Agent and dative of agent (`obl:agent`)
- Predicative (`advcl:pred`, `xcomp`, `ATV`/`AtvV`, `xadv`)
- Reported speech: *inquit*, direct speech (`parataxis:reporting`, `ccomp:reported`)
- Ellipsis and gapping (`orphan`, PROIEL empty nodes, LDT `ExD`)
- Place and time (`obl:lmod`, `obl:tmod`, `advmod:lmod`)
- Determiners and pronouns (`DET` or `PRON` for *hic*, *ille*, *is*)
- Discourse particles (*nam*, *enim*, *autem*, *quidem*)
- The enclitic *-ne* and questions
- Multiword proper names (`flat:name`) and abbreviations (*M.*, *Kal.*)
- Numbers and Roman numerals
- Lemmas: comparatives and superlatives, u/v and i/j spelling, lexicalised participles, deponents
