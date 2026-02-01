## Logování

Logování je důležitý nástroj pro diagnostiku a řešení problémů při vývoji programů. Většinou nemáme možnost sledovat přímo na obrazovce uživatelů, jak náš program používají. Když se vyskytne chyba nebo když potřebujeme analyzovat běh aplikace, často se obracíme k logům - záznamům, které aplikace vytváří během svého provozu.

Logování znamená zaznamenávání informací o operacích, které aplikace provádí, a o chybách, které nastaly. Záznamy pak můžeme použít pro ladění chyb, monitorování výkonu, auditování bezpečnosti a mnoho dalších účelů.

### Logování v Pythonu

Python obsahuje modul `logging`, který je možné pro logování použít. Chceme-li uložit nějakou zprávu, je potřeba pro ni vybrat :term{cs="úroveň" en="level"}. Přehled výchozích úrovení je v tabulce níže. Úrovně jsou seřazené od nejnižší po nejvyšší.

| Úroveň    | Stručný popis                                                        |
|-----------|-----------------------------------------------------------------------|
| DEBUG     | Pro detailní diagnostické informace během vývoje nebo ladění.        |
| INFO      | Potvrzující zprávy o běžném fungování aplikace.                       |
| WARNING   | Varování o možných problémech, které by mohly ovlivnit běh programu.  |
| ERROR     | Chybové události, které narušují některé operace aplikace.            |
| CRITICAL  | Velmi vážné problémy, které mohou vyžadovat okamžitou pozornost.      |

Úroveň zprávy určuje funkci, kterou použijeme pro zapsání logové zprávy. Výchozí úroveň logování je `WARNING`, tj. zprávy nižší úrovně jsou ignorovány. V řadě případů například máme jinou úroveň logování v produkčním a vývojovém prostředí. Ve vývojovém logujeme vše, abychom přesně sledovali, co se s aplikací děje. V produkčním prostředí pak obvykle stačí úroveň `INFO` nebo `WARNING`.

```py
import logging

logging.warning('Something bad happened.')
logging.debug('This is not important')
```

Výchozí formát pro logovací zprávy v Pythonu obsahuje úroveň logování, jméno zapisovatele zprávy (výchozí hodnota je `'root'`) a samotnou zprávu. Za je přehled důležitých proměnných, které můžeme do našich logovacích zpráv vložit.

- `%(name)s`: Název loggeru, který generuje logovací zprávu.
- `%(levelno)s`: Číselné označení úrovně logování (např. 10 pro DEBUG, 20 pro INFO, atd.).
- `%(levelname)s`: Textové označení úrovně logování (např. 'DEBUG', 'INFO').
- `%(pathname)s`: Plná cesta k souboru, ve kterém byl logger volán.
- `%(filename)s`: Název souboru, ve kterém byl logger volán.
- `%(module)s`: Název modulu, ve kterém byl logger volán.
- `%(funcName)s`: Název funkce/metody, ve které byl logger volán.
- `%(lineno)d`: Číslo řádku, na kterém byl logger volán.
- `%(asctime)s`: Časové razítko vytvoření logovací zprávy.
- `%(message)s`: Text logovací zprávy.
- `%(thread)d`: ID vlákna, ve kterém byl logger volán.
- `%(threadName)s`: Název vlákna, ve kterém byl logger volán.
- `%(process)d`: ID procesu, ve kterém byl logger volán.


Vyzkoušejme nyní nastavit logování zpráv od úrovně `DEBUG` a v jiném formátu. Písmeno za závorkou označuje typ hodnoty. Dále nastavíme ukládání do souboru `app.log`.

```py
logging.basicConfig(level=logging.DEBUG, filename="app.log", filemode="w", 
                    format="%(asctime)s - %(levelname)s - [%(filename)s:%(lineno)d] %(funcName)s(): %(message)s")
logging.warning('This will get logged to a file')
```

Toto nastavení pak generuje logovací zprávy ve formátu:

```
2024-03-31 21:48:59,329 - WARNING - [program.py:5] <module>(): This will get logged to a file
```

Pokud do logovací zprávy chceme vložit hdonotu nějaké proměnné, můžeme využít formátované řetězce.

### Bonusová cvičení

::exc[excs/kostky]
