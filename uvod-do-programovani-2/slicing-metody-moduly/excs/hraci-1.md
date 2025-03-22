---
title: Hráči
demand: 2
---

Uvažuj skupinu tří hráčů, kteří hrají karetní hru. Každý hráč dostane 5 karet a každá karta je označena dvěma písmeny - barvou (H, T, C, P - označují kříže, káry, srdce a píky) a hodnotou (čísla od 2 do 9).

Hráči mohou získat body, pokud mají řadu alespoň tří karet (může jich být i více) s po sobě jdoucími hodnotami (např. H3-T4-H5-P6), získá počet bodů, který odpovídá součtu všech hodnot v řadě (pro daný příklad je počet bodů 3+4+5+6 = 18).

Pokud má hráč více karet stejné hodnoty, počítá se do bodů pouze jedna z karet. Karty jsou vždy seřazené dle čísla a následně dle barvy v pořadí H, T, C, P. Vypočítej pro 10 řádků (10 her) součet bodů pro všechny hráče. Např. H3-T4-H4-H5-P6 je pořád za 18 bodů.

```py
data = [
    ["H2-C4-T5-H5-T6", "P2-T2-C3-T4-P8", "P3-T3-P4-T7-H9"],
    ["C2-H2-C3-P4-P7", "P2-P5-C5-H5-H6", "P3-C6-T6-P8-H8"],
    ["T2-T3-C5-H5-T9", "C2-P3-T5-T7-H9", "P2-C3-T4-P7-C7"],
    ["P3-H4-H5-C7-P8", "P2-H6-C8-C9-T9", "T3-H3-P4-T4-C5"],
    ["C3-T4-H4-T5-H8", "C2-C4-C7-C8-T8", "H3-P6-C6-T6-P9"],
    ["C2-C5-T5-C6-C9", "P3-T3-P6-T7-H8", "C3-C4-T4-C8-T9"],
    ["T5-C6-P7-C7-P9", "P3-H3-P4-T4-P6", "T2-P5-H5-H6-H7"],
    ["H2-C4-T5-P9-H9", "T3-P7-T7-C8-T9", "P3-C3-P6-H7-C9"],
    ["P4-P6-H6-C7-P9", "H2-H3-C4-H7-H8", "P2-C2-P5-T6-C8"],
    ["P2-T2-H7-P9-C9", "P3-H3-H4-T5-P6", "C2-H5-T6-P7-T7"],
]
```

Níže jsou příklady výstupu. Pro první kolo vypadají body takto:

```
[15, 9, 0]
```

Hráč č. 1 (v lidském počítání, tj. od 1) má postupku C4-T5-H5-T6 (4 + 5 + 6 = 15), druhá hráč má postupku (2 + 3 + 4 = 9), poslední hráč nemá postupku žádnou.

Po druhém kole vypadají výsledky takto (skóruje pouze první hráč):

```
[24, 9, 0]
```

Po třetím kole vypadají výsledky takto (skóruje pouze třetí hráč):

```
[24, 9, 9]
```

Po čtvrtém kole vypadají výsledky takto (skóruje první a třetí hráč):

```
[36, 9, 21]
```

Po poslední hře vypadají výsledky takto:

```
[66, 81, 57]
```
