# Ablatif absolu

*Caesare duce*, *urbe capta*, *regnante Hludouuico* : un nom à l'ablatif et un prédicat accordé avec lui forment une proposition circonstancielle sans conjonction. Ce prédicat est le plus souvent un participe, parfois un nom ou un adjectif. Toutes les normes font du prédicat la tête du groupe et du nom son sujet. Elles diffèrent par le nom de la relation qui rattache le groupe au verbe principal.

## En bref

| Norme | Participe → verbe principal | Nom → participe |
|---|---|---|
| [CIRCSE](../normes/circse.md), [Perseus](../normes/perseus.md), [ITTB](../normes/ittb.md), [UDante](../normes/udante.md) | `advcl:abs` | `nsubj:pass` (participe passif) ou `nsubj` (participe actif) |
| [LLCT](../normes/llct.md) | `advcl:abs` ; mais la formule de datation (*regnante domno nostro…*) est la racine d'une phrase sans verbe | idem |
| [PROIEL (UD)](../normes/proiel-ud.md) | `advcl`, sans sous-type : l'ablatif absolu ne se distingue pas des autres participes circonstanciels | idem |
| [LDT](../normes/ldt.md) | `ADV` | `SBJ` |
| [PROIEL](../normes/proiel.md) | `adv` | `sub` |
| [adnotationes-latinae](../normes/adnotationes.md) | `advcl:abs`, comme CIRCSE ; aussi pour un prédicat nominal (*Caesare duce* : *duce* tête) | `nsubj:pass` ou `nsubj` |

Le sous-type `advcl:abs` rend repérable une construction que les formats d'origine ne marquaient que par le cas : dans le LDT comme dans PROIEL, un ablatif absolu est un `ADV` / `adv` comme un autre, et on ne le reconnaît qu'à son sujet à l'ablatif.

### Points de divergence

- **Le choix de `nsubj` ou `nsubj:pass`** dépend de la voix du participe. Les participes passifs (*urbe capta*) dominent dans CIRCSE, Perseus et PROIEL (70 à 80 %). Dans ITTB et UDante, les deux sont à parts égales, car le latin scolastique et médiéval emploie beaucoup de participes présents (*mediante*, *existente*, *manente*).
- **LLCT** : 70 % des ablatifs absolus repérés sont la formule de datation *regnante* (avec le nom du souverain), annotée comme racine de la phrase. Le profil du treebank tient au genre documentaire, non à un désaccord sur l'analyse.
- **Prédicat nominal** (*me consule*, *Caesare duce*) : dans la norme CIRCSE, le nom ou l'adjectif prédicat est tête. Les fréquences ci-dessous ne comptent que les participes.

## Fréquences

Participes à l'ablatif qui ont un sujet à l'ablatif : relation du participe et relation du nom.

--8<-- "ablativus-absolutus-frequences.fr.md"

## Exemples

Les mots en couleur sont le participe et son sujet.

--8<-- "ablativus-absolutus-exemples.fr.md"
