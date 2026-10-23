# UD_Latin-LLCT

| | |
|---|---|
| Producteur | T. Korkiakangas (Oslo, Helsinki) pour l'annotation d'origine ; conversion UD par F. M. Cecchini et M. Passarotti (LiLa) |
| Textes | 521 chartes originales écrites en Toscane (Lucques) entre 774 et 897 : le *Late Latin Charter Treebank* 2 |
| Taille (UD 2.18) | 9 023 phrases, 242 411 mots |
| Origine | conversion automatique d'une annotation au format LDT (*Guidelines* de 2007, plus des règles propres aux chartes) |
| Licence | CC BY-SA 4.0 |
| Dépôt | <https://github.com/UniversalDependencies/UD_Latin-LLCT> |

## Caractéristiques

- **Latin non standard** du haut Moyen Âge, avec des graphies, une morphologie et une syntaxe propres : *que* pour *quae*, accusatif après préposition d'ablatif (*de ipsum lignamen*), noms propres germaniques. Le texte est gardé tel quel, et le lemme ramène à la forme classique (*Teopaldo* → *Teutpaldus*).
- **Genre documentaire** : beaucoup de formules (datation, souscriptions), qui pèsent sur les fréquences. La plupart des ablatifs absolus sont des formules de datation (*regnante domno nostro…*) annotées comme racine d'une phrase sans verbe (voir la [fiche](../phaenomena/ablativus-absolutus.md)).
- **Lemmes en u/i**, noms propres en majuscule ; l'XPOS est une étiquette de style LDT à 10 positions séparées par des barres (`v|v|3|s|p|i|p|-|-|-`).
- **Enclitiques** : *-que* est tantôt un mot multi-token, tantôt un mot séparé, comme le scribe l'a écrit.
- 223 phrases de LLCT2 ne sont pas reprises dans la version UD, faute de conversion satisfaisante.

## Références

- Cecchini, F. M., Korkiakangas, T., Passarotti, M. (2020). *A New Latin Treebank for Universal Dependencies: Charters between Ancient Latin and Romance Languages*. LREC 2020.
- Korkiakangas, T. (2021). *Late Latin Charter Treebank: contents and annotation*. *Corpora* 16.
