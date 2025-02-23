---
title: Známky z písemek
demand: 3
---

Máme data o písemce, která obsahovala 4 otázky. Za každou otázku mohl student (studentka) získat max. 10 bodů. Výsledky studentů jsou v následující tabulce.

| Student | Otázka 1 | Otázka 2 | Otázka 3 | Otázka 4 |
| ----    | -------- | -------- | -------- | -------- |
| A       | 9        | 7        | 8        | 5        |
| B       | 5        | 3        | 6        | 6        |
| C       | 8        | 4        | 9        | 7        |
| D       | 8        | 5        | 4        | 8        |
| E       | 10       | 6        | 10       | 7        |


Ulož si známky studentů do dvourozměrného seznamu.

Spočítej známku jednotlivých studentů. Známku urči podle celkového počtu bodů ze všech příkladů. Bodovací tabulku najdeš níže.

| Body        | Známka |
| ----------- | ------ |
| 36 a více   | 1      |
| 32 a více   | 2      |
| 26 a více   | 3      |
| 20 a více   | 4      |
| méně než 20 | 5      |

Vypočítej průměrné body z jednotlivých otázek. Ze které otázky dostali studenti v průměru nejvíce bodů? A ze které naopak nejméně?

:::solution
```py
import statistics

data = [
    ["Student", "Otázka 1", "Otázka 2", "Otázka 3", "Otázka 4"],
    ["A", 9, 7, 8, 5],
    ["B", 5, 3, 6, 6],
    ["C", 8, 4, 9, 7],
    ["D", 8, 5, 4, 8],
    ["E", 10, 6, 10, 7]
]

for radek in data[1:]:
    prumer = statistics.mean(radek[1:])
    print(f"Průměr studenta {radek[0]} je {prumer}")

body_za_otazky = []
for otazka in data[0][1:]:
    body_za_otazky.append([otazka])

for radek in data[1:]:
    index_otazka = 0
    for body_otazka in radek[1:]:
        body_za_otazky[index_otazka].append(body_otazka)
        index_otazka = index_otazka + 1

for radek in body_za_otazky:
    prumer = statistics.mean(radek[1:])
    print(f"Průměr za otázku {radek[0]} je {prumer}")
```
:::
