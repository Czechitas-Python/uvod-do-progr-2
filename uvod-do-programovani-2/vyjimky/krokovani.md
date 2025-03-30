## Výjimky a krokování

Krokování je podobné práci videorozhodčích v hokeji, když sledují zpomalené záběry, aby zjistili, co se v nějaké nepřehledné situaci stalo. Krokování nám umožní zastavit běh programu na konkrétním místě a podívat se, jaké v tom okamžiku existují v programu proměnné a jaké jsou jejich hodnoty. Pokud máme program "zastavený", můžeme nechat spustit jen jeden nebo několik vybraných řádků a sledovat, co se během té doby změní.

Tato technika je důležitá především pro odstraňování chyb a neočekávaného chování programu. Vyzkoušejme si krokování při čtení souboru [smeny.txt](assets/smeny.txt).

```py
lines = []

with open("smeny.txt", encoding="utf-8") as file:
    for line in file:
        lines.append(line)

avg_sales = []
for line in lines:
    line = line.split(",")
    day, total_sales, hours = line
    avg = int(total_sales) / int(hours)
    avg_sales.append(avg)

print(avg_sales)
```

V programu umístímě tzv. break point, tj. místo, kde se má běh programu zastavit.

::fig[]{src=assets/krokovani-01.png}

Program tentokrát spustíme z menu.

::fig[]{src=assets/krokovani-02.png}

Vybereme možnost `Python Debugger`.

::fig[]{src=assets/krokovani-03.png}

A v posledním menu možnost `Python File`.

::fig[]{src=assets/krokovani-04.png}

Program na vybraném místě zastaví. V levém menu vidíme všechny aktuálně existující proměnné, jejich typy a hodnoty v nich uložené.

::fig[]{src=assets/krokovani-05.png}

Nyní se můžeme rozhodnout, co dál. Máme následující možnosti:

- Pokračovat, dokud Python nenarazí na další break point (volba `Continue`).
- Přejít na další řádek (volba `Step Over`).

::fig[]{src=assets/krokovani-06.png}

Použijme volbu `Step Over`, abychom se dostali na další řádek. V levém panelu vidíme změnu hodnoty proměnné `line`.

::fig[]{src=assets/krokovani-07.png}

Přejdeme-li o řádek dál, uvidíme dvě nové proměnné - `total_sales` a `hours`.

::fig[]{src=assets/krokovani-08.png}

Pokud použijeme volbu `Continue`, program se zastaví, až znovu narazí na náš break point. V proměnné `line` už vidíme druhý řádek souboru, v proměnných `total_sales` a `hours` jsou stále ještě "staré" hodnoty.

::fig[]{src=assets/krokovani-09.png}

