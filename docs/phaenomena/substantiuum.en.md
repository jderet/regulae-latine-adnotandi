# Adjectives and participles used as nouns

*Omnia haec mala* "all these evils", *uidit ferum* "he saw the beast", *iussa perferre* "to carry out the orders", *coniugis, nati, patris* "of the son": an adjective or participle used on its own stands for a noun. The dictionary often gives it an entry of its own (*malum*, *fera*, *iussum*, *natus*), sometimes a mere cross-reference (*mălum, i, v. malus*). Should it be annotated as a noun, under that lemma, or as the adjective or verb it comes from?

## At a glance

| Standard | Part of speech | Lemma |
|---|---|---|
| [CIRCSE](../normes/circse.md) | **NOUN** (94%) | **the noun**: *malum*, *fera*, *natus*, *superi* |
| [Perseus](../normes/perseus.md) | mostly ADJ or VERB, sometimes NOUN | the adjective or verb: *malus*, *ferus*, *iubeo*, *nascor*; but *omnia*, *omnes* as NOUN under their own lemma |
| [PROIEL (UD)](../normes/proiel-ud.md) | mostly ADJ or VERB (67%) | the adjective or verb, except well-established nouns (*mandatum*) |
| [ITTB](../normes/ittb.md) | **NOUN** (86%) | the noun: *bonum*, *malum* |
| [LLCT](../normes/llct.md) | NOUN (82%) | the noun: *mandatum*, *debitum* |
| [UDante](../normes/udante.md) | split: NOUN (52%), ADJ (38%) | split |
| [LDT](../normes/ldt.md) | the category of the adjective (`a`) or participle (`v`) | the adjective or verb |
| [PROIEL](../normes/proiel.md) | `A-` or `V-`; `Nb` for established nouns | the adjective or verb |
| [adnotationes-latinae](../normes/adnotationes.md) | NOUN if Lewis & Short has a noun entry, cross-references included; otherwise ADJ (decision 11) | the dictionary noun |

### Points of divergence

- **Dictionary or form.** CIRCSE, ITTB and LLCT follow the dictionary: a word with a noun entry is NOUN under that lemma, even when the entry is only a cross-reference (*mălum, i, v. malus*). Perseus and PROIEL follow the form: *mala* "evils" stays ADJ under *malus*, *iussa* stays VERB under *iubeo*. The lemma *malum* as NOUN occurs 6 times in Perseus, 70 times in CIRCSE, which has only 10 ADJ *malus*.
- **Perseus is not consistent.** It makes some plurals NOUN under a lemma of their own (*omnia*, *omnes*, *multa*, *pauca*), but leaves *mali*, *ferae* or *bonum* as ADJ. The Sallust survey had shown the same wavering (*mortalis* ADJ 9 times, NOUN once).
- **Participles used as nouns.** *iussum*, *monitum*, *mandatum*, *debitum*, *natus* "son": VERB under the verb in Perseus and PROIEL, with a nominal relation (`obj`, `nmod`); NOUN under the noun in CIRCSE, LLCT and in the adnotationes-latinae standard when Lewis & Short has the entry.
- **Consequence for evaluation.** Between a standard that follows the dictionary and a treebank that follows the form, each such word counts as two errors, of part of speech and of lemma: 31 of each on the adnotationes-latinae poetry control set (Propertius, Phaedrus, Ovid, Virgil).

## Frequencies

Each word of the following list used as a noun (subject, object, oblique, `nmod`, `conj`, `appos` or vocative; not `amod` or `det`), under the noun's lemma or the source word's, when its form fits the noun: *malum* (*malus*), *bonum* (*bonus*), *fera* (*ferus*), *superi* (*superus*), *planum* (*planus*), *cauum* (*cauus*), *penetrale* (*penetralis*), *natus* (*nascor*), *monitum* (*moneo*), *iussum* (*iubeo*), *mandatum* (*mando*), *debitum* (*debeo*). Analysis: part of speech, and own lemma (the noun) or source lemma.

--8<-- "substantiuum-frequences.en.md"

## Examples

The highlighted word is the adjective or participle used as a noun.

--8<-- "substantiuum-exemples.en.md"
