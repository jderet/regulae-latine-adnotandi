# Collatinus

| | |
|---|---|
| Auteurs | Yves Ouvrard et Philippe Verkerk |
| Nature | lemmatiseur et analyseur morphologique du latin, avec scansion ; logiciel libre et service en ligne |
| Licence | GPL 3 (logiciel) |
| Sources | <https://github.com/biblissima/collatinus> ; en ligne : <https://outils.biblissima.fr/fr/collatinus-web/> |

## Principes

- **Analyse hors contexte** : pour une forme, Collatinus donne tous les lemmes possibles, chacun avec toutes ses analyses morphologiques. Il ne choisit pas : c'est l'utilisateur, ou un outil en aval, qui tranche en contexte.
- **Lexique avec quantités** : les lemmes et les formes portent les quantités vocaliques, ce qui sert à la scansion.
- **Lemmes de dictionnaire** : le lexique est construit sur les grands dictionnaires (Gaffiot, Lewis & Short, Georges…), dont les traductions sont affichées avec l'analyse.
- **Pas de syntaxe**.

Collatinus n'est pas une norme d'annotation au sens d'un treebank, mais un repère de lemmatisation très utilisé, notamment dans l'enseignement. Le projet [adnotationes-latinae](adnotationes.md) s'en sert comme aide : les lemmes qu'il admet pour chaque forme sont proposés au modèle.
