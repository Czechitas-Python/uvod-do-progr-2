---
title: Karty 3
demand: 4
---

Zkusme vyřešit problém losování karet tak, aby se nám nemohlo stát, že nám nějaká karta padne vícekrát, když by správně v balíčku měla být od každé karty pouze jedna.

Ze souboru [karty.txt](assets/karty.txt) si načtěte do seznamu kompletní balíček karet. Zadání je stejné jako v předchozí úložce, tedy vylosovat 4 karty z balíčku a vypsat je jako seznam spolu se součtem hodnot.

Existuje vícero možných postupů, které vedou ke stejnému výsledku. Zde už můžete trochu zagooglit. Ve většině postupů se vám bude hodit metoda, který umí odstranit prvek seznamu na zadaném indexu:

```py
x = [1, 2, 3]
x.pop(0)
print(x)  # [2, 3]
```

Také se vám může hodit funkce `shuffle()` z modulu `random`, která umí náhodně zamíchat seznam.
