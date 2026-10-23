# Participe

*Possidens paelex domum*, *terribilem picea tectus caligine uultum*, *comminatus eiecit* : le participe s'accorde avec un nom, exprimé ou non, et décrit en même temps une circonstance de l'action. Est-il le dépendant du nom (épithète, `acl`) ou du verbe (apposé, prédicatif, `advcl`) ? Les treebanks latins répondent de façons très différentes, et ce point pèse lourd dans les scores : le participe est fréquent, et chaque désaccord est une erreur de tête.

## En bref

| Norme | Participe accordé à un nom exprimé | Participe sans nom exprimé (*laetus uenit*) | Participe substantivé |
|---|---|---|---|
| [CIRCSE](../normes/circse.md) | **`acl` sur le nom**, même en hyperbate | `advcl:pred` sur le verbe | selon sa fonction (`obj`, `nsubj`…) |
| [Perseus](../normes/perseus.md) | **`amod` ou `nmod`** sur le nom, ou `advcl` sur le verbe, selon l'analyse du LDT (`ATR` ou `ADV`) | `advcl` | selon sa fonction |
| [PROIEL (UD)](../normes/proiel-ud.md) | **`advcl` sur le verbe** le plus souvent ; `acl` sur le nom quand il est épithète | `advcl` | selon sa fonction |
| [ITTB](../normes/ittb.md), [LLCT](../normes/llct.md) | `acl` sur le nom | `advcl` | selon sa fonction, souvent `obl` dans ITTB |
| [UDante](../normes/udante.md) | `acl` sur le nom | `advcl:pred` | selon sa fonction |
| [LDT](../normes/ldt.md) | `ATR` (épithète) ou `ADV` (circonstant), parfois `ATV` / `AtvV` (prédicatif) | `ADV` | selon sa fonction |
| [PROIEL](../normes/proiel.md) | `xadv` sur le verbe, avec une arête secondaire `xsub` vers le nom ; `atr` pour l'épithète | `xadv` | selon sa fonction |
| [adnotationes-latinae](../normes/adnotationes.md) | `acl` sur le nom, même en hyperbate (comme CIRCSE) | `advcl:pred` (décision 25) | selon sa fonction |

`amod` est réservé aux adjectifs dans CIRCSE et dans la norme adnotationes-latinae : un participe épithète y est `acl`. Perseus, qui hérite de la relation unique `ATR` du LDT, le met en `amod` ou en `nmod`.

### Points de divergence

- **Nom ou verbe.** Le participe apposé, qui décrit le sujet au moment de l'action (*tectus caligine uultum*), dépend du nom dans CIRCSE (`acl`, 61 % des participes) et du verbe dans PROIEL (`advcl`, 69 %). Ce choix vient des formats d'origine. PROIEL a une relation propre au prédicatif, `xadv`, rattachée au verbe avec une arête secondaire vers le nom (2 907 participes dans le treebank d'origine) ; la conversion en fait `advcl`. Le LDT hésite entre `ATR` (1 222 participes dans le LDT 2.1) et `ADV` (1 134) ; Perseus en hérite le partage entre `amod` ou `nmod` d'un côté, `advcl` de l'autre.
- **`advcl:pred`.** CIRCSE réserve ce sous-type au participe dont le nom n'est pas exprimé (*laetus uenit*, *sedens digerit*). Il l'emploie pour 22 % de ses participes, et rarement pour un participe accordé à un nom exprimé.
- **`nmod` pour un épithète.** Perseus met en `nmod` 24 % de ses participes, presque autant qu'en `amod` (23 %). Ce ne sont pas, pour l'essentiel, des participes substantivés compléments d'un nom (*oculi sequentum*), mais des épithètes accordés à leur nom : *antro aperto*, *ora indignantia*, *tela fabricata*. Les deux relations rendent le même `ATR` du LDT.
- **Catégorie.** Presque tous les participes sont VERB, dans Perseus comme dans CIRCSE (Perseus : 1 277 sur 1 298 ; CIRCSE : 1 331 sur 1 363). La norme adnotationes-latinae met en ADJ, sous leur propre lemme, les participes lexicalisés qui ont un article dans le Lewis & Short (*doctus*, *notus*, *perditus*, *tacitus*), ce que ni CIRCSE ni Perseus ne font.

## Fréquences

Chaque participe (`VerbForm=Part`), hors adjectif verbal et gérondif, hors périphrases (participe avec `aux` ou `cop`), hors ablatif absolu (`advcl:abs`), racine et conjoint. Analyse : relation du participe, et catégorie de sa tête (nom au sens large, ou verbe).

--8<-- "participium-frequences.fr.md"

## Exemples

Les mots en couleur sont le participe et sa tête. Le dernier exemple, tiré des *Catilinaires*, montre un participe en `amod` dans Perseus, là où CIRCSE mettrait `acl`.

--8<-- "participium-exemples.fr.md"
