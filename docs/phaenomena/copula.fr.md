# Copule : *sum*

*Gallia est omnis diuisa*, *uita breuis est*, *Caesar consul erat* : le verbe *sum* relie un sujet à un attribut (adjectif, nom, pronom, groupe prépositionnel, adverbe). Il sert aussi d'auxiliaire (*amatus est*, *delenda est*) et peut avoir un sens plein (*est deus*, « Dieu existe »). La question est de savoir qui est la tête de la proposition copulative : le verbe ou l'attribut.

## En bref

| Norme | Tête de *Caesar consul erat* | *sum* | Attribut | Périphrase *delenda est* |
|---|---|---|---|---|
| UD (tous les treebanks) | l'attribut *consul* | `cop` | tête (porte `nsubj`) | voir ci-dessous |
| [CIRCSE](../normes/circse.md), [Perseus](../normes/perseus.md), [ITTB](../normes/ittb.md), [UDante](../normes/udante.md) | attribut | `cop` | tête | adjectif verbal tête, *sum* `aux:pass` |
| [PROIEL (UD)](../normes/proiel-ud.md) | attribut | `cop` | tête | adjectif verbal tête, *sum* **`cop`** |
| [LDT](../normes/ldt.md), [IT-TB](../normes/it-tb.md) | ***sum*** (`PRED`) | tête | `PNOM` | *sum* tête, adjectif verbal `PNOM` (mesuré dans le LDT 2.1) |
| [PROIEL](../normes/proiel.md) | ***sum*** (`pred`) | tête | `xobj`, avec une arête secondaire `xsub` vers le sujet | *sum* tête, adjectif verbal `xobj` |
| [adnotationes-latinae](../normes/adnotationes.md) | attribut | `cop` | tête | adjectif verbal tête, *sum* `aux:pass` |

UD renverse donc l'analyse des formats d'origine : là où le LDT et PROIEL font de *sum* le prédicat, UD le traite comme un mot grammatical qui dépend de l'attribut. Ce choix, commun à toutes les langues UD, aligne le latin sur les langues sans copule exprimée (*omnia praeclara rara*) : la proposition sans *sum* a la même tête que la proposition copulative. Voir la fiche [Proposition sans verbe](sine-verbo.md).

### Ce qui varie entre les treebanks UD

- **Seul *sum* est copule.** Les verbes d'état (*fio*, *uideor*, *maneo*, *appellor*) sont des verbes pleins, et leur attribut est `xcomp`. Aucun treebank n'emploie `cop` pour un autre verbe que *sum*.
- **Périphrase obligative** (*delenda est*, *seruandum est*) : *sum* est `aux:pass` partout, sauf dans PROIEL, où il reste `cop`. LLCT n'en a presque pas d'occurrences.
- **Auxiliaire `aux`** : PROIEL le donne au parfait des déponents (*polliciti sunt*) et au participe futur (*facturus est*) ; ITTB et LLCT surtout à la périphrase *sum* + participe présent du latin tardif et médiéval (*est habens*).
- ***sum* tête** : quand rien ne peut être attribut (*est deus*, *sunt qui dicant*), *sum* est la tête de sa proposition. C'est le cas de 10 à 20 % des occurrences dans PROIEL, ITTB et LLCT, beaucoup moins dans CIRCSE et Perseus.

## Fréquences

Analyse de chaque occurrence du lemme *sum* : relation de *sum*, ou « tête » quand il gouverne sa proposition.

--8<-- "copula-frequences.fr.md"

## Exemples

Les mots en couleur sont *sum* et sa tête.

--8<-- "copula-exemples.fr.md"
