---
title: Pohyby na účtu
demand: 2
---

Mějme seznam pohybů na nějakém bankovním účtu:

```pycon
pohyby = [1200, -250, -800, 540, 721, -613, -222]
```

1. Vypište v pořadí třetí pohyb z uvedeného seznamu.
1. Vypište všechny pohyby kromě prvních dvou.
1. Vypište kolik je všech pohybů dohromady.
1. Pomocí volání vhodných funkcí vypište nejvyšší a nejnižší pohyb.
1. Spočítejte celkový přírůstek na účtu za dané období. Pozor, že přírůstek může vyjít i záporný.

:::solution
```
# Vypište v pořadí třetí pohyb z uvedeného seznamu.
print(pohyby[2])
# Vypište všechny pohyby kromě prvních dvou.
print(pohyby[2:])
# Vypište kolik je všech pohybů dohromady.
print(len(pohyby))
# Pomocí volání vhodných funkcí vypište nejvyšší a nejnižší pohyb.
print(max(pohyby))
print(min(pohyby))
# Spočítejte celkový přírůstek na účtu za dané období. Pozor, že přírůstek může vyjít i záporný.
print(sum(pohyby))
```
:::
