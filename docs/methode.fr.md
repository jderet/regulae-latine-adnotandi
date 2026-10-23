# Méthode

## Données

Les exemples et les chiffres viennent de données téléchargées à des versions figées par `scripts/telecharger.sh` :

| Données | Version | Source |
|---|---|---|
| Six treebanks UD latins | UD 2.18 (étiquette `r2.18` de chaque dépôt) | <https://github.com/UniversalDependencies> |
| Latin Dependency Treebank | 2.1, commit `bf4334f` | <https://github.com/PerseusDL/treebank_data> |
| PROIEL (latin) | commit `8e38896` | <https://github.com/proiel/proiel-treebank> |

## Fréquences

Pour chaque phénomène, une fonction du script `scripts/exemples.py` repère ses occurrences dans chaque phrase UD à partir des traits et des relations. Elle donne pour chacune une **analyse**, écrite en notation UD (`part. : advcl:abs · nom : nsubj:pass`). Le tableau des fréquences compte ces analyses. Les critères de repérage sont donnés en tête de chaque tableau. Ils sont volontairement simples, et donc imparfaits : un ablatif absolu dont le sujet n'est pas à l'ablatif, par exemple, n'est pas compté.

## Choix des exemples

Pour chaque treebank, l'exemple est tiré parmi les phrases qui suivent **l'analyse la plus fréquente de ce treebank**. Parmi elles, le script préfère :

1. une phrase de 6 à 14 mots (ponctuation non comprise) ;
2. hors formules de chartes (LLCT) ;
3. où le phénomène se présente sous sa forme la plus typique (par exemple, pour la copule, un attribut adjectif avec un sujet exprimé) ;
4. la plus proche de 9 mots ; à égalité, la première dans l'ordre des identifiants.

Le choix est donc déterministe : relancer le script donne les mêmes exemples. Pour Perseus et PROIEL, seule une phrase présente dans le format d'origine peut être retenue, et son analyse d'origine est affichée en dessous.

Les traductions des phrases retenues sont faites à la main et rangées dans `scripts/traductions.tsv` (treebank, `sent_id`, français, anglais). Si un exemple change, sa traduction manque jusqu'à ce qu'on l'ajoute.

## Arbres

Les arbres sont dessinés par le script en SVG, sans bibliothèque extérieure. Les arcs vont de la tête au dépendant, avec la relation au sommet. Sous chaque mot figure sa catégorie : UPOS pour UD, étiquette `postag` pour le LDT, catégorie à deux lettres pour PROIEL. Les nœuds vides de PROIEL (∅V, ∅C) sont placés en fin de phrase, et ses arêtes secondaires sont dessinées en pointillés sous la ligne.

## Reproduire

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./scripts/telecharger.sh
.venv/bin/python scripts/exemples.py
.venv/bin/mkdocs serve
```

Les fragments produits (`generes/`) sont versionnés, ce qui permet de construire le site sans retélécharger les treebanks.
