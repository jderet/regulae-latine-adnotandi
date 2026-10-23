# Proposition infinitive

*Dico te errare*, *oportet deum esse*, *sinite paruulos uenire* : un infinitif dont le sujet est à l'accusatif forme une proposition complétive. Elle est l'objet d'un verbe de parole, de pensée ou de volonté, ou le sujet d'un verbe impersonnel. Deux questions se posent : quelle relation relie l'infinitif à son verbe, et de qui dépend l'accusatif ?

## En bref

| Norme | Infinitif → verbe | Accusatif → |
|---|---|---|
| [CIRCSE](../normes/circse.md), [Perseus](../normes/perseus.md), [PROIEL (UD)](../normes/proiel-ud.md), [LLCT](../normes/llct.md), [UDante](../normes/udante.md) | `ccomp` (objet) ; `csubj` quand la proposition est sujet (*necesse est*, *oportet*) | l'infinitif, en `nsubj` (`nsubj:pass` si l'infinitif est passif) |
| [ITTB](../normes/ittb.md) | même règle, mais `csubj` est le cas le plus fréquent, à cause des impersonnels de l'argumentation scolastique (*oportet*, *manifestum est*, *necesse est*) | idem |
| [LDT](../normes/ldt.md) | `OBJ` (`SBJ` quand la proposition est sujet) | l'infinitif, en `SBJ` |
| [PROIEL](../normes/proiel.md) | `comp` | l'infinitif, en `sub` |
| [adnotationes-latinae](../normes/adnotationes.md) | `ccomp`, et `csubj` pour le sujet d'un impersonnel | l'infinitif, en `nsubj` ou `nsubj:pass` |

Toutes les normes font donc de l'accusatif le sujet de l'infinitif, et non l'objet du verbe principal. La proposition infinitive est traitée comme une proposition complète. Ce n'est pas le cas de l'infinitif complément de *possum*, *uolo* ou *incipio*, qui n'a pas de sujet propre (`xcomp` en UD).

### Points de divergence

- **Sujet ou objet** : l'infinitif est `ccomp` ou `csubj` selon la fonction de la proposition. Le partage dépend surtout du genre des textes. `csubj` représente 59 % des cas dans ITTB et 30 % dans UDante, 13 % dans CIRCSE, et 5 % au plus dans Perseus, PROIEL et LLCT.
- **Verbes d'ordre et de permission** (*iubeo*, *sino*, *cogo*, *ueto* + infinitif) : c'est la vraie divergence entre les treebanks. L'accusatif peut être l'objet du verbe principal, qui contrôle le sujet de l'infinitif (`xcomp`). Il peut aussi être le sujet d'une proposition infinitive (`ccomp`). Perseus et PROIEL choisissent surtout `ccomp` (*sinite paruulos uenire* : *paruulos* `nsubj` de *uenire*). CIRCSE, ITTB et LLCT choisissent surtout `xcomp`.

  | | CIRCSE | Perseus | PROIEL | ITTB | LLCT | UDante |
  |---|---:|---:|---:|---:|---:|---:|
  | `xcomp` | 29 | 9 | 33 | 23 | 12 | 4 |
  | `ccomp` | 8 | 45 | 119 | 7 | 4 | 5 |

- **Infinitif racine** (13 % dans Perseus, 8 % dans PROIEL) : il s'agit du discours indirect continu, dont le verbe introducteur est dans une phrase précédente, et de l'infinitif de narration.

## Fréquences

Infinitifs qui ont un sujet à l'accusatif : relation de l'infinitif et relation de l'accusatif.

--8<-- "accusativus-cum-infinitivo-frequences.fr.md"

## Exemples

Les mots en couleur sont l'infinitif et son sujet à l'accusatif.

--8<-- "accusativus-cum-infinitivo-exemples.fr.md"
