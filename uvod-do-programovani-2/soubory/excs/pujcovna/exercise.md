---
title: Půjčovna
demand: 4
---

Půjčovna aut má v každém kraji ČR jedno auto s danou SPZ. Ke konci roku chce zjistit, kolik všechna auta najezdila dohromady kilometrů. V souboru [auta.txt](assets/auta.txt) je pro každou SPZ zaznamenáno kolik dané auto ujelo kilometrů za daný rok. Hodnoty jsou v tisících kilometrů. Bohužel se v jednotlivých krajích blbě zkoordinovali a někdo používal desetinnou čárku, někdo zase tečku.

**Pozor!** V souboru s daty je ještě jeden problém, který není na první pohled vidět!

Napište program, který na výstup vypíše součet všech ujetých kilometrů. Jistě se vám bude hodit metoda řetězců jménem `replace()`.

:::solution
```py
kilometry_celkem = 0
with open("auta.txt") as soubor:
    for radek in soubor:
        if len(radek.strip()) > 0:
            znacka, kilometry = radek.split()
            kilometry = kilometry.replace(",", ".")
            kilometry_celkem += float(kilometry)
print(f"Auta celkem najezdila {kilometry_celkem} kilometrů.")
```
:::
