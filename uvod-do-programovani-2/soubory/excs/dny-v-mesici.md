---
title: Dny v měsíci
demand: 1
---

Napište program, který bude mít přímo v kódu zapsaný počet dní v jednotlivých měsících takto:

```py
pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
```

Nechte váš program vypsat tento seznam do souboru s názvem `kalendar.txt`, každé číslo na jeden řádek.

:::solution
```py
pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

with open("kalendar.txt", encoding="utf-8", mode="w") as file:
    for dny in pocty_dni:
        print(dny, file=file)
```
:::
