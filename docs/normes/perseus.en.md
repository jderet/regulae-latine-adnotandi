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
