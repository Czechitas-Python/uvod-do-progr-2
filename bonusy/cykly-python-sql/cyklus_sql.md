## Cyklus v Pythonu a dotaz v SQL

Máme tabulku s prodejem učebnic chemie v několika městech České republiky.

| Město    | Prodané kusy v roce 2021 | Prodané kusy v roce 2022 |
| -------- | ----------------------------- | ---------------------------- |
| Praha    | 4200                       | 4900                      |
| Brno     | 2500                       | 2100                      |
| Ostrava  | 1500                       | 1100                      |
| Plzeň    | 1000                       | 700                       |
| Liberec  | 700                        | 500                       |
| Olomouc  | 400                        | 300                       |

Data máme zadaná v Pythonu jako dvourozměrný seznam. Naším úkolem je zjistit, ve kterých městech prodeje učebnice poklesly.

```py
prodej_knih = [
    ["Praha", 4200, 4900],
    ["Brno", 2500, 2100],
    ["Ostrava", 1500, 1100],
    ["Plzeň", 1000, 700],
    ["Liberec", 700, 500],
    ["Olomouc", 400, 300]
]
```

## Řešení úlohy v SQL

Uvažujme, jak bychom řešili příklad v SQL. Tento příklad je založený na tom, že říkáme, jaký by měl být výsledek. Jinak řečeno, říkáme, *co chceme*. Neříkáme, jakým způsobem by měl počítač k požadovanému výsledku dojít.

```sql
SELECT mesto
FROM prodej_knih
WHERE rok2 < rok1;
```

## Řešení úlohy v Pythonu

V Pythonu s využitím cyklu říkáme, co má počítač udělat, tj. dáváme mu posloupnost kroků, kterou má provést, aby dospěl k námi požadovanému výsledku. Instrukce, které počítači dáme, jsou následující:

1. Projdi jednotlivé prvky seznamu (projdi tabulku řádek po řádku).
1. Pro každý prvek (podseznam) se podívej, jestli je hodnota ta pozici 1 větší než hodnota na pozici 2.
1. Pokud ano, vypiš prvek na pozici 0.


```py
# Projdi tabulku prodej knih řádek po řádku
for radek in prodej_knih:
    # Podívej se, jestli je hodnota na  pozici 1 větší než hodnota na pozici 2
    if radek[1] > radek[2]:
        # Pokud ano, vypiš na oprazovku hodnotu na pozici 0
        print(radek[0])
```

### První opakování cyklu

Python do proměnné `radek` vloží to, co je na začátku seznamu, tj. prodeje v Praze. To, že jde o proměnnou `radek`, určíme tím, že název `radek` vložíme mezi `for` a `in`.

```py
for radek in prodej_knih:
```

::fig[Průběh cyklu]{src=assets/cyklus-prubeh_1_1.drawio.svg}

Nyní je vyhodnocená podmínka

```py
    if radek[1] > radek[2]:
```

::fig[Průběh cyklu]{src=assets/cyklus-prubeh_1_2.drawio.svg}

Hodnota `radek[1]` je 4200 a hodnota `radek[2]` je 4900. Není tedy pravda, že je hodnota `radek[1]` větší než hodnota na pozici `radek[2]`, proto nespouštíme kód uvnitř podmínky. V cyklu již další příkazy nejsou a pokračuje dál.


### Druhé opakování cyklu

Python vidí, že není na konci seznamu, a proto tedy spouští cyklus znovu. Do proměnné `radek` vloží to, co je na dalším místě, tj. prodeje v Brně.

::fig[Průběh cyklu]{src=assets/cyklus-prubeh_2_1.drawio.svg}

Nyní je vyhodnocená podmínka

```py
    if radek[1] > radek[2]:
```

::fig[Průběh cyklu]{src=assets/cyklus-prubeh_2_2.drawio.svg}

Hodnota `radek[1]` je 2500 a hodnota `radek[2]` je 2100. V tomto případě je pravda, že hodnota `radek[1]` je větší než `radek[2]`. To znamená, že prodeje skutečně poklesly.

Python nyní spouští příkaz, který je uvnitř podmínky.

```py
        print(radek[0])
```

Hodnota `radek[0]` se nyní zobrazí na obrazovce.

### Třetí opakování cyklu

Třetí opakování cyklu se týká Ostravy.

::fig[Průběh cyklu]{src=assets/cyklus-prubeh_3_1.drawio.svg}

I zde bude podmínka vyhodnocena jako pravda a Python vypíše i "Ostrava".

::fig[Průběh cyklu]{src=assets/cyklus-prubeh_3_2.drawio.svg}

### Čtvrté opakování cyklu

Další pokračování se týká Plzně.

::fig[Průběh cyklu]{src=assets/cyklus-prubeh_4_1.drawio.svg}

Prodeje poklesly i zde.

::fig[Průběh cyklu]{src=assets/cyklus-prubeh_4_2.drawio.svg}

### Páté opakování cyklu

V Liberci prodeje taktéž klesly.

::fig[Průběh cyklu]{src=assets/cyklus-prubeh_5_1.drawio.svg}

::fig[Průběh cyklu]{src=assets/cyklus-prubeh_5_2.drawio.svg}

### Šesté opakování cyklu

A v Olomouci též prodeje taktéž klesly.

::fig[Průběh cyklu]{src=assets/cyklus-prubeh_6_1.drawio.svg}

::fig[Průběh cyklu]{src=assets/cyklus-prubeh_6_2.drawio.svg}
