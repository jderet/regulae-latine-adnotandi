# The adnotationes-latinae standard

The *adnotationes-latinae* project automatically annotates the whole Perseus Latin corpus (*canonical-latinLit*, about 8.5 million words) with a large language model. The model is guided by a written standard and by aids (an analysis proposed by UDPipe, the lemmas allowed by [Collatinus](collatinus.md), verb valencies). The standard starts from [CIRCSE](circse.md), chosen because it is the [EvaLatin 2024](evalatin.md) standard and the most detailed one for Classical Latin. It departs from CIRCSE on the points below, each time by a reasoned decision.

## What is taken from CIRCSE

- Parts of speech: *sum* is always AUX; demonstratives, possessives and quantifiers are always DET; *nam*, *enim*, *autem* are PART with `discourse`.
- Relations: `advcl:abs` for the ablative absolute (the participle is the head, the noun is `nsubj` or `nsubj:pass`), `advcl:pred` for the predicative, `obl:arg` for every governed oblique (the dative of *parco* as well as the recipient of *do*), `obl:agent` (including the dative of agent), free relatives as `:relcl`, and `ccomp:reported` and `parataxis:reporting`.
- The copula: only *sum* is `cop`. *fio*, *uideor*, *appellor* are full verbs, and their predicate is `xcomp`. In the obligative periphrasis (*delenda est*), *sum* is `aux:pass`.
- Coordination: *-que* is `cc` on the head of the conjunct that carries it, and enclitics are multiword tokens.
- Ellipsis: a [verbless clause](../phaenomena/sine-verbo.md) is analysed as if *sum* were written, with the predicate as head, even when it is a dative, a genitive or an adverb (*hic Suebiae finis*: *hic*); in [verb ellipsis](../phaenomena/ellipsis.md), the most core remnant is the head and the others are `orphan`, including when the verb is missing from the first conjunct (*raro armis nostris, saepius pecunia iuuantur*: *armis* root, *iuuantur* `conj`). Both rules, which CIRCSE follows in the *Germania*, were written into the standard after a trial on Tacitus.

## Where it departs

| Point | CIRCSE | adnotationes-latinae |
|---|---|---|
| Lemma spelling | u, i (*uenio*, *iam*) | consonantal v, j, as in Lewis & Short (*venio*, *jam*); the pipeline works in u/i and converts only at publication |
| Proper nouns | lowercase (*cocytus*) | capitalised (*Cocytus*), as in the dictionary |
| Peoples | plural (*chatti*); PROPN in Seneca, NOUN in Tacitus | singular (*Chattus*), with `LS=` pointing to the plural entry; always PROPN |
| Lexical reference | LASLA lexicon | Lewis & Short headwords, with `LS=` (entry identifier) and `LiLa=` (*Lemma Bank* lemma) in MISC; `Gaffiot=` for words missing from L&S |
| Lexicalised participles (*doctus*, *perditus*, *tacitus*) | VERB, lemma of the verb (1,331 participles VERB, 20 ADJ) | ADJ under their own lemma if they have an entry in Lewis & Short (decision 10) |
| *propior*, *proximus* | lemma *propior* for both | positive *propinquus*, like other degrees (decision 6) |
| Comparatives, superlatives | positive | positive as well (*maior* → *magnus*); MISC gives the Gaffiot headword for degrees that have an entry of their own |
| Punctuation | absent | present (`punct`), with UD rules written into the standard |
| Roman numerals | — | NUM, `NumForm=Roman`, value in MISC; ordinals (*legio X*) are `amod` with `NumType=Ord` |
| Abbreviations | — | the period stays attached to the word; the lemma is the full word (*M.* → *Marcus*), `Abbr=Yes` |
| Figurative place | — | `obl`, with `LocFig=Yes` in MISC (*in animo*) |
| Prodelision | — | *certumst* split into *certum* + *st* (lemma *sum*) |

## The two conventions of CIRCSE

CIRCSE does not annotate Tacitus's *Germania* as it does Seneca's tragedies (see [CIRCSE](circse.md#two-conventions-seneca-and-tacitus)). The standard follows Seneca's convention throughout, which covers 80% of the treebank:

| Point | Seneca and adnotationes-latinae | Tacitus |
|---|---|---|
| Features | `AdpType=Prep`, `Degree=Pos` marked, no `AdvType` | no `AdpType` and, mostly, no `Degree`; frequent `AdvType` |
| Peoples, *Oceanus*, *Penates* | PROPN | NOUN |
| *is, ea, id* | DET, like the other demonstratives (Seneca has only 4, split) | PRON |
| *et* "also, even" | ADV | CCONJ |
| *ceterus*, *unus* | ADJ, NUM | DET |

Scores computed on the Tacitus part therefore count differences of convention as errors: the pipeline cannot exceed 79% agreement on features there (98% on Seneca).

## Open questions

The evaluation on the *Catilinarians* and the *Catiline* (UD Perseus) brought up cases the standard does not settle yet, or settles differently from CIRCSE:

- **noun predicated of a pronoun** (*nos consules perferemus*, *ego video consul*): `xcomp` in Perseus, and in CIRCSE for nouns after *videor* and *fio*; `appos` is the other reading;
- ***iam pridem*, *iam diu***: a chain of adverbs (Perseus) or a fixed expression (`fixed`);
- **attachment of adverbs**: to the verb, or to the adverb, preposition or noun they modify, as Perseus often does;
- **completive *ut* and *ne* clauses** after a verb of asking, ordering or fearing: the standard has `ccomp`, like UD and PROIEL; CIRCSE and Perseus have `advcl` (see [Completive *ut* clauses](../phaenomena/ut-completiva.md));
- ***videor***: the standard lists it among full verbs and gives it a lemma of its own; CIRCSE and Perseus only have *video*;
- ***paucus*, *cunctus*, *reliquus***: DET in Perseus, ITTB and (for the first two) CIRCSE, ADJ in PROIEL; the standard's list of DET does not name them;
- ***igitur***: CCONJ `cc` in the standard (decision 15, "as in CIRCSE"), but CIRCSE has only 4 occurrences, split between `cc` and `discourse`; Perseus, ITTB, LLCT and UDante make it PART `discourse`, PROIEL ADV `discourse`. *itaque* (decision 38) is in the same situation.

On these texts, Perseus also follows conventions of its own (parts of speech, features, ablative `obj`, participles, relative clauses), described on the [Perseus page](perseus.md#conventions-compared-with-circse).

## Status

The standard is documented in the project repository. Its annotations are not published yet, so the pages of this site give no example for this standard. Each page does say where it follows CIRCSE and where it departs from it.
