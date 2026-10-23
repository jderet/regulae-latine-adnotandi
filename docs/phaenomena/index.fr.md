# Phénomènes

Chaque fiche suit le même plan :

1. **En bref** : un tableau qui donne, norme par norme, l'analyse du phénomène, des treebanks UD aux formats d'origine et à la norme adnotationes-latinae ;
2. **Points de divergence** : ce qui sépare réellement les normes, chiffres à l'appui ;
3. **Fréquences** : pour chaque treebank UD, les analyses les plus fréquentes du phénomène, comptées par le [script](../methode.md) ;
4. **Exemples** : une phrase par treebank, qui suit l'analyse la plus fréquente de ce treebank, avec l'arbre et les lignes CoNLL-U. Pour Perseus et PROIEL s'ajoute la même phrase dans son format d'origine.

## Fiches

| Fiche | Ce qui diverge |
|---|---|
| [Copule : *sum*](copula.md) | qui est tête, *sum* ou l'attribut ; *sum* dans la périphrase obligative |
| [Ablatif absolu](ablativus-absolutus.md) | `advcl:abs` ou `advcl` ; formules de datation |
| [Proposition infinitive](accusativus-cum-infinitivo.md) | `ccomp` ou `csubj` ; `xcomp` ou `ccomp` après *iubeo*, *sino* |
| [Gérondif et adjectif verbal](gerundium-gerundivum.md) | distinction morphologique ; préposition `case` ou `mark` |
| [Coordination par *-que*](coordinatio.md) | découpage ; rattachement à l'hôte ou à la tête du conjoint ; *neque* |
| [Proposition sans verbe](sine-verbo.md) | tête quand l'attribut est au datif, au génitif ou adverbe ; nœud vide de PROIEL, `ExD` du LDT |
| [Ellipse du verbe](ellipsis.md) | `orphan` ou nœud vide ; verbe absent du premier membre ; ellipse hors coordination |

## À venir

- Relatives : `acl:relcl`, relatives sans antécédent (`csubj:relcl`…)
- Comparaison : *quam*, ablatif de comparaison (`obl:cmp`, `advcl:cmp`)
- Obliques régis : datif et ablatif d'argument (`obl:arg`, `iobj`)
- Complément d'agent et datif d'agent (`obl:agent`)
- Prédicatif (`advcl:pred`, `xcomp`, `ATV`/`AtvV`, `xadv`)
- Discours rapporté : *inquit*, discours direct (`parataxis:reporting`, `ccomp:reported`)
- Lieu et temps (`obl:lmod`, `obl:tmod`, `advmod:lmod`)
- Déterminants et pronoms (`DET` ou `PRON` pour *hic*, *ille*, *is*)
- Particules de discours (*nam*, *enim*, *autem*, *quidem*)
- Enclitique *-ne* et interrogation
- Noms propres composés (`flat:name`) et abréviations (*M.*, *Kal.*)
- Nombres et chiffres romains
- Lemmes : comparatifs et superlatifs, graphies u/v et i/j, participes lexicalisés, déponents
