---
title: Vytvoření souboru
demand: 2
---

Napište program, který se po spuštění zeptá na název souboru, který má vytvořit (nebo přepsat, pokud už ten soubor existuje), a pak se zeptá na řádek textu, který má do souboru zapsat.

:::solution
```py
file_name = input("Zadej název souboru: ")
text = input("Zadej text: ")

with open(file_name, mode="w", encoding="utf-8") as output_file:
    print(text, file=output_file)
```
:::
