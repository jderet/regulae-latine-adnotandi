# Gérondif et adjectif verbal

*ars amandi*, *ad pacem petendam*, *Carthago delenda est* : le gérondif (nom verbal : *amandi*) et l'adjectif verbal en *-ndus* (gérondif adjectival : *petendam*, *delenda*) partagent la même forme. Ils posent trois questions aux normes : faut-il les distinguer dans la morphologie ? Dans *ad pacem petendam*, qui est la tête, le nom ou l'adjectif verbal ? Et la préposition y est-elle `case`, comme devant un nom, ou `mark`, comme devant une proposition ?

## En bref

| Norme | Morphologie | *ad (pacem) petendam* | *delenda est* |
|---|---|---|---|
| [CIRCSE](../normes/circse.md) | `VerbForm=Ger` / `VerbForm=Gdv` (le plus souvent) | forme en *-nd-* tête, préposition `mark` (3 cas seulement) | adjectif verbal tête, *sum* `aux:pass` |
| [PROIEL (UD)](../normes/proiel-ud.md) | `VerbForm=Ger` / `VerbForm=Gdv` | forme en *-nd-* tête, préposition **`case`**, le nom en `nsubj` | adjectif verbal tête, *sum* `cop` |
| [ITTB](../normes/ittb.md) | `VerbForm=Part`, `Aspect=Prosp`, `Voice=Pass` : pas de distinction | forme en *-nd-* tête, préposition **`case`**, le nom en `obj` ou `nsubj:pass` | adjectif verbal tête, *sum* `aux:pass` |
| [LLCT](../normes/llct.md), [UDante](../normes/udante.md) | `VerbForm=Part`, `Aspect=Prosp`, `Voice=Pass` | forme en *-nd-* tête, préposition **`mark`** ; mais dans un quart (UDante) à un tiers (LLCT) des cas, le nom est tête et l'adjectif verbal `acl` | adjectif verbal tête, *sum* `aux:pass` (UDante) |
| [Perseus](../normes/perseus.md) | `VerbForm=Part`, `Aspect=Prosp`, `Voice=Pass` | variable (peu d'exemples) | adjectif verbal tête, *sum* `aux:pass` |
| [LDT](../normes/ldt.md) | mode `d` (gérondif) / `g` (adjectif verbal) dans l'étiquette | la préposition est tête (`AuxP`) ; sous elle, le plus souvent la forme en *-nd-*, parfois le nom avec l'adjectif verbal en `ATR` | *sum* tête, adjectif verbal `PNOM` |
| [PROIEL](../normes/proiel.md) | mode `d` / `g` dans l'étiquette | la préposition est tête ; la forme en *-nd-* en dépend (`obl`) | *sum* tête, adjectif verbal `xobj` |
| [adnotationes-latinae](../normes/adnotationes.md) | comme CIRCSE : `Ger` / `Gdv` ; UPOS VERB, lemme du verbe | non tranché par la norme écrite | adjectif verbal tête, *sum* `aux:pass` |

### Points de divergence

- **La distinction morphologique** existe dans les deux formats d'origine (LDT et PROIEL), et en UD dans CIRCSE et PROIEL. Elle est perdue dans Perseus, ITTB, LLCT et UDante, qui rendent les deux formes comme un participe « prospectif » passif (`Aspect=Prosp`, comme le participe futur, mais avec `Voice=Pass`). Pour y retrouver un gérondif, il faut ajouter le contexte (neutre singulier sans nom accordé).
- **Le groupe prépositionnel** : tous les treebanks UD font le plus souvent de la forme en *-nd-* la tête du groupe. Ils diffèrent par la relation de la préposition. PROIEL et ITTB la traitent comme devant un nom (`case`). LLCT, UDante, CIRCSE et Perseus la traitent comme une conjonction qui introduit une proposition (`mark`). LLCT garde en outre souvent la structure nominale (*pacem* tête, *petendam* `acl`). Groupes prépositionnels avec gérondif ou adjectif verbal, dans les données UD 2.18 :

  | Structure | CIRCSE | Perseus | PROIEL | ITTB | LLCT | UDante |
  |---|---:|---:|---:|---:|---:|---:|
  | forme en *-nd-* tête, préposition `case` | 0 | 5 | 262 | 833 | 0 | 0 |
  | forme en *-nd-* tête, préposition `mark` | 3 | 11 | 0 | 23 | 359 | 68 |
  | nom tête, préposition sur le nom | 0 | 3 | 30 | 74 | 233 | 21 |

- **La périphrase obligative** : voir la fiche [Copule](copula.md).

## Fréquences

Toutes les formes en *-nd-* reconnues par leurs traits : catégorie, traits et relation.

--8<-- "gerundium-gerundivum-frequences.fr.md"

## Exemples

Le mot en couleur est le gérondif ou l'adjectif verbal, avec sa préposition s'il en a une.

--8<-- "gerundium-gerundivum-exemples.fr.md"
