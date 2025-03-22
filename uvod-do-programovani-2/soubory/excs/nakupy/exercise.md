---
title: Nákupy
demand: 4
---

V souboru [GroceryBasket.csv](assets/GroceryBasket.csv) máš typy produktů, které nakupují zákazníci jednoho supermarketu. Jeden řádek vždy představuje jeden typ nákupu a data na řádku jsou jednotlivé typy položek v jeho/jejím košíku. Kterou dvojici typů produktů nakupují zákazníci nejčastěji?

Pro řešení můžeš využít modul `itertools`, který je součástí Pythonu. Funkce `itertools.combinations()` ti ze seznamu položek vygeneruje všechny kombinace. Protože potřebuješ dvojice, vlož jako druhý parametr funkce číslo 2. S využitím této funkce můžeš vygenerovat všechny dvojice produktů v každém nákupním košíku a spočítat, jak často se která z nich vyskytuje.


```python
import itertools
# Příklad seznamu produktů
items = ["Produce", "Dairy & Eggs", "Meat & Poultry"]
# Vytvoření dvojic
current_combinations = itertools.combinations(items, 2)
# Převod na seznam
current_combinations = list(current_combinations)
print(current_combinations)
```
