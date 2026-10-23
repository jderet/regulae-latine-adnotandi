# Coordination par *-que*

*Senatus populusque Romanus*, *Lauiniaque uenit litora* : l'enclitique *-que* coordonne en se collant au premier mot du second conjoint. Pour *et*, les treebanks UD s'accordent : le premier conjoint est tête, les suivants sont `conj`, et la conjonction est `cc` sur le conjoint qu'elle introduit. *-que* pose en plus deux questions. Faut-il le séparer de son hôte, et comment ? Faut-il le rattacher à son hôte, ou à la tête du conjoint, qui n'est pas toujours le même mot ?

## En bref

| Norme | Découpage de *-que* | *-que* rattaché à | *neque*, *nec* |
|---|---|---|---|
| [CIRCSE](../normes/circse.md), [ITTB](../normes/ittb.md), [UDante](../normes/udante.md) | mot multi-token (`4-5 uirumque` → `uirum` + `que`) | la tête du conjoint (*Lauiniaque uenit* : *que* → *uenit*) | un seul mot |
| [Perseus](../normes/perseus.md) | mot multi-token | **son hôte**, même quand l'hôte n'est pas la tête du conjoint | découpé (*nec* → *ne* + *c*) |
| [PROIEL (UD)](../normes/proiel-ud.md) | token séparé, sans ligne de plage | la tête du conjoint | découpé (*ne* + *que*) |
| [LLCT](../normes/llct.md) | token séparé, *que* étant souvent écrit à part dans les chartes ; mot multi-token sinon | la tête du conjoint | parfois découpé |
| [LDT](../normes/ldt.md) | mot séparé, écrit `-que` | *-que* est **tête de la coordination** (`COORD`), et les conjoints en dépendent avec le suffixe `_CO` | |
| [PROIEL](../normes/proiel.md) | mot séparé | *que* est **tête de la coordination**, et les conjoints portent la relation du groupe | découpé |
| [adnotationes-latinae](../normes/adnotationes.md) | mot multi-token | la tête du conjoint, comme CIRCSE | un seul mot |

Les formats d'origine font de la conjonction la tête de la coordination. UD en fait un dépendant du conjoint qui suit. La conversion doit donc choisir à quel mot du second conjoint rattacher *-que*. La règle UD est de rattacher la conjonction à la tête du conjoint.

### Points de divergence

- **Hôte ou tête du conjoint.** Dans *Confremuere omnes studiisque ardentibus ausum talia deposcunt* (Perseus), le second conjoint est *studiis … deposcunt*, dont la tête est *deposcunt*. Perseus rattache pourtant *que* à *studiis*, son hôte, et la coordination ne se lit plus que par la relation `conj` de *deposcunt*. Part des *-que* rattachés à un hôte qui n'est pas la tête de son conjoint :

  | CIRCSE | Perseus | PROIEL | ITTB | LLCT | UDante |
  |---:|---:|---:|---:|---:|---:|
  | 3 % | 65 % | 2 % | 0 % | 0 % | 7 % |

- **Découpage.** C'est une différence de tokenisation, non de syntaxe. Elle compte toutefois pour l'évaluation : un analyseur entraîné sur PROIEL produit un token *que* là où le texte de référence de CIRCSE attend un mot multi-token.
- ***neque* découpé.** PROIEL coupe *neque* en *ne* + *que* (754 cas), et Perseus *nec* en *ne* + *c* (100 cas). CIRCSE, ITTB et UDante gardent un seul mot (CCONJ). Ces cas sont exclus des fréquences ci-dessous.

## Fréquences

Chaque *-que* en `cc` (hors *neque*) : découpage (MWT : mot multi-token ; token : mot séparé), puis mot de rattachement (hôte ou autre mot) et relation de ce mot.

--8<-- "coordinatio-frequences.fr.md"

## Exemples

Les mots en couleur sont *que*, le mot auquel il est rattaché et, s'il est différent, son hôte.

--8<-- "coordinatio-exemples.fr.md"
