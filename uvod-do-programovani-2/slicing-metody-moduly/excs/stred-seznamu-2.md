---
title: Střed seznamu podruhé
demand: 5
---

Sestavte vzoreček, který vrátí číslo nacházející se přesně uprostřed v zadaném
seznamu `s`. Tentokrát však u seznamů sudé délky vyberte jako střed číslo blíž k
**začátku** seznamu.

:::solution
```py
s = [1, 2, 3, 4, 5, 6, 7, 8]

if len(s) % 2 == 0:
    prostredni_cislo = s[len(s) // 2 - 1]
    print(prostredni_cislo) # tato varianta se vytiskne pokud je pocet prvku v seznamu sudy
else:
    prostredni_cislo = s[len(s) // 2]
    print(prostredni_cislo) # tato varianta se vytiskne pokud je pocet prvku v seznamu lichy
```
:::
