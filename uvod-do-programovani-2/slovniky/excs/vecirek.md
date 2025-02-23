---
title: Paranoidní večírek.
demand: 4
---

Pracuješ pro paranoidního pořadatele večírku, který rozhodl, že každý z pozvaných hostů bude mít speciální heslo, které je platné jen pro něj. Seznam hostů a jejich hesel je níže. Napiš program, který nejprve zkontroluje, zda je host na seznamu, a pokud tam je, zeptá se ho na heslo a zkontroluje jeho správnost. Hostu na seznamu, který zadá správné heslo, vypíše program text: `"Smíš vstoupit."`

```py
passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}
```

:::solution
```py
passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}
name = input("Zadej jméno: ")
if name in passwords:
    password = input("Zadej heslo: ")
    if password == passwords[name]:
        print("Smíš vstoupit.")
    else:
        print("Toto není správné heslo.")
else:
    print("Bohužel nejsi na seznamu.")
```
:::
