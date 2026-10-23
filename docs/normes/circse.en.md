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
- *Degree=Pos* is marked; in the tragedies, prepositions carry `AdpType=Prep`.

## See also

The [phenomenon pages](../phaenomena/index.md), where CIRCSE always comes first, and the [adnotationes-latinae standard](adnotationes.md), which derives from it.
