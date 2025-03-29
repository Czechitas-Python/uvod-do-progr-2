---
title: Závod
demand: 3
---

Pracuj dál se souborem `zavod.json`. Cílem cvičení je zjistit čas závodníka, který získal stříbrnou medaili - seznam závodníků je seřazený, tedy výherce je zapsán jako první v našem souboru. Budeš tedy muset projít data pomocí cyklu a vytvořit seznam všech závodníků, kteří závod dokončili, tj. jejich oficiální čas není `'DNF'`.

:::solution
```py
import json

with open("zavod.json", encoding="utf-8") as file:
    data = json.load(file)

print(data[1]["casy"]["oficialni"])
```
:::
