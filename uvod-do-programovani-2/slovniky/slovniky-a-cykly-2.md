## Čtení na doma: Další příklad použití slovníků a cyklu

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

### Řešení úlohy v SQL

*Poznámka: Pokud jazyk SQL neznáš, můžeš tuto část přeskočit.*

Uvažujme, jak bychom řešili příklad v SQL. Tento příklad je založený na tom, že říkáme, jaký by měl být výsledek. Jinak řečeno, říkáme, *co chceme*. Neříkáme, jakým způsobem by měl počítač k požadovanému výsledku dojít.

```sql
SELECT mesto
FROM prodej_knih
WHERE rok2 < rok1;
```

### Řešení úlohy v Pythonu

V Pythonu s využitím cyklu říkáme, co má počítač udělat, tj. dáváme mu posloupnost kroků, kterou má provést, aby dospěl k námi požadovanému výsledku. Instrukce, které počítači dáme, jsou následující:

1. Projdi jednotlivé prvky seznamu (projdi tabulku řádek po řádku).
1. Pro každý prvek (slovník) se podívej, jestli je hodnota s klíčem `"prodej_2021"` větší než hodnosta s klíček `"prodej_2022"`.
1. Pokud ano, vypiš hodnotu s klíčem `"mesto"`.

```python
prodej_knih = [
    {"mesto": "Praha", "prodej_2021": 4200, "prodej_2022": 4900},
    {"mesto": "Brno", "prodej_2021": 2500, "prodej_2022": 2100},
    {"mesto": "Ostrava", "prodej_2021": 1500, "prodej_2022": 1100},
    {"mesto": "Plzeň", "prodej_2021": 1000, "prodej_2022": 700},
    {"mesto": "Liberec", "prodej_2021": 700, "prodej_2022": 500},
    {"mesto": "Olomouc", "prodej_2021": 400, "prodej_2022": 300}
]

for radek in prodej_knih:
    if radek["prodej_2021"] > radek["prodej_2022"]:
        print(radek["mesto"])
```

Níže je výstup, který kód vypíše na obrazovku.

```
Brno
Ostrava
Plzeň
Liberec
Olomouc
```

#### První opakování cyklu

Python do proměnné `radek` vloží to, co je na začátku seznamu, tj. prodeje v Praze. To, že jde o proměnnou `radek`, určíme tím, že název `radek` vložíme mezi `for` a `in`.

```py
for radek in prodej_knih:
```

![](assets/Cyklus-prubeh_slovnik_1.drawio.svg)

Nyní je vyhodnocená podmínka

```py
    if radek["prodej_2021"] > radek["prodej_2022"]:
```

Hodnota `radek["prodej_2021"]` je 4200 a hodnota `radek["prodej_2022"]` je 4900. Není tedy pravda, že je hodnota `radek["prodej_2021"]` větší než hodnota na pozici `radek["prodej_2022"]`, proto nespouštíme kód uvnitř podmínky. V cyklu již další příkazy nejsou a pokračuje dál.


#### Druhé opakování cyklu

Python do proměnné `radek` vloží další hodnotu ze seznamu, tj. prodeje v Brně. To, že jde o proměnnou `radek`, určíme tím, že název `radek` vložíme mezi `for` a `in`.

```py
for radek in prodej_knih:
```

![](assets/Cyklus-prubeh_slovnik_2.drawio.svg)

Nyní je vyhodnocená podmínka

```py
    if radek["prodej_2021"] > radek["prodej_2022"]:
```

Hodnota `radek["prodej_2021"]` je 2500 a hodnota `radek["prodej_2022"]` je 2100. Je pravda, že je hodnota `radek["prodej_2021"]` větší než hodnota na pozici `radek["prodej_2022"]`, proto spouštíme kód uvnitř podmínky. Program vypíše na obrazovku `Brno`.


#### Třetí opakování cyklu

Python do proměnné `radek` vloží další hodnotu ze seznamu, tj. prodeje v Ostravě. To, že jde o proměnnou `radek`, určíme tím, že název `radek` vložíme mezi `for` a `in`.

```py
for radek in prodej_knih:
```

![](assets/Cyklus-prubeh_slovnik_3.drawio.svg)

Nyní je vyhodnocená podmínka

```py
    if radek["prodej_2021"] > radek["prodej_2022"]:
```

Hodnota `radek["prodej_2021"]` je 1500 a hodnota `radek["prodej_2022"]` je 1100. Je pravda, že je hodnota `radek["prodej_2021"]` větší než hodnota na pozici `radek["prodej_2022"]`, proto spouštíme kód uvnitř podmínky. Program vypíše na obrazovku `Ostrava`.

### Průchod slovníku

Pokud procházíme slovník, využijeme metodu `.items()`, abychom získali klíč a hodnotu. Připravíme si dvě proměnné. Můžeme je pojmenovat jakkoli. Do prvním proměnné bude Python ukládat klíč aktuální položky a do druhé proměnné hodnotu aktuální položky.

```python
slovnik = {
    "jablko": "apple",
    "pes": "dog",
    "kočka": "cat"
}

for key, value in slovnik.items():
    print(f"Slovo {key} přeložíme jako {value}.")
```

```
Slovo jablko přeložíme jako apple.
Slovo pes přeložíme jako dog.
Slovo kočka přeložíme jako cat.
```

#### První průchod

Do proměnné `"key"` uloží Python `jablko` a do proměnné `value` uloží Python `"apple"`.

![](assets/Cyklus-Slovnik_items-1.drawio.svg)

#### Druhý průchod

Do proměnné `"key"` uloží Python `pes` a do proměnné `value` uloží Python `"dog"`.

![](assets/Cyklus-Slovnik_items-2.drawio.svg)

#### První průchod

Do proměnné `"key"` uloží Python `kočka` a do proměnné `value` uloží Python `"cat"`.

![](assets/Cyklus-Slovnik_items-3.drawio.svg)
