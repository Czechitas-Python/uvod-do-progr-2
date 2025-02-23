---
title: Zaokrouhlování
demand: 1
---

Napište program, který dostane na vstupu desetinné číslo a na výstup napíše toto číslo zaokrouhlené nejdříve nahoru, potom dolů a potom běžným Pythonovským zaokrouhlováním.

:::solution
```py
import math

number = input("Zadej číslo: ")
number = float(number)
print(math.ceil(number))
print(math.floor(number))
print(round(number))
```
:::