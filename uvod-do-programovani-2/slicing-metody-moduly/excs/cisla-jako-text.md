---
title: Čísla jako text
demand: 2
---

Mějme seznam celých čísel zadaných jako text

```py
hodnoty = ['12', '1', '7', '-11']
```

Potřebujeme k třetímu číslu v seznamu přičíst 4, aby výsledek vypadal takto:

```py
hodnoty = ['12', '1', '11', '-11']
```


:::solution
```py
treti_hodnota = hodnoty[2]
treti_hodnota = int(treti_hodnota)
vysledek = treti_hodnota + 4
vysledek = str(vysledek)
hodnoty[2] = vysledek
print(hodnoty)
```
:::
