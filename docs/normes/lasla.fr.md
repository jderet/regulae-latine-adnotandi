# LASLA

| | |
|---|---|
| Producteur | Laboratoire d'Analyse Statistique des Langues Anciennes, université de Liège, fondé en 1961 |
| Contenu | corpus *Opera Latina* : textes latins classiques lemmatisés et analysés morphologiquement, de façon semi-automatique, avec vérification manuelle complète |
| Accès | consultation en ligne ; les textes sont diffusés par accords de partage de données ; les liens vers LiLa sont publiés par CIRCSE (<https://github.com/CIRCSE/LASLA>) |
| Site | <http://web.philo.ulg.ac.be/lasla/> |

## Principes

- **Pas de syntaxe** : le LASLA annote les lemmes et la morphologie, pas les dépendances.
- **Lemmes avec indice d'homonyme** : chaque lemme est accompagné d'un indice qui sépare les homonymes. Il reparaît en MISC dans [UD_Latin-CIRCSE](circse.md) (`LASLAVariant=2`).
- **Code de catégorie et de flexion** : une lettre pour la catégorie et un chiffre pour la classe flexionnelle (`A3` : nom de la 3e déclinaison, `B2` : verbe de la 2e conjugaison, `C1` : adjectif de la 1re classe, `M` : adverbe). CIRCSE le reprend comme XPOS.
- **Texte édité** : les textes suivent les éditions critiques disponibles au moment de la lemmatisation, avec les choix éditoriaux propres des annotateurs.

Le LASLA est la source des lemmes et de la morphologie de [CIRCSE](circse.md), et il a fourni les données des premières campagnes [EvaLatin](evalatin.md).
