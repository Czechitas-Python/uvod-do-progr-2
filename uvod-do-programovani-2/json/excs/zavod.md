---
title: Závod
demand: 3
---

Pracuj dál se souborem `zavod.json`. Cílem cvičení je zjistit čas závodníka, který získal stříbrnou medaili - seznam závodníků je seřazený, tedy výherce je zapsán jako první v našem souboru.

:::solution
```py
import json

with open("zavod.json", encoding="utf-8") as file:
    data = json.load(file)

print(data[1]["casy"]["oficialni"])
```
:::
