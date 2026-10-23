# UD_Latin-Perseus

| | |
|---|---|
| Producer | Perseus Project (Tufts) and Leipzig University; UD conversion by G. Celano |
| Texts | excerpts from Augustus (*Res gestae*), Cicero (*In Catilinam*), Virgil (*Aeneid* VI), Ovid (*Metamorphoses* I), Petronius, Phaedrus, Propertius, Sallust (*Catiline*), Suetonius (*Augustus*), Tacitus (*Histories*), and the Vulgate |
| Size (UD 2.18) | 2,273 sentences, 29,223 words |
| Origin | automatic conversion of the [Latin Dependency Treebank 2.1](ldt.md) |
| Licence | CC BY-NC-SA 2.5 (LDT 2.1 itself is CC BY-SA 3.0) |
| Repository | <https://github.com/UniversalDependencies/UD_Latin-Perseus> |

## Characteristics

- **It inherits from the LDT**: XPOS is the 9-position LDT tag (`v3spia---`), and MISC keeps the LDT lemma identifier with its homograph number (`LId=mando1`). Each `sent_id` gives the LDT file and sentence number (`phi0690.phi003.perseus-lat1.tb.xml@43`), so the original analysis can be recovered, as the pages of this site do.
- **Lemmas are spelled with v**, and proper nouns are capitalised.
- **It has fewer subtypes** than CIRCSE: no `obl:agent`, no `obl:lmod` / `obl:tmod`, and no free relatives as `:relcl`.
- **Gerund and gerundive**: the conversion renders them as `VerbForm=Part` with `Aspect=Prosp`, whereas the LDT distinguished them by mood (`g` gerundive, `d` gerund).
- Coordination, headed by the conjunction in the LDT (`COORD`), is rebuilt the UD way: the first conjunct is the head, and `cc` attaches to the following conjunct.
- The set is small but varied, poetry included: it is the only UD treebank that covers Virgil and Ovid.

## Conventions compared with CIRCSE

UD Perseus and CIRCSE are almost the same size (29,223 and 29,055 words) and both cover classical literature, but they do not annotate in the same way. A parser that follows CIRCSE loses points on Perseus without making real errors. The differences below were found while evaluating the [adnotationes-latinae](adnotationes.md) pipeline on Cicero's *Catilinarians*, Sallust's *Catiline* and extracts from Propertius, Phaedrus, Ovid and Virgil, then counted over the whole treebank (UD 2.18).

### Parts of speech

| Words | Perseus | CIRCSE |
|---|---|---|
| interrogative adjective *qui* (*quem ad finem*) | *qui* DET (56) | *quis* PRON as `det` (85) |
| *is, ea, id* | PRON (194), DET (39) | PRON in Tacitus; DET in the adnotationes-latinae standard |
| negative *ne* | ADV (99) | PART (56) |
| *ceterus* | DET (20) | DET in Tacitus, ADJ in Seneca |
| *verum* "but" | SCONJ or ADV, lemma *verus* | — |
| *nemo* | NOUN (21) | PRON (24) |
| *quisquam* | DET (17) | PRON (12) |
| *senex* | ADJ (7), NOUN (5) | NOUN (22) |
| *ecce* | PART (7) | INTJ (18) |
| *an*, *quin* | SCONJ (10, 6) | PART (31, 15) |
| *igitur*, *ergo* | PART `discourse` (15), ADV `discourse` (25) | split: CCONJ `cc` (2), PART `discourse` (2) |
| *itaque* | lemma *ita*, ADV `advmod` (23 out of 25) | absent |
| *ne* of split *neque* | ADV `advmod` (90), SCONJ `mark` (10) | *neque* not split |
| subordinating *quo*, *ubi* | ADV `mark` (9 and 6), otherwise SCONJ | SCONJ `mark` |
| *quasi* | ADV `advmod` (8), SCONJ (5) | SCONJ |
| Plural adjectives used as nouns | sometimes NOUN with a lemma of their own: *omnia* (11), *omnes* (8), *multa*, *pauca*; mostly *omnis* DET (81) | DET or ADJ |
| *Kalendae*, *December* | PROPN | — |
| *unus* on a noun | ADJ `amod` (15), NUM `nummod` (12) | NUM `nummod` (31) |
| *inuicem* | PRON (4) | ADV |
| *o* before a vocative | PART `advmod:emph` (8), INTJ `discourse` (3) | PART `advmod:emph` (36) |
| Adjectives and participles used as nouns | under the adjective or verb (*malus*, *ferus*, *iubeo*) | NOUN under the noun (*malum*, *fera*); see [Used as nouns](../phaenomena/substantiuum.md) |

