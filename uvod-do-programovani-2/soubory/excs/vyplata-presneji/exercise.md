---
title: Výplata přesněji
demand: 2
---

Zatím jsme výplatu počítali za předpokladu, že každý měsíc odpracujeme stejný počet hodin, což není příliš realistické. Stáhněte si textový soubor [vykaz.txt](assets/vykaz.txt), který obsahuje 12 řádků a na každém řádku počet odpracovaných hodin za každý měsíc za poslední rok.

1. Otevřete tento soubor ve svém programu a načtěte hodnoty na řádcích do seznamu `vykaz`. Vytiskněte tento seznam do terminálu funkcí `print()` abyste si ověřili, že jste soubor načetli správně.
1. Nechte uživatele zadat na příkazovém řádku hodinovou mzdu. Spočítejte a na výstup vytiskněte celkovou výplatu za celý rok a průměrnou výplatu na jeden měsíc.

:::solution
```py
lines = []
vykazy = []

with open('vykaz.txt', encoding='utf-8') as file:
    for line in file:
        vykazy.append(float(line))

hodinova_mzda = int(input("Napiš hodinovou mzdu v Kč: "))
celkova_mzda = 0
    
for vykaz in vykazy:
    celkova_mzda += hodinova_mzda * vykaz
    
print(celkova_mzda)
print(celkova_mzda / len(vykazy))
```
:::
