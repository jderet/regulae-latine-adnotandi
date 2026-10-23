# UD_Latin-PROIEL

| | |
|---|---|
| Producer | University of Oslo; UD conversion by D. Haug |
| Texts | Vulgate (almost the whole New Testament), Caesar (*Gallic War*, excerpts), Cicero (*Letters to Atticus*, *De officiis* I), Palladius (*Opus agriculturae*) |
| Size (UD 2.18) | 18,689 sentences, 205,566 words |
| Origin | automatic conversion of release 20180408 of the [PROIEL treebank](proiel.md) |
| Licence | CC BY-NC-SA 3.0 |
| Repository | <https://github.com/UniversalDependencies/UD_Latin-PROIEL> |

## Characteristics

- **Very few subtypes**: the ablative absolute is a plain `advcl` and the relative clause an `acl`. The subtypes `obl:arg` and `obl:agent` exist, but there is no `obl:lmod` and no subtype of `advmod`.
- **Enclitics are separate tokens**: *-que* is a word of its own, with no range line (*quae que imperasset*), and *neque* is split into *ne* + *que*.
- **Gerund and gerundive are distinguished** (`VerbForm=Ger`, `VerbForm=Gdv`). In the obligative periphrasis (*seruandum est*), *sum* is `cop`, not `aux:pass` as in CIRCSE.
- **Lemmas are spelled with v**, and proper nouns are capitalised. XPOS is the two-letter PROIEL category (`Nb` common noun, `Ne` proper noun, `V-` verb, `Df` adverb).
- **What the conversion loses**: PROIEL's empty nodes (elided verb, asyndetic coordination) disappear, and ellipsis is handled with `orphan`. Secondary edges (shared subject, control) are not carried into the basic tree.
- MISC gives the passage reference (`Ref=MARK_6.27`), and `sent_id` is the sentence identifier in PROIEL. The pages of this site use it to show the original analysis.
