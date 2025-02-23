---
title: Ruleta
demand: 5
---

Napiš funkci, která bude jednoduchou simulací rulety. Budeme uvažovat pouze možnost sázení na řady. Uživatel(ka) si může vybrat jednu ze tří řad:

- první řada (hodnoty 1, 4, 7 atd.),
- druhá řada (hodnoty 2, 5, 8 atd.),
- třetí řada (hodnoty 3, 6, 9 atd.).

Vytvoř funkci `roulette`. Funkce bude mít tři parametry: číslo na ruletě, číslo řady, na kterou uživatel(ka) sází, a výši sázky. 

Na začátku funkce `roulette` vyhodnoť, do které řady číslo náleží. Pokud uživatel vsadil na správnou řadu, vyhrává dvojnásobek sázky, v opačném případě nevyhrává nic jeho/její sázka propadá.

Nezapomeň, že 0 nepatří do žádné z řad a pokud padne, uživatel vždy prohrává.

:::solution
```py
def roulette(winning_number, line_number, bet):
    if winning_number == 0:
        return 0
    if winning_number % 3 == 1 and line_number == 1:
        return bet * 2
    if winning_number % 3 == 2 and line_number == 2:
        return bet * 2
    if winning_number % 3 == 1 and line_number == 3:
        return bet * 2
    return 0

print(roulette(0, 1, 1000))
print(roulette(1, 1, 1000))
print(roulette(2, 1, 1000))
print(roulette(3, 1, 1000))
```
:::

