## Různé přístupy k ošetřování chyb

Ještě než se pustíme do samotného ošetřování výjimek, povíme si něco o ošetřování vstupů programu. Pokud totiž program nemá žádné vstupy "zvenku", není příliš univerzální. Takový program by se choval vždy stejně a vypsal by jen to, co jsme mu zadrátovali uvnitř (např. text "Hello world!").

Důležité je si pod pojmem vstup programu představit mnoho různých věcí, např.:

* Návratovou hodnotu funkce `input()` - vstup textu z klávesnice
* Parametry předané programu přes příkazovou řádku(`sys.argv`)
* Data z načítaného souboru
* Data stažená přes internet z API nebo webové stránky
* Formuláře na webové stránce (viz [xkcd komix](https://xkcd.com/327/))
* Posloupnost klikání na tlačítka a jiné prvky u GUI aplikací

Všechny tyto vstupy mohou způsobit v našem programu chyby, kterým se vždy musíme snažit předejít. K tomu se používají dva hlavní přístupy.

### Nejprve otestuj a pak proveď

Uvažujme, že chceme převést uživatelský vstup na číslo. U tohoto přístupu nejprve ověříme, že vstup obsahuje pouze číslice, a to například s využitím metody `.isdigit()`. Tato metoda vrátí `True`, pokud jsou v řetězci pouze čísla, v opačném případě vrátí `False`. V našem programu tedy řetězec zkontrolujeme a pokud obsahuje jiné znaky než číslice, ukončíme program pomocí funkce `exit()`. Řádek převodem řetězce na číslo bude tedy spuštěn pouze v případě, že řetězec obsahuje pouze čísla a tím pádem probehne korektně.

```py
import sys

vek = input("Zadej věk: ")
if not vek.isdigit():
    print("Je třeba zadat číslo!")
    sys.exit()
vek = int(vek)
if vek > 15:
    print("Vítej")
else:
    print("Představení je až od 15 let.")
```

Tento přístup se v angličtině označuje slovy *Look Before You Leap (LBYL)*.


### Proveď a řeš až problémy

Protože provedení všech potřebných kontrol by bylo v řadě případů příliš komplikované, byl v mnoha programovacích jazycích vytvořen mechanismus obsluhy výjimek. Kromě Pythonu jsou to např. jazyky C++, Java nebo C#. Slouží  k tomu nová klíčová slova `try` a `except`. Kus kódu, ve kterém může dojít k chybě, "obalíme" blokem `try`. Za tím to blokem _odchytíme_ příslušnou chybu v bloku `except`. Předchozí příklad přepíšeme následujícím způsobem:

```python
try:
    vek = input("Zadej věk: ")
    vek = int(vek) # Zde se pokoušíme o převod
    if vek > 15:
        print("Vítej")
    else:
        print("Představení je až od 15 let.")
except ValueError:  # Zde odchytáváme chybu při převodu
    print("Je třeba zadat číslo!")
```

Pokud by program získal vstup, který není možné převést na číslo, funkce `int()` vyvolá chybu `ValueError`. Protože ale máme v programu blok `except ValueError`, nedojde k ukončení programu neošetřenou chybou. Namísto toho program provede kód, který je v bloku `except ValueError` a může dále pokračovat. V případě ošetření výjimky totiž Python předpokládá, že problémy, které mohlo chybné zadání způsobit, jsou již v tomto bloku ošetřeny a program může pokračovat dále.

Tento přístup se v angličtině označuje slovy *Easier to Ask Forgiveness Than Permission (EAFP)* a za jeho úvodní autorku je označována admirálka [Grace Hopper](https://en.wikipedia.org/wiki/Grace_Hopper).

V reálném životě samozřejmě můžeme kombinovat oba přístupy, tj. známé komplikace ošetříme pomocí předběžných kontrol, ale doplníme i ošetření výjimek pro případ dalších chyb.

## Cvičení

::exc[excs/deleni]
::exc[excs/knihy]

### Bonusy

::exc[excs/datum]
