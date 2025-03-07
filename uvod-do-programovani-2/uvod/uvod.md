## Úvod, proměnné a hodnoty

Během kurzu Úvod do programování 2 - Python se ponoříme o něco hlouběji do tajů programování a podíváme se, jaké další možnosti nabízí jazyk Python. Na začátku bychom si ale měli zopakovat věci, které jsme již probírali na kurzu Úvod do programování 1, případně je známe odjinud. Před kurzem si prosím nainstaluj Python a Visual Studio Code na svůj počítač. Návod najdeš [zde](https://kodim.cz/programovani/uvod-do-progr-1/priprava/jazyky-nastroje/instalace-python).

Na této stránce najdeš několik příkladů. Nejlepší způsob, jak si svoje znalosti procvičit, je zkopírovat si kódy příkladů do Visual Studia Code nebo jiného editoru a zkusit si, co dělají.

### Proměnné

Proměnné jsou způsob, jak v našem programu uložit nějaké hodnoty. Jak jejich název napovídá, hodnotu uloženou v proměnné můžeme kdykoli změnit. Proměnné můžeme použít například jako vstup pro nějaké výpočty, předat je funkci ke zpracování nebo vypsat uživateli.

Do proměnných jsme ukládali například vstupy od uživatelů nebo výsledky našich výpočtů. Hodnoty proměnných jsme též často vypisovali na obrazovku.

U uživateli a uživatelkami našeho programu můžeme komunikovat s využitím funkce `print()`. Pokud chceme do našeho výstupu vložit informaci z proměnné, můžeme použít formátovaný řetězec. Před uvozovky vložíme písmeno `f`, aby Python věděl, že půjde o formátovaný řetězec. Poté můžeme do složených závorek vkládat názvy proměnných a Python z nich vytvoří souvislý text.

```py
play = "Každý má svou pravdu"
number_of_tickets = 3
price_per_ticket = 190
total_price = price_per_ticket * number_of_tickets

print(f"Cena {number_of_tickets} lístků na hru {play} je celkem {total_price} Kč.")
```
