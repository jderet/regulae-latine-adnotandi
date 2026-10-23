# Adjectif et participe substantivés

*Omnia haec mala* « tous ces maux », *uidit ferum* « il vit la bête », *iussa perferre* « porter les ordres », *coniugis, nati, patris* « du fils » : un adjectif ou un participe employé seul tient lieu de nom. Le dictionnaire en donne souvent un article propre (*malum*, *fera*, *iussum*, *natus*), parfois un simple renvoi (*mălum, i, v. malus*). Faut-il l'annoter comme un nom, sous ce lemme, ou comme l'adjectif ou le verbe dont il vient ?

## En bref

| Norme | Catégorie | Lemme |
|---|---|---|
| [CIRCSE](../normes/circse.md) | **NOUN** (94 %) | **le nom** : *malum*, *fera*, *natus*, *superi* |
| [Perseus](../normes/perseus.md) | ADJ ou VERB le plus souvent, NOUN parfois | l'adjectif ou le verbe : *malus*, *ferus*, *iubeo*, *nascor* ; mais *omnia*, *omnes* en NOUN sous leur propre lemme |
| [PROIEL (UD)](../normes/proiel-ud.md) | ADJ ou VERB le plus souvent (67 %) | l'adjectif ou le verbe, sauf noms bien établis (*mandatum*) |
| [ITTB](../normes/ittb.md) | **NOUN** (86 %) | le nom : *bonum*, *malum* |
| [LLCT](../normes/llct.md) | NOUN (82 %) | le nom : *mandatum*, *debitum* |
| [UDante](../normes/udante.md) | partagé : NOUN (52 %), ADJ (38 %) | partagé |
| [LDT](../normes/ldt.md) | catégorie de l'adjectif (`a`) ou du participe (`v`) | l'adjectif ou le verbe |
| [PROIEL](../normes/proiel.md) | `A-` ou `V-` ; `Nb` pour les noms établis | l'adjectif ou le verbe |
| [adnotationes-latinae](../normes/adnotationes.md) | NOUN si le Lewis & Short a un article de nom, renvoi compris ; ADJ sinon (décision 11) | le nom du dictionnaire |

### Points de divergence

- **Le dictionnaire ou la forme.** CIRCSE, ITTB et LLCT suivent le dictionnaire : un mot qui a un article de nom est NOUN sous ce lemme, même quand l'article n'est qu'un renvoi (*mălum, i, v. malus*). Perseus et PROIEL suivent la forme : *mala* « les maux » reste ADJ sous *malus*, *iussa* reste VERB sous *iubeo*. Le lemme *malum* NOUN apparaît 6 fois dans Perseus, 70 fois dans CIRCSE, qui n'a que 10 *malus* ADJ.
- **Perseus n'est pas constant.** Il met en NOUN sous un lemme propre certains pluriels (*omnia*, *omnes*, *multa*, *pauca*), mais laisse en ADJ *mali*, *ferae* ou *bonum*. Le relevé sur Salluste avait montré le même flottement (*mortalis* ADJ 9 fois, NOUN 1 fois).
- **Participes substantivés.** *iussum*, *monitum*, *mandatum*, *debitum*, *natus* « fils » : VERB sous le verbe dans Perseus et PROIEL, avec une relation de nom (`obj`, `nmod`) ; NOUN sous le nom dans CIRCSE, LLCT et dans la norme adnotationes-latinae quand le Lewis & Short en a l'article.
- **Conséquence pour l'évaluation.** Entre une norme qui suit le dictionnaire et un treebank qui suit la forme, chaque substantivé compte deux erreurs, de catégorie et de lemme : 31 de chaque sur le jeu de contrôle en poésie d'adnotationes-latinae (Properce, Phèdre, Ovide, Virgile).

## Fréquences

Chaque mot de la liste suivante employé comme nom (sujet, objet, oblique, `nmod`, `conj`, `appos` ou vocatif ; pas `amod` ni `det`), sous le lemme du nom ou sous celui du mot d'origine, quand sa forme convient au nom : *malum* (*malus*), *bonum* (*bonus*), *fera* (*ferus*), *superi* (*superus*), *planum* (*planus*), *cauum* (*cauus*), *penetrale* (*penetralis*), *natus* (*nascor*), *monitum* (*moneo*), *iussum* (*iubeo*), *mandatum* (*mando*), *debitum* (*debeo*). Analyse : catégorie, et lemme propre (le nom) ou lemme d'origine.

--8<-- "substantiuum-frequences.fr.md"

## Exemples

Le mot en couleur est l'adjectif ou le participe substantivé.

--8<-- "substantiuum-exemples.fr.md"
