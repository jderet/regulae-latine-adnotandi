# Regulae Latine adnotandi

Un wiki comparatif des normes d'annotation du latin (lemmatisation, morphologie, syntaxe en dépendances), avec des exemples tirés des treebanks.
*A comparative wiki of Latin annotation standards, with examples drawn from the treebanks.*

Site : <https://julesderet.fr/regulae-latine-adnotandi/> (français et anglais)

## Contenu

- `docs/` : les pages du site, en français (`*.fr.md`) et en anglais (`*.en.md`) ;
  - `docs/normes/` : une page par norme (treebanks UD, formats LDT, PROIEL et IT-TB, LASLA, LiLa, Collatinus, EvaLatin, adnotationes-latinae) ;
  - `docs/phaenomena/` : une fiche par phénomène, qui compare les normes ;
- `scripts/telecharger.sh` : télécharge les treebanks à des versions figées (UD 2.18, LDT 2.1, PROIEL) dans `.cache/` ;
- `scripts/exemples.py` : compte les analyses de chaque phénomène, choisit les exemples, dessine les arbres en SVG et écrit les fragments de `generes/`, inclus dans les fiches ;
- `generes/` : fragments produits par le script, versionnés.

## Construire

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./scripts/telecharger.sh            # seulement pour régénérer les exemples
.venv/bin/python scripts/exemples.py
.venv/bin/mkdocs serve
```

Le site est publié sur GitHub Pages par `.github/workflows/pages.yml` à chaque push sur `main`.

## Ajouter une fiche

1. Écrire dans `scripts/exemples.py` la fonction qui repère le phénomène dans une phrase UD et donne son analyse, puis l'ajouter à `PHENOMENES`.
2. Lancer le script.
3. Écrire `docs/phaenomena/<nom>.fr.md` et `.en.md` sur le modèle des fiches existantes, en incluant les fragments `--8<-- "<nom>-frequences.<langue>.md"` et `--8<-- "<nom>-exemples.<langue>.md"`.
4. Ajouter la fiche à `nav` dans `mkdocs.yml`.

## Licence

Textes et exemples : [CC BY-NC-SA 4.0](LICENSE). C'est la licence compatible avec tous les treebanks cités, dont PROIEL, ITTB, UDante et UD Perseus, qui sont sous clause non commerciale.
Code (`scripts/`, configuration) : [MIT](LICENSE-CODE).

Les exemples restent soumis à la licence de leur treebank d'origine, indiquée sous chacun d'eux.
