# LiLa : Linking Latin

| | |
|---|---|
| Producteur | projet ERC *LiLa: Linking Latin* (n° 769994), CIRCSE, Università Cattolica del Sacro Cuore, Milan (M. Passarotti) |
| Contenu | une base de connaissances en données liées (RDF) qui relie corpus, treebanks et lexiques latins par leurs lemmes |
| Pièce centrale | la *Lemma Bank* : un inventaire de lemmes, chacun avec sa catégorie, sa classe flexionnelle et ses graphies |
| Licence | Lemma Bank : CC BY-SA 4.0 |
| Site | <https://lila-erc.eu> ; données : <https://github.com/CIRCSE/LiLa_Lemma-Bank> |

## Principes

- **Un lemme, plusieurs graphies** : chaque lemme de la *Lemma Bank* a une forme canonique et des représentations écrites alternatives (*tempto* / *tento*). Une ressource se relie à LiLa par l'identifiant du lemme, quelle que soit sa propre graphie.
- **Catégorie et classe flexionnelle** : la classe (`n3` : 3e déclinaison, `v2` : 2e conjugaison) est celle que [CIRCSE](circse.md) donne en MISC (`LiLaflcat`) et que les treebanks UD milanais rendent par le trait `InflClass` (`IndEurX`, `LatE`…).
- **Homonymes** : deux lemmes de même graphie mais de catégorie ou de flexion différentes ont deux identifiants (*appello* de la 1re et de la 3e conjugaison).
- Les treebanks [ITTB](ittb.md), [UDante](udante.md) et [CIRCSE](circse.md), le corpus du [LASLA](lasla.md) et plusieurs dictionnaires (dont le Lewis & Short) sont reliés à LiLa.
