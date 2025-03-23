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

## Cvičení: JSON
::exc[excs/zavod]
::exc[excs/transformace-dat]

## Bonus
::exc[excs/skolka]