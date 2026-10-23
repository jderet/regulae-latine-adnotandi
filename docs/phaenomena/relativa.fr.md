# Proposition relative

*Verbi quod dixerat ei Iesus*, *quae mente agitaui, audistis*, *qui bene amat, bene castigat* : la relative dépend d'ordinaire d'un antécédent, mais le latin l'emploie aussi sans antécédent, à la place d'un nom (sujet, objet, complément), et en tête de phrase pour relier deux phrases (*quae cum ita sint*, relatif de liaison). UD rattache la relative à son antécédent en `acl:relcl`. Sans antécédent, faut-il garder `acl:relcl`, prendre la relation du nom absent, ou les deux ?

## En bref

| Norme | Relative à antécédent | Relative sans antécédent (*quae agitaui, audistis*) | Relatif de liaison |
|---|---|---|---|
| UD (règle générale) | `acl:relcl` sur l'antécédent | la relation du nom absent ; sous-type `:relcl` permis | racine de sa phrase |
| [CIRCSE](../normes/circse.md) | `acl:relcl` | relation du nom absent **avec le sous-type `:relcl`** (`csubj:relcl`, `ccomp:relcl`, `advcl:relcl`) | racine |
| [Perseus](../normes/perseus.md) | `acl:relcl` | **`acl:relcl` sur le verbe principal**, ou relation simple (`csubj`, `advcl`) ; jamais de sous-type `:relcl` ailleurs qu'`acl` | racine |
| [PROIEL (UD)](../normes/proiel-ud.md) | **`acl`**, sans sous-type | relation simple (`nsubj`, `obj`, `advcl`…) | racine |
| [ITTB](../normes/ittb.md), [UDante](../normes/udante.md) | `acl:relcl` | relation avec `:relcl`, comme CIRCSE | racine |
| [LLCT](../normes/llct.md) | `acl:relcl` | relation avec `:relcl`, surtout `ccomp:relcl` | racine |
| [LDT](../normes/ldt.md) | verbe de la relative `ATR` de l'antécédent | verbe de la relative avec la fonction du nom absent (`OBJ`, `SBJ`) | `PRED` |
| [PROIEL](../normes/proiel.md) | verbe de la relative `atr` de l'antécédent | fonction du nom absent | `pred` |
| [adnotationes-latinae](../normes/adnotationes.md) | `acl:relcl` | comme CIRCSE : relation du nom absent avec `:relcl` (décision 30) | racine |

Dans tous les cas, le relatif garde sa fonction dans la relative (*quae* `obj` de *agitaui*) ; seule varie la relation qui rattache la relative au reste de la phrase.

### Points de divergence

- **Sous-type `:relcl` hors d'`acl`.** CIRCSE, ITTB, UDante et LLCT marquent la relative sans antécédent par sa fonction et le sous-type `:relcl` : 156 cas dans CIRCSE, 2 579 dans ITTB. Perseus n'emploie que `acl:relcl` (288) : la relative sans antécédent y est tantôt `acl:relcl` rattachée au verbe principal (*quae mente agitaui* → *audistis*), tantôt une relation simple (`csubj`, 10 % des relatives). Dans le LDT, le verbe d'une telle relative portait la fonction du nom absent (`OBJ`) ; la conversion la transforme en `acl:relcl`.
- **`acl` ou `acl:relcl`.** PROIEL n'a aucun sous-type `:relcl` : la relative y est `acl`, comme un participe épithète, et la relative sans antécédent prend la relation simple du nom absent (`nsubj`, `obj`, `advcl`). Pour retrouver les relatives dans PROIEL, il faut passer par le pronom relatif.
- **Relatif de liaison.** *Quae cum ita sint*, *quibus rebus cognitis* : le relatif reprend la phrase précédente, et sa proposition est principale. Tous les treebanks font de sa proposition la racine de la phrase. C'est le cas de 3 à 11 % des relatifs : 11 % dans PROIEL, ITTB et UDante, 5 % dans CIRCSE, 3 % dans les chartes de LLCT.
- **Relative ou interrogative indirecte.** *Memorare possum, quibus in locis… fuderit* : *quibus* est ici un interrogatif, et la proposition est l'objet de *memorare* (`ccomp`), non une relative. UD Perseus l'analyse parfois en relative (`acl:relcl`), et lemmatise sous *quis* quelques relatifs de liaison.

## Fréquences

Chaque relatif (*qui*, *quicumque*, `PronType=Rel`), avec le prédicat de sa proposition (le premier verbe, ou mot qui porte une copule, au-dessus de lui) : relation de ce prédicat et catégorie de sa tête (nom au sens large : relative à antécédent ; verbe : le plus souvent relative sans antécédent). Les relatives coordonnées (`conj`) sont laissées de côté.

--8<-- "relativa-frequences.fr.md"

## Exemples

Les mots en couleur sont le relatif et le prédicat de sa proposition. Le dernier exemple, tiré du *Catilina* de Salluste, montre une relative sans antécédent rattachée en `acl:relcl` au verbe principal dans Perseus.

--8<-- "relativa-exemples.fr.md"
