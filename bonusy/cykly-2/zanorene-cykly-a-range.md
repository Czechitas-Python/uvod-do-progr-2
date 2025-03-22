## Zanořené cykly a range

Uvažujme, že si vytváříme tabulku, která bude sloužit k rezervaci míst v dopravních prostředcích. Na začátku uvažujeme tabulku pro místa v jednom autobusu. Náš autobus má místa od 1 do 40, proto funkci `range()` zadáme hodnoty 1 a 41 (podobně jako slice je druhé číslo vynechané).


```python
places = {}
for i in range(1, 41):
    # Vložíme prázdnou hodnotu - na začátku je místo volné
    places[i] = None
# Rezervace místa 5
places[5] = "Jirka Pešík"
# Rezervace místa 6
places[6] = "Jakub Červinka"
print(places)
```

Nyní uvažujme místa v jednom vlaku. Vlak má několik vozů a v každém voze jsou sedačky. Uvažujme třeba místa od 1 do 30 v každém voze a vozy s čísly 1 a 2. Nejprve si výstup vypíšeme na obrazovku.


```python
places = {}
for i in range(1, 3):
    for j in range(1, 31):
        print(f"Vůz {i}, sedadlo {j}")
```

Nyní vložíme místa do slovníku. Máme několik možností. První z nich je vícerozměrný klíč ve slovníku, další by byl vícerozměrný slovník. Pro vícerozměrný klíč musíme použít n-tici (tuple).

```python
places = {}
for i in range(1, 3):
    for j in range(1, 31):
        places[(i, j)] = None
# Rezervace místa 35 ve voze 1
places[(1, 15)] = "Jirka Pešík"
# Rezervace místa 36 ve voze 1
places[(1, 16)] = "Jakub Červinka"
```

Třetí rozměr přidáme, pokud uvažujeme několik vlaků. Uvažujme 2 různé vlaky, každý má 2 vozy a každý vůz 30 míst.


```python
places = {}

for i in range(1, 3):
    for j in range(1, 3):
        for k in range(1, 31):
            print(f"Vlak R{i}, vůz {j}, sedadlo {k}")
            places[(i, j, k)] = None
# Rezervace místa 35 ve voze 1 ve vlaku 3
places[(2, 1, 15)] = "Jirka Pešík"
# Rezervace místa 36 ve voze 1 ve vlaku 3
places[(2, 1, 16)] = "Jakub Červinka"
print(places)
```

Můžeme si zkusit vytvořit i vícerozměrné slovníky. Zde je potřeba v rámci cyklů vytvořit zanořené slovníky, abychom měli kam vkládat hodnoty.


```python
places = {}

for i in range(1, 3):
    # Vytvoření zanořeného slovníku pro vlak
    places[i] = {}
    for j in range(1, 3):
        # Vytvoření zanořeného slovníku pro vůz
        places[i][j] = {}
        for k in range(1, 31):
            print(f"Vlak R{i}, vůz {j}, sedadlo {k}")
            places[i][j][k] = None
# Rezervace místa 35 ve voze 1 ve vlaku 3
places[2][1][15] = "Jirka Pešík"
# Rezervace místa 36 ve voze 1 ve vlaku 3
places[2][1][16] = "Jakub Červinka"
print(places)
```

