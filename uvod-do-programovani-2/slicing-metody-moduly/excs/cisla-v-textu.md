---
title: Čísla v textu
demand: 3
---

Máme obdobné zadání jako v předchozím cvičení, avšak tentokrát máme čísla
zadána nikoliv v seznamu, ale v řetězci oddělená mezerou:

```py
hodnoty = '12.1 1.68 7.45 -11.51'
```

K poslednímu číslu v seznamu chceme přičíst 0.25 tak, aby výsledek vypadal
takto

```py
hodnoty = '12.1 1.68 7.45 -11.26'
```

Určitě se vám budou hodit metody `split` a `join`.

:::solution
```py
hodnoty = '12.1 1.68 7.45 -11.51'

list_hodnoty = hodnoty.split()
posledni_hodnota = list_hodnoty[-1]
posledni_hodnota = float(posledni_hodnota)
vysledek = posledni_hodnota + 0.25
print(vysledek)
vysledek = str(vysledek)
list_hodnoty[-1] = vysledek
vysledek_hodnoty = " ".join(list_hodnoty)
print(vysledek_hodnoty)
```
:::
