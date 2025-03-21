---
title: Pasažéři
demand: 4
---

Autobus mezi Zdebudevsí a Kozoprdy jezdí čtyřikrát denně každý všední den v týdnu. Za poslední týden jsme naměřili počty pasažérů pro každou jízdu tam i zpět. Data jsou uložená v souboru [pasazeri.txt](assets/pasazeri.txt). Jízda vždy obsahuje dvě čísla oddělená čárkou, která udávají počet pasažérů směrem tam a směrem zpět.

1. Napište program, který pro první den vypíše, kolik pasažérů jelo celkem směrem tam a kolik směrem zpět.
1. Nechť váš program vypisuje součty pasažérů ze celý týden, tedy kolik lidí za celý týden jelo směrem tam a kolik směrem zpět.

:::solution
```py
pasazeri_tam = []
pasazeri_zpet = []

with open("pasazeri.txt") as soubor:
    for radek in soubor:
        radek_rozdeleny = radek.split()
        den_tam = 0
        den_zpet = 0
        for polozka in radek_rozdeleny:
            tam, zpet = polozka.split(",")
            den_tam += int(tam)
            den_zpet += int(zpet)
        pasazeri_tam.append(den_tam)
        pasazeri_zpet.append(den_zpet)

print(f"První den jelo tam {pasazeri_tam[0]} cestujících a zpět {pasazeri_zpet[0]} cestujících.")
print(f"Za celý týden jelo tam {sum(pasazeri_tam)} cestujících a zpět {sum(pasazeri_zpet)} cestujících.")
```
:::
