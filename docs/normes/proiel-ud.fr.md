# UD_Latin-PROIEL

| | |
|---|---|
| Producteur | université d'Oslo ; conversion UD par D. Haug |
| Textes | Vulgate (Nouveau Testament presque entier), César (*Guerre des Gaules*, extraits), Cicéron (*Lettres à Atticus*, *De officiis* I), Palladius (*Opus agriculturae*) |
| Taille (UD 2.18) | 18 689 phrases, 205 566 mots |
| Origine | conversion automatique de la version 20180408 du [treebank PROIEL](proiel.md) |
| Licence | CC BY-NC-SA 3.0 |
| Dépôt | <https://github.com/UniversalDependencies/UD_Latin-PROIEL> |

## Caractéristiques

- **Très peu de sous-types** : l'ablatif absolu est un simple `advcl` et la relative un `acl`. Les sous-types `obl:arg` et `obl:agent` existent, mais pas `obl:lmod`, ni les sous-types d'`advmod`.
- **Enclitiques en tokens séparés** : *-que* est un mot à part, sans ligne de plage (*quae que imperasset*), et *neque* est découpé en *ne* + *que*.
- **Gérondif et adjectif verbal** distingués (`VerbForm=Ger`, `VerbForm=Gdv`). Dans la périphrase obligative (*seruandum est*), *sum* est `cop`, et non `aux:pass` comme dans CIRCSE.
- **Lemmes en v**, noms propres en majuscule ; l'XPOS est la catégorie PROIEL à deux lettres (`Nb` nom commun, `Ne` nom propre, `V-` verbe, `Df` adverbe).
- **Ce que la conversion perd** : les nœuds vides de PROIEL (verbe elliptique, coordination asyndétique) disparaissent, et l'ellipse passe par `orphan`. Les arêtes secondaires (sujet partagé, contrôle) ne sont pas reprises dans l'arbre de base.
- MISC donne la référence du passage (`Ref=MARK_6.27`), et `sent_id` est l'identifiant de la phrase dans PROIEL. Les fiches de ce site s'en servent pour montrer l'analyse d'origine.
