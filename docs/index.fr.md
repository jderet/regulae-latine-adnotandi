# Regulae Latine adnotandi

Ce site compare les **normes d'annotation du latin** : lemmatisation, morphologie et syntaxe en dépendances.
Il en existe aujourd'hui une dizaine. Six treebanks au format Universal Dependencies (UD) ne s'accordent pas toujours entre eux, et les formats dont ils ont été convertis (LDT, PROIEL, Index Thomisticus) suivent des principes différents. Les ressources lexicales (LASLA, LiLa, Collatinus) ont en outre leurs propres conventions de lemmes.

Le site est organisé selon deux axes.

<div class="grid cards" markdown>

- **[Normes](normes/index.md)** : une page par norme, avec son origine, ses textes, son format, sa licence et ses choix caractéristiques.
- **[Phénomènes](phaenomena/index.md)** : une fiche par fait de langue (copule, ablatif absolu, proposition infinitive…), avec un tableau comparatif, les fréquences observées dans chaque treebank et un exemple réel par norme.

</div>

## Les exemples

Les exemples ne sont pas choisis à la main. Un [script](methode.md) parcourt les treebanks à une version figée (UD 2.18) et retient, pour chacun, une phrase courte qui suit **l'analyse la plus fréquente de ce treebank** : on voit ainsi la pratique ordinaire de la norme, et non un cas d'école. Chaque phrase est donnée avec sa source exacte (`sent_id`), sa licence, un arbre et les lignes CoNLL-U.

Pour UD_Latin-Perseus et UD_Latin-PROIEL, la même phrase est aussi montrée **dans son format d'origine** (LDT 2.1, PROIEL XML), ce qui fait voir ce que la conversion vers UD a changé.

## État du site

Sept fiches : [copule](phaenomena/copula.md), [ablatif absolu](phaenomena/ablativus-absolutus.md), [proposition infinitive](phaenomena/accusativus-cum-infinitivo.md), [gérondif et adjectif verbal](phaenomena/gerundium-gerundivum.md), [coordination par -que](phaenomena/coordinatio.md), [proposition sans verbe](phaenomena/sine-verbo.md), [ellipse du verbe](phaenomena/ellipsis.md). Les fiches prévues sont listées sur la page [Phénomènes](phaenomena/index.md). Les corrections et propositions sont bienvenues sous forme d'*issues* ou de *pull requests* sur [GitHub](https://github.com/jderet/regulae-latine-adnotandi).

## Licence

Les textes du site et les exemples sont publiés sous licence [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.fr). C'est la licence compatible avec tous les treebanks cités, dont plusieurs (PROIEL, ITTB, UDante, UD Perseus) interdisent l'usage commercial. Le code est publié sous licence MIT.
