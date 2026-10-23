# Relative clauses

*Verbi quod dixerat ei Iesus*, *quae mente agitaui, audistis*, *qui bene amat, bene castigat*: a relative clause usually depends on an antecedent, but Latin also uses it without one, in place of a noun (subject, object, complement), and at the head of a sentence to link it to the previous one (*quae cum ita sint*, the connecting relative). UD attaches the relative clause to its antecedent as `acl:relcl`. Without an antecedent, should it keep `acl:relcl`, take the relation of the missing noun, or both?

## At a glance

| Standard | Relative with an antecedent | Free relative (*quae agitaui, audistis*) | Connecting relative |
|---|---|---|---|
| UD (general rule) | `acl:relcl` on the antecedent | the relation of the missing noun; `:relcl` subtype allowed | root of its sentence |
| [CIRCSE](../normes/circse.md) | `acl:relcl` | relation of the missing noun **with the `:relcl` subtype** (`csubj:relcl`, `ccomp:relcl`, `advcl:relcl`) | root |
| [Perseus](../normes/perseus.md) | `acl:relcl` | **`acl:relcl` on the main verb**, or a plain relation (`csubj`, `advcl`); never a `:relcl` subtype other than on `acl` | root |
| [PROIEL (UD)](../normes/proiel-ud.md) | **`acl`**, no subtype | plain relation (`nsubj`, `obj`, `advcl`…) | root |
| [ITTB](../normes/ittb.md), [UDante](../normes/udante.md) | `acl:relcl` | relation with `:relcl`, as in CIRCSE | root |
| [LLCT](../normes/llct.md) | `acl:relcl` | relation with `:relcl`, mostly `ccomp:relcl` | root |
| [LDT](../normes/ldt.md) | verb of the relative `ATR` of the antecedent | verb of the relative with the function of the missing noun (`OBJ`, `SBJ`) | `PRED` |
| [PROIEL](../normes/proiel.md) | verb of the relative `atr` of the antecedent | function of the missing noun | `pred` |
| [adnotationes-latinae](../normes/adnotationes.md) | `acl:relcl` | as in CIRCSE: relation of the missing noun with `:relcl` (decision 30) | root |

In every case the relative pronoun keeps its function inside the clause (*quae* `obj` of *agitaui*); only the relation linking the clause to the rest of the sentence varies.

### Points of divergence

- **`:relcl` subtype outside `acl`.** CIRCSE, ITTB, UDante and LLCT mark a free relative by its function plus the `:relcl` subtype: 156 cases in CIRCSE, 2,579 in ITTB. Perseus only uses `acl:relcl` (288): a free relative there is either `acl:relcl` attached to the main verb (*quae mente agitaui* → *audistis*), or a plain relation (`csubj`, 10% of relatives). In the LDT, the verb of such a clause bore the function of the missing noun (`OBJ`); the conversion turns it into `acl:relcl`.
- **`acl` or `acl:relcl`.** PROIEL has no `:relcl` subtype at all: a relative clause is `acl`, like an attributive participle, and a free relative takes the plain relation of the missing noun (`nsubj`, `obj`, `advcl`). To find relative clauses in PROIEL, one has to go through the relative pronoun.
- **Connecting relative.** *Quae cum ita sint*, *quibus rebus cognitis*: the relative picks up the previous sentence, and its clause is a main clause. All treebanks make it the root of the sentence. This covers 3 to 11% of relatives: 11% in PROIEL, ITTB and UDante, 5% in CIRCSE, 3% in the LLCT charters.
- **Relative or indirect question.** *Memorare possum, quibus in locis… fuderit*: *quibus* is an interrogative here, and the clause is the object of *memorare* (`ccomp`), not a relative. UD Perseus sometimes analyses such clauses as relatives (`acl:relcl`), and lemmatises a few connecting relatives under *quis*.

## Frequencies

Each relative word (*qui*, *quicumque*, `PronType=Rel`), with the predicate of its clause (the first verb, or word carrying a copula, above it): relation of that predicate and part of speech of its head (a noun in the broad sense: relative with an antecedent; a verb: most often a free relative). Coordinated relatives (`conj`) are left out.

--8<-- "relativa-frequences.en.md"

## Examples

The highlighted words are the relative word and the predicate of its clause. The last example, from Sallust's *Catiline*, shows a free relative attached as `acl:relcl` to the main verb in Perseus.

--8<-- "relativa-exemples.en.md"
