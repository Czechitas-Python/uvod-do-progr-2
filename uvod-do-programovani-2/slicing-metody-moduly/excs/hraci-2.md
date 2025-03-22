---
title: Hráči podruhé
demand: 2
---

Tento příklad je rozšířením předchozího. Oproti předchozímu zadání nyní dostávají hráči 8 karet. Stále platí, že každá z karet je označena dvěma písmeny - barvou (H, T, C, P - označují kříže, káry, srdce a píky) a hodnotou (čísla od 2 do 9).

Hráči mohou získat body, pokud mají řadu alespoň tří karet (může jich být i více) s po sobě jdoucími hodnotami (např. H3-T4-H5-P6), získá počet bodů, který odpovídá součtu všech hodnot v řadě (pro daný příklad je počet bodů 3+4+5+6 = 18). Pokud má hráč více karet stejné hodnoty, počítá se do bodů pouze jedna z karet. Karty jsou vždy seřazené dle čísla a následně dle barvy v pořadí H, T, C, P. Vypočítej pro 10 řádků (10 her) součet bodů pro všechny hráče. Pozor ale, že nyní může mít každý hráč během jedné hry řad více. Například může mít karty "H2-C3-T4-H7-C8-P8-H9-T9". V takovém případě dostává 2+3+4 = 9 bodů za první řadu a 7+8+9 za druhou řadu.


```python
data = [
    ["C2-P4-C4-H4-H5-C7-H8-P9", "T2-P3-H3-C6-T7-H7-T8-C9", "P2-H2-C3-T4-P5-H6-T9-H9"],
    ["C2-C4-H4-C5-C6-P7-P8-P9", "P2-C3-T4-H6-C7-C8-H8-C9", "H2-T3-H3-H5-T6-H7-T8-T9"],
    ["P2-P3-C3-H4-H5-P6-T6-T8", "T2-H2-H3-P5-P7-C7-H8-P9", "C2-C5-T5-C6-H6-T7-T9-H9"],
    ["T2-H3-H4-P6-H6-C8-T8-C9", "P2-C4-C5-T5-P7-C7-H7-H8", "P3-C3-T3-H5-C6-T7-P8-H9"],
    ["T2-P3-P4-C5-T5-H6-C9-T9", "C2-C4-P5-P6-C6-H7-T8-H8", "H2-C3-H3-H4-T6-C7-T7-P9"],
    ["C2-C3-P4-H4-C6-T7-C8-T8", "P2-T3-C4-T6-H6-P7-C7-C9", "T2-H2-C5-T5-P6-H7-H8-H9"],
    ["P2-H3-T4-H4-C6-T7-H8-H9", "C2-T2-H2-T3-C5-H5-P7-C7", "P3-C3-C4-P6-T6-H7-T8-P9"],
    ["T2-T4-H4-P5-T5-C7-P8-H8", "H2-P3-C3-H3-H5-T7-C8-P9", "P4-C4-C5-T6-P7-C9-T9-H9"],
    ["H5-P6-T6-H6-T7-H7-C8-T8", "P2-H2-C4-P5-C6-P7-P8-H8", "T2-P3-C3-T3-P4-P9-C9-H9"],
    ["T3-P4-T4-H4-C5-C6-P7-H7", "C2-T5-H5-P6-P8-C8-P9-H9", "P2-H2-C3-C4-P5-T6-T8-C9"],
]
```

