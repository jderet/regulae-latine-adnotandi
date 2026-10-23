# Ablative absolute

*Caesare duce*, *urbe capta*, *regnante Hludouuico*: a noun in the ablative and a predicate agreeing with it form an adverbial clause with no conjunction. The predicate is usually a participle, sometimes a noun or an adjective. All standards make the predicate the head of the group and the noun its subject. They differ in the name of the relation that attaches the group to the main verb.

## Summary

| Standard | Participle → main verb | Noun → participle |
|---|---|---|
| [CIRCSE](../normes/circse.md), [Perseus](../normes/perseus.md), [ITTB](../normes/ittb.md), [UDante](../normes/udante.md) | `advcl:abs` | `nsubj:pass` (passive participle) or `nsubj` (active participle) |
| [LLCT](../normes/llct.md) | `advcl:abs`; but the dating formula (*regnante domno nostro…*) is the root of a verbless sentence | same |
| [PROIEL (UD)](../normes/proiel-ud.md) | `advcl`, without a subtype: the ablative absolute is not distinguished from other adverbial participles | same |
| [LDT](../normes/ldt.md) | `ADV` | `SBJ` |
| [PROIEL](../normes/proiel.md) | `adv` | `sub` |
| [adnotationes-latinae](../normes/adnotationes.md) | `advcl:abs`, as in CIRCSE; also for a nominal predicate (*Caesare duce*: *duce* is the head) | `nsubj:pass` or `nsubj` |

The `advcl:abs` subtype makes visible a construction that the original formats marked only by case: in the LDT as in PROIEL, an ablative absolute is an `ADV` / `adv` like any other, recognisable only by its ablative subject.

### Points of divergence

- **The choice between `nsubj` and `nsubj:pass`** depends on the voice of the participle. Passive participles (*urbe capta*) dominate in CIRCSE, Perseus and PROIEL (70 to 80 %). In ITTB and UDante the two are evenly split, because scholastic and medieval Latin uses many present participles (*mediante*, *existente*, *manente*).
- **LLCT**: 70 % of the ablative absolutes found are the dating formula *regnante* (with the ruler's name), annotated as the root of the sentence. The treebank's profile reflects its documentary genre, not a disagreement on the analysis.
- **Nominal predicate** (*me consule*, *Caesare duce*): in the CIRCSE standard, the predicate noun or adjective is the head. The frequencies below count participles only.

## Frequencies

Ablative participles with an ablative subject: relation of the participle and relation of the noun.

--8<-- "ablativus-absolutus-frequences.en.md"

## Examples

The coloured words are the participle and its subject.

--8<-- "ablativus-absolutus-exemples.en.md"
