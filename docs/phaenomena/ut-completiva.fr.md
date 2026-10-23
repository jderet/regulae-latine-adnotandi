# Complétive en *ut* et *ne*

*Rogabat eum ut daemonium eiceret*, *decreuit ne quid res publica detrimenti caperet*, *timui ne… descenderet* : après les verbes de demande, d'ordre, d'effort et de crainte, la proposition en *ut* ou *ne* au subjonctif dit ce qui est demandé, ordonné ou craint. Elle tient la place d'un objet, comme l'infinitive après *iubeo* ; mais elle a la forme d'une finale (*ut* + subjonctif), que UD range parmi les circonstancielles. Est-elle `ccomp` ou `advcl` ?

## En bref

| Norme | *rogo ut*, *impero ut*, *timeo ne* | Finale (*uenit ut uideret*) |
|---|---|---|
| UD (règle générale) | `ccomp` : la proposition est un argument du verbe | `advcl` |
| [CIRCSE](../normes/circse.md) | **`advcl`**, comme la finale (`ccomp` presque jamais) | `advcl` |
| [Perseus](../normes/perseus.md) | `advcl` le plus souvent, `ccomp` sinon | `advcl` |
| [PROIEL (UD)](../normes/proiel-ud.md) | **`ccomp`** (83 %) | `advcl` |
| [ITTB](../normes/ittb.md), [UDante](../normes/udante.md) | partagés (peu de cas) | `advcl` |
| [LLCT](../normes/llct.md) | `ccomp` (76 %) | `advcl` |
| [LDT](../normes/ldt.md) | la conjonction (`AuxC`) est tête ; le verbe qui en dépend porte la fonction de la proposition, `OBJ` ou, le plus souvent, `ADV` (*timui ne… descenderet*) | `ADV` |
| [PROIEL](../normes/proiel.md) | la conjonction est tête, en `comp` (complétive), distinct d'`adv` ; le verbe en dépend en `pred` | `adv` |
| [adnotationes-latinae](../normes/adnotationes.md) | **`ccomp`**, comme UD et PROIEL, mais contre CIRCSE | `advcl` |

### Points de divergence

- **CIRCSE contre UD.** Les guides d'UD font de la complétive un `ccomp`, et PROIEL, qui distinguait déjà `comp` d'`adv` dans son format d'origine, s'y tient. CIRCSE met en `advcl` toutes les propositions en *ut* ou *ne* au subjonctif : 75 `advcl` contre 1 `ccomp` dans tout le treebank, quel que soit le verbe. La forme l'emporte sur la fonction.
- **La norme adnotationes-latinae s'écarte ici de CIRCSE.** Elle écrit `ccomp` pour les propositions en *ut* des verbes de demande, d'ordre et de crainte. Le choix est défendable (c'est celui d'UD), mais il fait compter comme erreurs, sur CIRCSE et sur Perseus, des analyses conformes à ces treebanks : 9 écarts sur le *Catilina* de Salluste (*effecerat ut… proderet*, *decreuit… ne quid… caperet*). La question reste ouverte.
- **Perseus.** Dans le LDT, le verbe placé sous la conjonction porte la fonction de toute la proposition : `OBJ` pour une complétive, `ADV` pour une circonstancielle. Les propositions en *ut* y sont surtout `ADV` (sous *ut*, 287 verbes `ADV` contre 28 `OBJ` dans le LDT 2.1), même après un verbe de crainte. La conversion en garde la trace (`advcl` contre `ccomp`).
- **Peu de données.** En dehors de PROIEL (296 cas), les complétives repérées ici sont rares : 9 dans CIRCSE, 28 dans Perseus, moins de 20 dans ITTB, LLCT et UDante. Les pourcentages de ces treebanks sont donc fragiles.

## Fréquences

Chaque verbe au subjonctif qui a pour `mark` *ut*, *uti* ou *ne* et dépend d'un verbe de demande, d'ordre, d'effort ou de crainte : *rogo*, *oro*, *postulo*, *precor*, *obsecro*, *flagito*, *exoro*, *impetro*, *impero*, *praecipio*, *edico*, *decerno*, *statuo*, *moneo*, *admoneo*, *hortor*, *persuadeo*, *suadeo*, *efficio*, *perficio*, *curo*, *caueo*, *permitto*, *timeo*, *metuo*, *uereor*. Le repérage est lexical : une finale qui dépend de l'un de ces verbes est comptée aussi. Analyse : relation de la proposition.

--8<-- "ut-completiva-frequences.fr.md"

## Exemples

Les mots en couleur sont le verbe principal, la conjonction et le verbe de la complétive.

--8<-- "ut-completiva-exemples.fr.md"
