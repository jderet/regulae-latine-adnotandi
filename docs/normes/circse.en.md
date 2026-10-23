# UD_Latin-CIRCSE

| | |
|---|---|
| Producer | CIRCSE Research Centre, Università Cattolica del Sacro Cuore, Milan |
| Texts | Seneca, *Hercules Furens*, *Agamemnon*, *Oedipus*, *Phoenissae*; Tacitus, *Germania* |
| Size (UD 2.18) | 1,972 sentences, 29,055 words |
| Origin | tokenisation, lemmas and morphology received from the [LASLA](lasla.md) *Opera Latina* corpus; syntax annotated by hand, directly in UD |
| Licence | CC BY-SA 4.0 |
| Repository | <https://github.com/UniversalDependencies/UD_Latin-CIRCSE> |

## Characteristics

- **It is the most recent UD standard for Classical Latin**, and the richest in subtypes: `advcl:abs`, `advcl:pred`, `obl:arg`, `obl:agent`, `obl:lmod`, `advmod:tmod`, free relatives as `:relcl` (`csubj:relcl`…), and `ccomp:reported` and `parataxis:reporting` for reported speech.
- **Lemmas are lowercase and spelled with u/i**, proper nouns included (*cocytus*, *iuppiter*). XPOS holds the LASLA category code (`A3`: third-declension noun, `B2`: second-conjugation verb, `M`: adverb).
- **No punctuation**: the texts are supplied without punctuation marks.
- **Gerund and gerundive are distinguished** (`VerbForm=Ger`, `VerbForm=Gdv`). In the obligative periphrasis (*habenda est*), *sum* is `aux:pass` and the gerundive is the head.
- **MISC**: `LASLAVariant` (index distinguishing homonyms in the LASLA lexicon) and `LiLaflcat` ([LiLa](lila.md) inflectional category). The tragedies record the speaking character (`# speaker`).
- **Features**: in the tragedies, *Degree=Pos* is marked and prepositions carry `AdpType=Prep`; the *Germania* follows other conventions (below).

## Two conventions: Seneca and Tacitus

The two authors were not annotated with the same conventions. The *Germania* (299 sentences, 5,674 words, spread over train, dev and test) differs from the tragedies (1,673 sentences, 23,381 words) in features and in several parts of speech. A parser trained on the whole treebank thus learns both usages, and a score computed on the Tacitus part alone partly measures agreement with these conventions. Counts from UD 2.18, all three parts together.

### Features

| Feature | Seneca | Tacitus |
|---|---|---|
| `AdpType=Prep` on prepositions | 100% of 598 | 0% of 341 |
| `Degree` on adjectives | 100% of 3,334 | 18% of 540 |
| `Degree` on participles | 100% of 1,129 | 0% of 234 |
| `Degree` on adverbs | 81% of 1,116 | 14% of 375 |
| `AdvType` on adverbs | 1% | 38% |
| `Case=Loc` on an adverb | never | *hic*, *hinc* (`AdvType=Loc\|Case=Loc\|PronType=Dem`) |

### Parts of speech

| Words | Seneca | Tacitus |
|---|---|---|
| Peoples | PROPN (*Phryges*, *Danai*) | **NOUN** (*Chatti*, *Suebi*) |
| *Oceanus*, *Penates* | PROPN | NOUN |
| Ethnic adjectives used as nouns (*Germani*, *Galli*) | — | ADJ, lemmas *germanus*, *gallus* |
| *is, ea, id* | rare (DET 2, PRON 2) | **PRON** (44), even as `det` |
| adverbial *et* ("also, even") | ADV, `advmod` (29) | **CCONJ**, `advmod` (29) |
| *ceterus* | ADJ (2) | DET (16), ADJ (1) |
| *unus* | NUM (40), DET (7) | DET (11) |

Outside sentence-initial position, capitalised words are NOUN 140 times in Tacitus (110 PROPN, 69 ADJ), only once in Seneca (830 PROPN, 235 ADJ).

### Lemmas

Lemmas follow the same conventions in both authors. Peoples are in the plural, as in dictionary headwords (*chatti*, *suebi*, *semnones*; *phryges*, *pelasgi*); only their part of speech differs. The ethnic words Tacitus uses for the people are lemmatised as adjectives (*germanus*, *gallus*, *batauus*).

### Syntax

Syntax follows the same rules, but Tacitus's prose tests them more often:

- **verbless clauses**: 23% of the sentences of the *Germania* contain one, against 2% in Seneca. What would be the predicate is the head, even a dative or an adverb (*hic Suebiae finis*: *hic*). See [Verbless clauses](../phaenomena/sine-verbo.md);
- **verb missing from the first conjunct**: *raro armis nostris, saepius pecunia iuuantur* (*armis* root, *raro* `orphan`, *iuuantur* `conj`). `orphan` makes up 1.2% of Tacitus's relations, 0.2% of Seneca's. See [Verb ellipsis](../phaenomena/ellipsis.md).

A few analyses in the *Germania* follow from no general rule: *ea uis numini nomen Alcis* (*ea* root, *numini* `conj`), *illuc usque* (*usque* `case` of *illuc*), *multum… rationis* (*multum* `det:numgov`), *in consensum uertit* (*consensum* `obj` despite the preposition).

## See also

The [phenomenon pages](../phaenomena/index.md), where CIRCSE always comes first, and the [adnotationes-latinae standard](adnotationes.md), which derives from it and follows Seneca's conventions throughout.
