# Gerund and gerundive

*ars amandi*, *ad pacem petendam*, *Carthago delenda est*: the gerund (a verbal noun: *amandi*) and the gerundive in *-ndus* (a verbal adjective: *petendam*, *delenda*) share the same form. They raise three questions for the standards. Should they be distinguished in the morphology? In *ad pacem petendam*, which word is the head, the noun or the gerundive? And is the preposition `case`, as before a noun, or `mark`, as before a clause?

## Summary

| Standard | Morphology | *ad (pacem) petendam* | *delenda est* |
|---|---|---|---|
| [CIRCSE](../normes/circse.md) | `VerbForm=Ger` / `VerbForm=Gdv` (mostly) | *-nd-* form is the head, preposition `mark` (only 3 cases) | gerundive is the head, *sum* is `aux:pass` |
| [PROIEL (UD)](../normes/proiel-ud.md) | `VerbForm=Ger` / `VerbForm=Gdv` | *-nd-* form is the head, preposition **`case`**, noun as `nsubj` | gerundive is the head, *sum* is `cop` |
| [ITTB](../normes/ittb.md) | `VerbForm=Part`, `Aspect=Prosp`, `Voice=Pass`: no distinction | *-nd-* form is the head, preposition **`case`**, noun as `obj` or `nsubj:pass` | gerundive is the head, *sum* is `aux:pass` |
| [LLCT](../normes/llct.md), [UDante](../normes/udante.md) | `VerbForm=Part`, `Aspect=Prosp`, `Voice=Pass` | *-nd-* form is the head, preposition **`mark`**; but in a quarter (UDante) to a third (LLCT) of cases the noun is the head and the gerundive is `acl` | gerundive is the head, *sum* is `aux:pass` (UDante) |
| [Perseus](../normes/perseus.md) | `VerbForm=Part`, `Aspect=Prosp`, `Voice=Pass` | varies (few examples) | gerundive is the head, *sum* is `aux:pass` |
| [LDT](../normes/ldt.md) | mood `d` (gerund) / `g` (gerundive) in the tag | the preposition is the head (`AuxP`); under it, usually the *-nd-* form, sometimes the noun with the gerundive as `ATR` | *sum* is the head, gerundive `PNOM` |
| [PROIEL](../normes/proiel.md) | mood `d` / `g` in the tag | the preposition is the head; the *-nd-* form depends on it (`obl`) | *sum* is the head, gerundive `xobj` |
| [adnotationes-latinae](../normes/adnotationes.md) | as in CIRCSE: `Ger` / `Gdv`; UPOS VERB, lemma of the verb | not settled by the written standard | gerundive is the head, *sum* is `aux:pass` |

### Points of divergence

- **The morphological distinction** exists in both original formats (LDT and PROIEL), and in UD in CIRCSE and PROIEL. It is lost in Perseus, ITTB, LLCT and UDante, which render both forms as a passive "prospective" participle (`Aspect=Prosp`, like the future participle, but with `Voice=Pass`). Finding a gerund there requires context as well (neuter singular with no agreeing noun).
- **The prepositional phrase**: all UD treebanks usually make the *-nd-* form the head of the phrase. They differ in the relation of the preposition. PROIEL and ITTB treat it as before a noun (`case`). LLCT, UDante, CIRCSE and Perseus treat it as a conjunction introducing a clause (`mark`). LLCT also often keeps the nominal structure (*pacem* as head, *petendam* as `acl`). Prepositional phrases with a gerund or gerundive in the UD 2.18 data:

  | Structure | CIRCSE | Perseus | PROIEL | ITTB | LLCT | UDante |
  |---|---:|---:|---:|---:|---:|---:|
  | *-nd-* form as head, preposition `case` | 0 | 5 | 262 | 833 | 0 | 0 |
  | *-nd-* form as head, preposition `mark` | 3 | 11 | 0 | 23 | 359 | 68 |
  | noun as head, preposition on the noun | 0 | 3 | 30 | 74 | 233 | 21 |

- **The obligative periphrasis**: see the [Copula](copula.md) page.

## Frequencies

All *-nd-* forms identified by their features: part of speech, features and relation.

--8<-- "gerundium-gerundivum-frequences.en.md"

## Examples

The coloured word is the gerund or gerundive, with its preposition if it has one.

--8<-- "gerundium-gerundivum-exemples.en.md"
