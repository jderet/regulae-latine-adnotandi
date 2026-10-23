# Method

## Data

The examples and figures come from data downloaded at fixed versions by `scripts/telecharger.sh`:

| Data | Version | Source |
|---|---|---|
| Six Latin UD treebanks | UD 2.18 (tag `r2.18` of each repository) | <https://github.com/UniversalDependencies> |
| Latin Dependency Treebank | 2.1, commit `bf4334f` | <https://github.com/PerseusDL/treebank_data> |
| PROIEL (Latin) | commit `8e38896` | <https://github.com/proiel/proiel-treebank> |

## Frequencies

For each phenomenon, a function in `scripts/exemples.py` finds its occurrences in every UD sentence from features and relations. It gives each one an **analysis**, written in UD notation (`part. : advcl:abs · noun : nsubj:pass`). The frequency table counts these analyses. The detection criteria are stated above each table. They are deliberately simple, and therefore imperfect: an ablative absolute whose subject is not in the ablative, for instance, is not counted.

## Choice of examples

For each treebank, the example is drawn from the sentences that follow **that treebank's most frequent analysis**. Among them, the script prefers:

1. a sentence of 6 to 14 words (punctuation excluded);
2. outside charter formulae (LLCT);
3. where the phenomenon appears in its most typical form (for the copula, for instance, a predicate adjective with an overt subject);
4. the one closest to 9 words; on a tie, the first by identifier.

The translations of the chosen sentences are made by hand and stored in `scripts/traductions.tsv` (treebank, `sent_id`, French, English). If an example changes, its translation is missing until it is added.

The choice is therefore deterministic: running the script again gives the same examples. For Perseus and PROIEL, only a sentence present in the original format can be chosen, and its original analysis is shown below it.

## Trees

The script draws the trees as SVG, with no external library. Arcs run from head to dependent, with the relation at the top. Under each word is its category: UPOS for UD, the `postag` tag for the LDT, and the two-letter category for PROIEL. PROIEL empty nodes (∅V, ∅C) are placed at the end of the sentence, and its secondary edges are drawn dotted below the line.

## Reproducing

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./scripts/telecharger.sh
.venv/bin/python scripts/exemples.py
.venv/bin/mkdocs serve
```

The generated fragments (`generes/`) are under version control, so the site can be built without downloading the treebanks again.
