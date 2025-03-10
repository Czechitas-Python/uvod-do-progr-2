---
title: Nápravy
demand: 4
---

Náprava je část vozidla, která spojuje kola s karosérií vozidla. U nákladních vozidel ho můžeme chápat jako počet "dvojic kol". Počet náprav je důležitý napříkad kvůli maximální povolené hmotnosti vozidla.

Uvažuj limity pro maximální hmotnost nákladního vozidla, které jsou v tabulce níže.

| Počet náprav | Maximální dovolená hmotnost v tunách |
| ------ | ---- |
| 2   | 18 |
| 3  | 25 |
| 4   | 32 |
| 5  | 48 |

Pokud je limit překročen, platí provozovatel pokutu 1000 Kč za každou tunu, o které je vozidlo těžší. Například pokud má vozidlo 4 nápravy a hmotnost 34 tun, platí provozovatel pokutu 2000 Kč. Napiš funkci `spocitej_pokutu()`, která bude mít dva parametry - `pocet_naprav` (počet náprav vozidla) a `hmotnost` (hmotnost vozidla v tunách). Funkce na základě těchto parametrů vypočte výši pokuty a vrátí ji jako celé číslo.

```py
pokuta = spocitej_pokutu(4, 34)
print(pokuta) # 2000
```

Dále uvažuj následující dvourozměrný seznam, kde na prvním místě vnořeného seznamu je počet náprav vozidla a na druhém místě je zjištěná hmotnost.

```py
vazeni = [
    [4, 33],
    [2, 19],
    [3, 29],
    [3, 27],
    [5, 53],
    [5, 51],
    [2, 20],
]

```

Projdi seznam pomocí cyklu a pro každé vážení urči (s využitím funkce `spocitej_pokutu()`) výši pokuty. Spočítej celkovou výši pokut za všechna vážení.

:::solution
```py
def spocitej_pokutu(pocet_naprav: int, hmotnost: int) -> int:
    if pocet_naprav == 2:
        prekroceni = max(0, hmotnost - 18)
    elif pocet_naprav == 3:
        prekroceni = max(0, hmotnost - 25)
    elif pocet_naprav == 4:
        prekroceni = max(0, hmotnost - 32)
    elif pocet_naprav == 5:
        prekroceni = max(0, hmotnost - 18)
    return 1000 * prekroceni

vazeni = [
    [4, 33],
    [2, 19],
    [3, 29],
    [3, 27],
    [5, 53],
    [5, 51],
    [2, 20],
]

pokuty = []
for radek in vazeni:
    pokuty.append(spocitej_pokutu(radek[0], radek[1]))
print(f"Celková hodnota pokut je {sum(pokuty)} Kč.")
```
:::
