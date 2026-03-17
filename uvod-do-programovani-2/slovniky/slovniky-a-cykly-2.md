## Slovníky a cykly (alternativní příklad)

### Průchod slovníku

Pokud procházíme slovník, využijeme metodu `.items()`, abychom získali **klíč** a **hodnotu**. Připravíme si dvě proměnné. Můžeme je pojmenovat **jakkoli**. Do první proměnné bude Python ukládat klíč aktuální položky a do druhé proměnné hodnotu aktuální položky.

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

#### Třetí průchod

Do proměnné `"key"` uloží Python `kočka` a do proměnné `value` uloží Python `"cat"`.

![](assets/Cyklus-Slovnik_items-3.drawio.svg)

#### Jiné názvy proměnných

Názvy proměnných opravdu závisí jen na nás. Pokud bychom např. použili názvy `word_en` a `word_cz`, program bude fungovat úplně stejně.

```py
for word_en, word_cz in slovnik.items():
    print(f"Slovo {word_cz} přeložíme jako {word_en}.")
```

Takto bude vypadat uložení při prvním průchodu.

![](assets/Cyklus-Slovnik_items-1-alt.drawio)

### Seznam slovníků

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

Dále chceme zjistit, kolik učebnic bylo v roce 2022 prodáno celkem.

#### Řešení úlohy v SQL

*Poznámka: Pokud jazyk SQL neznáš, můžeš tuto část přeskočit.*

Uvažujme, jak bychom řešili příklad v SQL. Tento příklad je založený na tom, že říkáme, jaký by měl být výsledek. Jinak řečeno, říkáme, *co chceme*. Neříkáme, jakým způsobem by měl počítač k požadovanému výsledku dojít.

```sql
SELECT mesto
FROM prodej_knih
WHERE rok2 < rok1;

SELECT SUM(rok2)
FROM prodej_knih;
```

#### Řešení úlohy v Pythonu

V Pythonu s využitím cyklu říkáme, co má počítač udělat, tj. dáváme mu posloupnost kroků, kterou má provést, aby dospěl k námi požadovanému výsledku. Instrukce, které počítači dáme, jsou následující:

1. Projdi jednotlivé prvky seznamu (projdi tabulku řádek po řádku).
1. Pro každý prvek (slovník) se podívej, jestli je hodnota s klíčem `"prodej_2021"` větší než hodnota s klíčem `"prodej_2022"`.
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

prodej_2022 = 0
for radek in prodej_knih:
    if radek["prodej_2021"] > radek["prodej_2022"]:
        print(radek["mesto"])
    prodej_2022 += radek["prodej_2022"]
print(f"Celkem bylo v roce prodáno {prodej_2022} učebnic.")
```

Níže je výstup, který kód vypíše na obrazovku.

```
Brno
Ostrava
Plzeň
Liberec
Olomouc
```

##### První opakování cyklu

Python do proměnné `radek` vloží to, co je na začátku seznamu, tj. prodeje v Praze. To, že jde o proměnnou `radek`, určíme tím, že název `radek` vložíme mezi `for` a `in`.

```py
for radek in prodej_knih:
```

![](assets/Cyklus-prubeh_slovnik_1.drawio.svg)

Nyní je vyhodnocená podmínka

```py
    if radek["prodej_2021"] > radek["prodej_2022"]:
```

Hodnota `radek["prodej_2021"]` je 4200 a hodnota `radek["prodej_2022"]` je 4900. Není tedy pravda, že je hodnota `radek["prodej_2021"]` větší než hodnota na pozici `radek["prodej_2022"]`, proto nespouštíme kód uvnitř podmínky.

Dále máme v cyklu příkaz pro přičtení prodejů do proměnné `prodej_2022`.

```py
    prodej_2022 += radek["prodej_2022"]
```

Tento příkaz je **mimo** podmínku, tím pádem ho Python spustí a hodnota proměnné `prodej_2022` s zvýší z 0 na 4900.

##### Druhé opakování cyklu

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

Hodnota proměnné `prodej_2022` se zvýší z 4900 na 4900 + 2100 = 7000.


##### Třetí opakování cyklu

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

Hodnota proměnné `prodej_2022` se zvýší ze 7000 na 7000 + 1100 = 8100.

##### Čtvrté opakování cyklu

Python do proměnné `radek` vloží další hodnotu ze seznamu, tj. prodeje v Plzni.

![](assets/Cyklus-prubeh_slovnik_4.drawio.svg)

Podmínka je opět splněná. Hodnota proměnné `prodej_2022` se zvýší ze 8100 na 8100 + 700 = 8800.

##### Páté opakování cyklu

Python do proměnné `radek` vloží další hodnotu ze seznamu, tj. prodeje v Liberci.

![](assets/Cyklus-prubeh_slovnik_5.drawio.svg)

Podmínka je opět splněná. Hodnota proměnné `prodej_2022` se zvýší ze 8800 na 8800 + 500 = 9300.

##### Šesté opakování cyklu

Python do proměnné `radek` vloží další hodnotu ze seznamu, tj. prodeje v Olomouci.

![](assets/Cyklus-prubeh_slovnik_6.drawio.svg)

Podmínka je opět splněná. Hodnota proměnné `prodej_2022` se zvýší ze 9300 na 9300 + 300 = 9600.

##### Výpis počtu prodaných učebnic

Teprve nyní Python opustí cyklus a pokračuje posledním příkazem. Ten vypíše hodnotu proměnné `prodej_2022`

```py
print(f"Celkem bylo v roce prodáno {prodej_2022} učebnic.")
```

Posledním výstupem programu bude:

```
Celkem bylo v roce prodáno 9600 učebnic.
```
