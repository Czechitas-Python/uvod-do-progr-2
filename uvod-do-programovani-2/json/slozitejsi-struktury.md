## Složitější JSON struktury

Ve formátu JSON můžeme narazit i na složitější struktury. Uvažujme výsledky běžeckého závodu, které jsou uložené v souboru [zavod.json](assets/zavod.json). Struktura je složitější tím, že v sobě obsahuje zanořené slovníky. Data si nejprve uložíme do proměnné `runners`.

```py
import json
with open('zavod.json', encoding='utf-8') as file:
    runners = json.load(file)
```

Strukturu dat si můžeme pro přehlednost znázornit graficky. Obrázek v plné velikosti je [zde](assets/Indexovani-Slovnik1.drawio.svg).

::fig[Struktura slovníku v JSON]{src=assets/Indexovani-Slovnik1.drawio.svg}

Do proměnné `winner` si nyní načtěme informace o prvku seznamu na nulté pozici, což jsou data o vítězi závodu.

```py
winner = runners[0]
```

Obsah proměnné `winner` si opět můžeme zobrazit graficky.

::fig[Struktura slovníku v JSON]{src=assets/Indexovani-Slovnik2.drawio.svg}

I do této struktury se můžeme ponořit hlouběji. Pokud bychom chtěli například zjistit oficiální čas vítěze, napíšeme:

```py
winner_time = winner["casy"]["oficialni"]
```

### Další příklady JSON souborů

Podívejme se na ještě jeden příklad zápisu dat. Data reprezentují informace o konání kurzu Úvod do programování.

```json
{
    "nazev": "Úvod do programování",
    "lektor": "Martin Podloucký",
    "konani": [
        {
            "misto": "T-Mobile",
            "koucove": [
                "Dan Vrátil",
                "Filip Kopecký",
                "Martina Nemčoková"
            ],
            "ucastnic": 30
        },
        {
            "misto": "MSD IT",
            "koucove": [
                "Dan Vrátil",
                "Zuzana Tučková",
                "Martina Nemčoková"
            ],
            "ucastnic": 25
        },
        {
            "misto": "Škoda DigiLab",
            "koucove": [
                "Dan Vrátil",
                "Filip Kopecký",
                "Kateřina Kalášková"
            ],
            "ucastnic": 41
        }
    ]
}
```

Všimni si, jak obsah JSON souboru představující jeden kurz, obsahuje pod klíčem `konani` seznam dalších slovníků. Každý z nich reprezentuje jedno konání kurzu a dále obsahuje například seznam koučů atd.


## Cvičení: JSON
::exc[excs/zavod]
