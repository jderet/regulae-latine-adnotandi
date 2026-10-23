# Index Thomisticus Treebank (IT-TB)

| | |
|---|---|
| Producteur | CIRCSE, Università Cattolica del Sacro Cuore, Milan (M. Passarotti), à partir de 2006 |
| Textes | œuvres de Thomas d'Aquin, tirées de l'*Index Thomisticus* de R. Busa (près de 11 millions de mots, lemmatisés et analysés à partir de 1949) |
| Format | style analytique du *Prague Dependency Treebank* |
| Normes | les mêmes *Guidelines* que le [LDT](ldt.md) (2007), écrites en commun |
| Consultation | <https://itreebank.marginalia.it> |

## Principes

- **Mêmes relations que le LDT** (`PRED`, `SBJ`, `OBJ`, `ATR`, `ADV`, `PNOM`, `AuxP`, `AuxC`, `COORD`…), avec les mêmes choix : les mots grammaticaux sont têtes, *sum* est tête de la phrase copulative.
- **Morphologie de l'*Index Thomisticus*** : la classification d'origine de Busa est flexionnelle et tripartite (flexion nominale, flexion verbale, mots invariables). Les catégories de discours UD ont dû être reconstruites à la conversion, ce que décrit Cecchini et al. (2018).
- Le code morphologique (`C1|grn1|casD|gen2|vgr1`) est conservé comme XPOS dans [UD_Latin-ITTB](ittb.md).

Les fiches de ce site ne montrent que la version UD de l'IT-TB.

## Références

- Cecchini, F. M., Passarotti, M., Marongiu, P., Zeman, D. (2018). *Challenges in Converting the Index Thomisticus Treebank into Universal Dependencies*. UDW 2018.
