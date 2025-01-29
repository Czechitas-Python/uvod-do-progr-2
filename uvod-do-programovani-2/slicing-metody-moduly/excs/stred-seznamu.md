---
title: Střed seznamu
demand: 4
---

Sestavte výraz, který vrátí číslo nacházející se přesně uprostřed v zadaném seznamu `s`. U seznamů liché délky je střed jasně definovaný, ovšem u seznamů sudé délky nám padne mezi dvě čísla. V takovém případě vyberte jako střed číslo blíže ke konci seznamu.

:::solution
```py
s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
prostredni_cislo = s[len(s) // 2]
print(prostredni_cislo)
```
:::
