---
title: Průměr
demand: 2
---

Mějme proměnnou `s`, ve které předpokládáme uložený nějaký seznam. Sestavte v výraz (vzoreček), který spočítá průměrnou hodnotu v takovém seznamu. Otestujte jej na seznamech různých délek.

:::solution
```py
s = [1, 2, 3, 4, 5, 6, 7, 8, 9]
v = sum(s)/len(s)
print(v)
```
:::