### Lemmas

- **Adverbs under the adjective**: 226 adverbs out of 1,851 (12%) have an adjective of the treebank as their lemma (*facile* → *facilis*, *parum* → *parvus*, *longe* → *longus*, *male* → *malus*); 11 out of 1,491 in CIRCSE.
- ***vos*, *vobis*** under *tu*; *mehercle* under *Hercules* (INTJ).
- **Plurals**: *castrum* (8) beside *castra* (3), *comitium*, *locum* for *loca*.
- **Interrogative adjective** under *qui*, not *quis*; a few connecting relatives under *quis* (*quibus mihi videntur*).
- **Fixed adverbs** under their source word: *facile* under *facilis* (14), *primum* under *primus* (10), *merito* under *mereo* (7), *paulo* under the noun *paulum*.
- **Abbreviated praenomina**: lemma *L*, *C*, *M*…, not expanded; *uti*, *sicuti* keep their own lemma.

### Features

| Feature | Perseus | CIRCSE |
|---|---|---|
| `Degree` on adjectives | 8% | 88% (100% in Seneca) |
| `Polarity=Neg` on *non* | 3 out of 262 | 251 out of 251 |
| `Reflex=Yes` on *suus* | never (129) | always (98) |
| `PronType` of the determiners *qui*, *quidam*, *nullus* | always `Ind` | `Neg` (*nullus*) or `Ind` (*quidam*) |
| `PronType=Int` on *cur*, *ubi*, *quando*… | never | 42 |

Perseus's convention is close to that of Tacitus in CIRCSE (see [CIRCSE](circse.md#two-conventions-seneca-and-tacitus)): few "default" features.

### Syntax

- **`obj` outside the accusative**: 198 ablative and 34 genitive `obj` (*abutere patientia nostra*, *obliviscere caedis*), inherited from the LDT `OBJ`. See [Governed obliques](../phaenomena/obliqui.md).
- **Participles**: `advcl` (28%), `nmod` (24%) or `amod` (23%), depending on whether the LDT had `ADV` or `ATR`; `acl` is rare. See [Participles](../phaenomena/participium.md).
- **Noun predicated of a pronoun**: *nos consules perferemus*, *te imperatorem… desiderant*: the noun is `xcomp` of the pronoun. Perseus has 72 nouns as `xcomp`, CIRCSE 42, mostly after *videor* and *fio*.
- ***iam pridem*, *iam diu***: a chain of adverbs (*pridem* `advmod:tmod` of the verb), not a fixed expression.
- **Infinitive with no subject of its own** (*malo dicere*, *statui parare*): `ccomp` 56 times (CIRCSE: 14), `xcomp` 312 times. See [Accusative and infinitive](../phaenomena/accusativus-cum-infinitivo.md).
- **Free relatives**: never a `:relcl` subtype other than `acl:relcl` (*quae mente agitavi, audistis*: `acl:relcl` of *audistis*). See [Relative clauses](../phaenomena/relativa.md).
- **Completive *ut* and *ne* clauses**: mostly `advcl`, as in CIRCSE. See [Completive *ut* clauses](../phaenomena/ut-completiva.md).
- **Adverb on a noun**: `nmod` (12 cases: *privatim … liberalitate*); CIRCSE has none.
- **Predicative adjective**: `xcomp`, attached to the verb or to the noun following the LDT (`AtvV` or `ATV`), almost never `advcl:pred`. See [Predicative adjectives](../phaenomena/praedicatiuum.md).
- **Copular clause in object position** (*ne solus esset studui*): the predicate head keeps a nominal relation, `obj` (3), where CIRCSE has `advcl` or `ccomp`.
- **Directional *domum***: `obj` (10), as in CIRCSE (16 `obj`, 3 `obl:lmod`).

