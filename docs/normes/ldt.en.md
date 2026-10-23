# Latin Dependency Treebank (LDT / AGDT)

| | |
|---|---|
| Producer | Perseus Project (Tufts University), then Leipzig University; D. Bamman, G. Crane, G. Celano |
| Texts (LDT 2.1) | Augustus, Caesar (*BG* II, excerpts), Cicero (*In Catilinam*), Jerome (Vulgate), Virgil (*Aeneid* VI), Ovid (*Metamorphoses* I), Petronius, Phaedrus, Propertius, Sallust, Suetonius, Tacitus |
| Format | XML, one `<word>` element per word, with `form`, `lemma`, `postag`, `head`, `relation` |
| Standard | *Guidelines for the Syntactic Annotation of Latin Treebanks* v1.3 (Bamman, Passarotti, Crane, Raynaud, 2007) |
| Licence | CC BY-SA 3.0 (United States) |
| Repository | <https://github.com/PerseusDL/treebank_data/tree/master/v2.1/Latin> |

The LDT is the first Latin treebank (2006). Its Greek counterpart, the *Ancient Greek Dependency Treebank* (AGDT), follows the same standard. The 2007 *Guidelines* were written jointly with the [Index Thomisticus Treebank](it-tb.md) team. They adapt the analytical layer of the *Prague Dependency Treebank* to Latin. The LDT format is still used by the Arethusa editor, by [LLCT](llct.md) and by many annotation projects.

## Principles

- **Function words are heads**, the reverse of UD: a preposition governs its noun (`AuxP`), a subordinating conjunction its verb (`AuxC`), and a coordinating conjunction its conjuncts (`COORD`). The conjuncts then carry the suffix `_CO` (`PRED_CO`, `OBJ_CO`).
- **The verb *sum* is the head** of a copular clause (`PRED`), and the predicate noun or adjective is `PNOM`.
- **Functional relations**: `PRED`, `SBJ`, `OBJ`, `ATR`, `ADV`, `ATV`/`AtvV` (predicative complement), `PNOM`, `OCOMP`, `APOS`, `ExD` (element whose head is elided), and the auxiliaries `AuxP`, `AuxC`, `AuxY` (sentence adverbs, secondary coordinators), `AuxZ` (emphasising particles), `AuxV` (auxiliary *sum*), `AuxX` (comma), `AuxK` (final punctuation), `AuxG`.
- **One relation per word**: the role of the noun in an ablative absolute (`SBJ` of the participle) or of the accusative in an accusative and infinitive (`SBJ` of the infinitive) is read off the structure.
- **9-position morphological tag**: part of speech, person, number, tense, mood, voice, gender, case, degree (`v3spia---`: verb, 3rd person, singular, present, indicative, active). The mood position distinguishes gerund (`d`) and gerundive (`g`).
- **Lemmas carry a homograph number** (`sum1`, `hic1`, `-que1`) and come from the Morpheus analyser. Enclitics are separate words written with a hyphen (`-que`).

## In the phenomenon pages

Each page shows, under the [UD_Latin-Perseus](perseus.md) example, the same sentence in LDT 2.1.

## References

- Bamman, D., Passarotti, M., Crane, G., Raynaud, S. (2007). *Guidelines for the Syntactic Annotation of Latin Treebanks (v. 1.3)*. <http://hdl.handle.net/10427/42683>
- Bamman, D. and Crane, G. (2006). *The Design and Use of a Latin Dependency Treebank*. TLT 2006.
