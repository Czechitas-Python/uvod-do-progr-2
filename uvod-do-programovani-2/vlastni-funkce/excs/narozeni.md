---
title: Měsíc narození
demand: 3
---

Napiš funkci `month_of_birth`, která bude mít jeden parametr - rodné číslo. Funkce ze zadaného rodného čísla určí měsíc narození, které vrátí jako výstup. Nezapomeň, že pro ženy je k měsíci připočtena hodnota 50.

- Příklad: Pro hodnotu `9207054439` vrátí 7. Pro hodnotu `9555125899` vrátí 5.

:::solution
```py
def month_of_birth(birth_number: str) -> int:
    return int(birth_number[2:4]) % 50


print(month_of_birth("9207054439"))
print(month_of_birth("9555125899"))
```
:::
