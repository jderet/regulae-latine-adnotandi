# Participles

*Possidens paelex domum*, *terribilem picea tectus caligine uultum*, *comminatus eiecit*: a participle agrees with a noun, expressed or not, and at the same time describes a circumstance of the action. Does it depend on the noun (attributive, `acl`) or on the verb (appositive, predicative, `advcl`)? Latin treebanks answer in very different ways, and the point weighs heavily on scores: participles are frequent, and each disagreement is a head error.

## At a glance

| Standard | Participle agreeing with an expressed noun | Participle with no expressed noun (*laetus uenit*) | Substantivised participle |
|---|---|---|---|
| [CIRCSE](../normes/circse.md) | **`acl` on the noun**, even in hyperbaton | `advcl:pred` on the verb | by its function (`obj`, `nsubj`…) |
| [Perseus](../normes/perseus.md) | **`amod` or `nmod`** on the noun, or `advcl` on the verb, depending on the LDT analysis (`ATR` or `ADV`) | `advcl` | by its function |
| [PROIEL (UD)](../normes/proiel-ud.md) | **`advcl` on the verb** most of the time; `acl` on the noun when attributive | `advcl` | by its function |
| [ITTB](../normes/ittb.md), [LLCT](../normes/llct.md) | `acl` on the noun | `advcl` | by its function, often `obl` in ITTB |
| [UDante](../normes/udante.md) | `acl` on the noun | `advcl:pred` | by its function |
| [LDT](../normes/ldt.md) | `ATR` (attribute) or `ADV` (adverbial), sometimes `ATV` / `AtvV` (predicative) | `ADV` | by its function |
| [PROIEL](../normes/proiel.md) | `xadv` on the verb, with a secondary `xsub` edge to the noun; `atr` when attributive | `xadv` | by its function |
| [adnotationes-latinae](../normes/adnotationes.md) | `acl` on the noun, even in hyperbaton (as in CIRCSE) | `advcl:pred` (decision 25) | by its function |

In CIRCSE and in the adnotationes-latinae standard, `amod` is reserved for adjectives: an attributive participle is `acl`. Perseus, which inherits the single `ATR` relation of the LDT, makes it `amod` or `nmod`.

### Points of divergence

- **Noun or verb.** The appositive participle, which describes the subject at the time of the action (*tectus caligine uultum*), depends on the noun in CIRCSE (`acl`, 61% of participles) and on the verb in PROIEL (`advcl`, 69%). The choice comes from the original formats. PROIEL has a relation of its own for predicatives, `xadv`, attached to the verb with a secondary edge to the noun (2,907 participles in the original treebank); the conversion makes it `advcl`. The LDT wavers between `ATR` (1,222 participles in LDT 2.1) and `ADV` (1,134); Perseus inherits the split between `amod` or `nmod` on one side and `advcl` on the other.
- **`advcl:pred`.** CIRCSE reserves this subtype for a participle whose noun is not expressed (*laetus uenit*, *sedens digerit*). It uses it for 22% of its participles, and rarely for a participle agreeing with an expressed noun.
- **`nmod` for an attribute.** Perseus makes 24% of its participles `nmod`, almost as many as `amod` (23%). For the most part these are not substantivised participles depending on a noun (*oculi sequentum*), but attributes agreeing with their noun: *antro aperto*, *ora indignantia*, *tela fabricata*. Both relations render the same LDT `ATR`.
- **Part of speech.** Almost all participles are VERB, in Perseus as in CIRCSE (Perseus: 1,277 out of 1,298; CIRCSE: 1,331 out of 1,363). The adnotationes-latinae standard makes lexicalised participles that have an entry in Lewis & Short ADJ, under their own lemma (*doctus*, *notus*, *perditus*, *tacitus*), which neither CIRCSE nor Perseus does.

## Frequencies

Each participle (`VerbForm=Part`), excluding gerundives and gerunds, periphrases (a participle with `aux` or `cop`), ablative absolutes (`advcl:abs`), roots and conjuncts. Analysis: relation of the participle, and part of speech of its head (a noun in the broad sense, or a verb).

--8<-- "participium-frequences.en.md"

## Examples

The highlighted words are the participle and its head. The last example, from the *Catilinarians*, shows a participle as `amod` in Perseus, where CIRCSE would have `acl`.

--8<-- "participium-exemples.en.md"
