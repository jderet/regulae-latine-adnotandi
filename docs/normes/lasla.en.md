# LASLA

| | |
|---|---|
| Producer | Laboratoire d'Analyse Statistique des Langues Anciennes, University of Liège, founded in 1961 |
| Content | the *Opera Latina* corpus: Classical Latin texts lemmatised and morphologically analysed, semi-automatically, with full manual verification |
| Access | online consultation; the texts are distributed under data-sharing agreements; the links to LiLa are published by CIRCSE (<https://github.com/CIRCSE/LASLA>) |
| Website | <http://web.philo.ulg.ac.be/lasla/> |

## Principles

- **No syntax**: LASLA annotates lemmas and morphology, not dependencies.
- **Lemmas with a homonym index**: each lemma has an index that separates homonyms. It reappears in MISC in [UD_Latin-CIRCSE](circse.md) (`LASLAVariant=2`).
- **Category and inflection code**: a letter for the category and a digit for the inflectional class (`A3`: third-declension noun, `B2`: second-conjugation verb, `C1`: first-class adjective, `M`: adverb). CIRCSE uses it as XPOS.
- **Edited text**: the texts follow the critical editions available at the time of lemmatisation, with the annotators' own editorial choices.

LASLA is the source of the lemmas and morphology of [CIRCSE](circse.md), and it provided the data for the first [EvaLatin](evalatin.md) campaigns.
