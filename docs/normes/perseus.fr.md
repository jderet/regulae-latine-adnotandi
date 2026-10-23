# UD_Latin-Perseus

| | |
|---|---|
| Producteur | Perseus Project (Tufts) et université de Leipzig ; conversion UD par G. Celano |
| Textes | extraits d'Auguste (*Res gestae*), Cicéron (*Catilinaires*), Virgile (*Énéide* VI), Ovide (*Métamorphoses* I), Pétrone, Phèdre, Properce, Salluste (*Catilina*), Suétone (*Auguste*), Tacite (*Histoires*), de la Vulgate |
| Taille (UD 2.18) | 2 273 phrases, 29 223 mots |
| Origine | conversion automatique du [Latin Dependency Treebank 2.1](ldt.md) |
| Licence | CC BY-NC-SA 2.5 (le LDT 2.1 est sous CC BY-SA 3.0) |
| Dépôt | <https://github.com/UniversalDependencies/UD_Latin-Perseus> |

## Caractéristiques

- **Héritier du LDT** : l'XPOS est l'étiquette LDT à 9 positions (`v3spia---`), et MISC garde l'identifiant de lemme LDT avec son numéro d'homonyme (`LId=mando1`). Chaque `sent_id` donne le fichier et le numéro de phrase du LDT (`phi0690.phi003.perseus-lat1.tb.xml@43`). On retrouve ainsi l'analyse d'origine, comme le font les fiches de ce site.
- **Lemmes en v**, noms propres en majuscule.
- **Moins de sous-types** que CIRCSE : pas d'`obl:agent`, ni d'`obl:lmod` / `obl:tmod`, ni de relatives sans antécédent en `:relcl`.
- **Gérondif et adjectif verbal** : la conversion les rend par `VerbForm=Part` avec `Aspect=Prosp`, alors que le LDT les distinguait par le mode (`g` adjectif verbal, `d` gérondif).
- La coordination, tête de la structure dans le LDT (`COORD`), est reconstruite selon UD : premier conjoint tête, `cc` sur le conjoint suivant.
- Ensemble petit mais varié, poésie comprise : c'est le seul treebank UD qui couvre Virgile et Ovide.
