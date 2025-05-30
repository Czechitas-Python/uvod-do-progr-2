## Výjímky

Uvažujme teď upravená data, která obsahují chybu.

```py
lines = [
    "2904,4",
    "7390,0",
    "6950,8",
    "3300,4",
    "10570,8",
    "1310,2",
    "9806,8"
]
```

```shell
    avg = int(total_sales) / int(hours)
          ~~~~~~~~~~~~~~~~~^~~~~~~~~~~~
ZeroDivisionError: division by zero
```

Pokusme se o chybě zjistit víc pomocí krokování. Umístíme break point na řádek, který vidíme v chybě.

::fig[]{src=assets/krokovani-10.png}

Pro první průběh cyklu vypadá vše v pořádku.

::fig[]{src=assets/krokovani-11.png}

Pro druhý běh už v proměnné `hours` vidíme 0, která je příčinou našeho problému.

::fig[]{src=assets/krokovani-12.png}

Abychom zabránili neřízenému pádu programu v případě takové chyby ve vstupních datech, můžeme si vybrat ze dvou přístupů:

- Před dělením zkontrolujeme, jestli číslo není 0.
- Dělení provedeme a v případnou chybu "odchytíme".

### Nejprve otestuj a pak proveď

V tomto případě nejprve zkontrolujeme, zda je proměnná `hours` větší než 0. Pokud není, vypíšeme chybu a dělení neprovádíme.

```py
lines = [
    "2904,4",
    "7390,0",
    "6950,8",
    "3300,4",
    "10570,8",
    "1310,2",
    "9806,8"
]

avg_sales = []
for line in lines:
    line = line.split(",")
    if int(line[1]) > 0:
        avg = int(line[0]) / int(line[1])
        avg_sales.append(avg)
    else:
        print("Údaj o délce směny je chybný.")

print(avg_sales)
```

Tento přístup se v angličtině označuje slovy *Look Before You Leap (LBYL)*.


### Proveď a řeš až problémy

Protože provedení všech potřebných kontrol by bylo v řadě případů příliš komplikované, byl v mnoha programovacích jazycích vytvořen mechanismus obsluhy výjimek. Kromě Pythonu jsou to např. jazyky C++, Java nebo C#. Slouží  k tomu nová klíčová slova `try` a `except`. Kus kódu, ve kterém může dojít k chybě, "obalíme" blokem `try`. Za tím to blokem _odchytíme_ příslušnou chybu v bloku `except`. Předchozí příklad přepíšeme následujícím způsobem:

```python
avg_sales = []
for line in lines:
    line = line.split(",")
    try:
        avg = int(line[0]) / int(line[1])
        avg_sales.append(avg)
    except ZeroDivisionError:
        print("Údaj o délce směny je chybný.")

print(avg_sales)
```

Protože máme v programu blok `except ZeroDivisionError`, nedojde k ukončení programu neošetřenou chybou. Namísto toho program provede kód, který je v bloku `except ZeroDivisionError` a může dále pokračovat. V případě ošetření výjimky totiž Python předpokládá, že problémy, které mohlo chybné zadání způsobit, jsou již v tomto bloku ošetřeny a program může pokračovat dále.

Tento přístup se v angličtině označuje slovy *Easier to Ask Forgiveness Than Permission (EAFP)* a za jeho úvodní autorku je označována admirálka [Grace Hopper](https://en.wikipedia.org/wiki/Grace_Hopper).

V reálném životě samozřejmě můžeme kombinovat oba přístupy, tj. známé komplikace ošetříme pomocí předběžných kontrol, ale doplníme i ošetření výjimek pro případ dalších chyb.

A jak vlastně proběhne odchycení výjimky? Při zpracovávání řádku s 0 se program nejprve dostane na řádek s dělením. Tento řádek ale vyvolá chybu `ZeroDivisionError`.

::fig[]{src=assets/krokovani-13.png}

Python správně najde blok `except ZeroDivisionError` a přejde k němu.

::fig[]{src=assets/krokovani-14.png}

Protože v tomto bloku je jeden příkaz, Python tento příkaz spustí.

::fig[]{src=assets/krokovani-15.png}


### Obecná výjimka

Ve vstupních datech může být více záludností. Podívej se na obsah souboru níže. Co tam ma nás číhá?

- Některé hodnoty nepůjdou převést na číslo
- V jednom případě údaj o délce směny chybí.
- Jeden řádek je úplně prázdný

```
lines = [
    "2904,4",
    "7390,0",
    "6950 (pršelo),8",
    "3300",
    "10570,8",
    "1310,2",
    ""
]
```

Pokud se spokojíme pouze s výpisem o chybě, můžeme namísto chyby `ZeroDivisionError` odchytávat obecnou chybu `Exception`. Tato obecná chyba odchytí další chyby, které se v programu můžou vyskytnout, tedy nejen `ZeroDivisionError`, ale i `ValueError`, `IndexError` a řadu dalších. Dokáže odchytit i chybu s neexistujícím souborem nebo nedostatečnými právy pro jeho čtení.

```py
avg_sales = []
for line in lines:
    try:
        line = line.split(",")
        avg = int(line[0]) / int(line[1])
        avg_sales.append(avg)
    except Exception:
        print("Údaj o délce směny je chybný.")
```


## Cvičení

::exc[excs/knihy]

### Bonusy

::exc[excs/knizni-serie]
