---
title: Zarovnání výpisu
demand: 4
---

Vypište seznam čísel každé na nový řádek zarovnané vpravo na délku nejdelšího čísla. Při vytvoření funkce můžeš počítat s tím, že v seznamu jsou pouze kladná celá čísla.

```py
numbers = [7728, 88, 958621, 5941, 959847272, 3944, 80, 521, 57035, 3967894]
```

Návod:

1. Zjistěte kolik znaků zabírá nejdelší číslo ze seznamu
1. Napište funkci, která dostane řetězec a délku, na kterou má text vyplnit zleva mezerami
1. Bonus: funkce bude mít volitelný parametr, jakým znakem má text vyplňovat

Výstup:

```shell
     7728
       88
   958621
     5941
959847272
     3944
       80
      521
    57035
  3967894
```

Výstup bonusu:

```
.....7728
.......88
...958621
.....5941
959847272
.....3944
.......80
......521
....57035
..3967894
```

:::solution
```py
def aligned_print(numbers, len_max_number, character="."):
    for item in numbers:
        print(f"{character * (len_max_number - len(str(item)))}{item}")


numbers = [7728, 88, 958621, 5941, 959847272, 3944, 80, 521, 57035, 3967894]
# Víme, že největší číslo je současně nejdelší
max_number = max(numbers)
len_max_number = len(str(max_number))
aligned_print(numbers, len_max_number)
```
:::
