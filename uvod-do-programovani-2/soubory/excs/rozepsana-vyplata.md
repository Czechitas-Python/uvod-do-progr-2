---
title: Rozepsaná výplata
demand: 3
---

Modifikujte program pro počítání výplaty z předchozí sekce tak, aby nevypisoval průměrnou výplatu za rok, nýbrž aby vypsal konkrétní vyplacenou částku pro každý měsíc zvlášť.

1. Nejprve tyto informace vypište na terminál
1. Poté program upravte tak, aby vypsal tyto výsledky do souboru


:::solution
```py
vyplata_po_mesicich = []

hodinova_mzda = int(input("Napiš hodinovou mzdu v Kč: "))

with open('vykaz.txt', encoding='utf-8') as soubor:
    for radek in soubor:
        vyplata = float(radek) * hodinova_mzda
        vyplata_po_mesicich.append(vyplata)
        print(vyplata)

with open("vyplata_po_mesicich.txt", "w", encoding="utf-8") as soubor:
    for hodnota in vyplata_po_mesicich:
        print(hodnota, file=soubor)
```
:::
