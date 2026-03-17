---
title: Směny
demand: 3
---

*Poznámka: K řešení tohoto příkladu je potřeba znalost hodnoty typu tuple, které je popsaná ve čtení na doma v této lekci.*

Fastfoodová restaurace eviduje rozvrh směn v podobě slovníku. Klíčem je dvojice `(den, typ_smeny)` a hodnotou jméno zaměstnance.

Klíče ve slovníku jsou hodnoty typu `tuple`.

```py
smeny = {
    ("pondělí", "ranní"): "Natálie",
    ("pondělí", "odpolední"): "Anna",
    ("úterý", "ranní"): "Jiří",
    ("úterý", "odpolední"): "Michal",
    ("středa", "ranní"): "Anna",
    ("středa", "odpolední"): "Natálie",
    ("čtvrtek", "ranní"): "Michal",
    ("čtvrtek", "odpolední"): "Jiří",
    ("pátek", "ranní"): "Natálie",
    ("pátek", "odpolední"): "Anna",
    ("sobota", "ranní"): "Jiří",
    ("sobota", "odpolední"): "Michal",
    ("neděle", "ranní"): "Anna",
    ("neděle", "odpolední"): "Natálie",
}
```

Napiš program, který pro každého zaměstnance zjistí, zda pracuje více ranních nebo odpoledních směn, nebo zda má obou stejně. Výstup by měl vypadat například takto:

```
Natálie: stejně
Anna: stejně
Jiří: více ranních
Michal: více odpoledních
```

:::solution
```py
statistika = {}
for key, value in smeny.items():
    if value not in statistika:
        statistika[value] = {"ranní": 0, "odpolední": 0}
    statistika[value][key[1]] += 1
for key, value in statistika.items():
    if value["ranní"] > value["odpolední"]:
        print(f"{key}: více ranních")
    elif value["ranní"] < value["odpolední"]:
        print(f"{key}: více odpoledních")
    else:
        print(f"{key}: stejně")
```
:::
