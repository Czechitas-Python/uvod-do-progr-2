## Testování

Testování je proces, při kterém ověřujeme, že náš program funguje správně. I zkušení programátoři a programátorky dělají chyby a testování nám pomáhá tyto chyby odhalit dříve, než se dostanou k uživatelům. Bez testů se často stává, že opravou jedné chyby nechtěně způsobíme chybu jinou. Testy nám dávají jistotu, že úpravou jedné části programu nerozbijeme část jinou.

Existuje několik úrovní testování. My si představíme dvě základní. :term{cs="Unit testy" en="unit tests"} (jednotkové testy) testují jednotlivé malé části programu, nejčastěji jednu funkci. Ověřují, že funkce pro daný vstup vrací správný výstup. Například pokud máme funkci na výpočet ceny objednávky, unit test ověří, že pro konkrétní vstupní hodnoty vrací očekávanou cenu. Unit testy jsou rychlé, jednoduché na psaní a pokud selžou, snadno z nich poznáme, kde přesně je problém.

:term{cs="Integrační testy" en="integration tests"} ověřují, že jednotlivé části programu správně spolupracují. Například pokud máme funkci na výpočet ceny a funkci na vytvoření objednávky, integrační test ověří, že celý proces od vytvoření objednávky po výpočet ceny funguje dohromady. Integrační testy jsou složitější a pomalejší, ale zachycují chyby, které unit testy odhalit nedokážou.

V rámci tohoto kurzu se zaměříme na unit testy, protože jsou nejdůležitějším základem testování a dobře se hodí k testování funkcí, které už umíme psát.

### Unit testy v Pythonu

Pro psaní unit testů v Pythonu použijeme modul `unittest`, který je součástí standardní knihovny Pythonu, takže ho nemusíme instalovat.

Představme si, že pracujeme na projektu pro zásilkovou společnost. Náš projekt bude mít následující strukturu:

```
preprava/
├── package.py
└── test_package.py
```

Soubor `package.py` obsahuje náš hlavní kód s třídou. Soubor `test_package.py` obsahuje testy. Důležité je, že název souboru s testy začíná prefixem `test_`.

V souboru `package.py` budeme mít třídu `Package`, která reprezentuje balík. Třída má atributy `address` (adresa), `weight` (hmotnost) a `state` (stav doručení). Metoda `delivery_price()` vypočítá cenu přepravy na základě hmotnosti balíku a metoda `get_info()` vrátí informace o balíku jako řetězec.

```py
class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state

    def delivery_price(self):
        if self.weight < 10:
            return 129
        if self.weight < 20:
            return 159
        return 359

    def get_info(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}."
```

Nyní vytvoříme testy pro tuto třídu. V souboru `test_package.py` nejprve naimportujeme třídu `TestCase` z modulu `unittest` a třídu `Package` z modulu `package`. Poté napíšeme testovací třídu, která dědí z `unittest.TestCase`. Název třídy musí začínat prefixem `Test`. Jednotlivé testy jsou metody této třídy a jejich názvy musí začínat prefixem `test_`. Uvnitř každé testovací metody vytvoříme objekt třídy `Package` s konkrétními hodnotami a pomocí metody `self.assertEqual()` ověříme, že výsledek odpovídá tomu, co očekáváme. Metoda `assertEqual()` porovná dvě hodnoty a pokud se liší, test selže. Seskupení testů do třídy nám pomáhá udržet testy přehledné - testy pro jednu metodu máme pohromadě na jednom místě.

```py
from unittest import TestCase
from package import Package


class TestDeliveryPrice(TestCase):
    def test_light_package(self):
        package = Package("Krakovská 583/9, Praha", 0.25, "nedoručen")
        self.assertEqual(package.delivery_price(), 129)

    def test_medium_package(self):
        package = Package("Pernerova 702/39, Praha", 12.47, "nedoručen")
        self.assertEqual(package.delivery_price(), 159)

    def test_heavy_package(self):
        package = Package("Vinohradská 12, Praha", 25.0, "nedoručen")
        self.assertEqual(package.delivery_price(), 359)


class TestGetInfo(TestCase):
    def test_contains_address(self):
        package = Package("Krakovská 583/9, Praha", 0.25, "nedoručen")
        self.assertIn("Krakovská 583/9, Praha", package.get_info())

    def test_contains_weight(self):
        package = Package("Krakovská 583/9, Praha", 0.25, "nedoručen")
        self.assertIn("0.25", package.get_info())
```

Všimni si, že každá metoda má jako první parametr `self`, stejně jako je tomu u metod v jiných třídách v Pythonu. Díky dědění z `TestCase` máme k dispozici různé testovací metody, které voláme přes `self`. Metoda `assertEqual()` přijímá dva argumenty a ověří, že se rovnají. Metoda `assertIn()` ověří, že první argument je obsažen ve druhém - to se hodí například tehdy, když nechceme testovat přesnou podobu celého řetězce, ale jen to, že obsahuje důležité údaje.

### Spuštění testů

Testy můžeme spustit přímo pomocí Visual Studio Code. V levém panelu klikneme na tlačítko `Testing`.

::fig[]{src=assets/testovani_01.png}

Poté na tlačítko `Configure Python Tests`. Objeví se menu, kde vybereme možnost `unittest`.

::fig[]{src=assets/testovani_02.png}

Dále vybereme možnost `. Root directory`. Soubor s testy je totiž ve stejném adresáři jako testovaný soubor. V případě větších projektů je lepší vkládat testy do odděleného adresáře a ten poté zvolit v tomto kroku.

::fig[]{src=assets/testovani_03.png}

Dále určíme "styl" pojmenování souborů s testy. Protože náš soubor se jmenuje `test_package.py`, vybereme možnost `test_*.py`. Visual Studio Code nyní správně pozná, který soubor obsahuje testy.

::fig[]{src=assets/testovani_04.png}

Po ukončení nastavení se zobrazí hrozivá červená hláška. Ve skutečnosti jde ale pouze o žádost o restart Visual Studio Code.

::fig[]{src=assets/testovani_05.png}

Po restartu spusťme testy pomocí tlačítka `Run tests`. Pokud všechny testy proběhnou bez problémů, uvidíme zelené značky u všech testů.

::fig[]{src=assets/testovani_06.png}

Zkusme nyní testovanou metodu upravit tak, aby některý z testů skončil chybou. U metody `delivery_price` upravíme poslední vracenou hodnotu na `459`. Pro balíky, které mají alespoň 20 kilogramů, nyní metoda vrací hodnotu 459.

Očekáváme, že test `test_heavy_package` ze třídy `TestDeliveryPrice` skončí chybou, protože očekávaná hodnota 359 nebude odpovídat skutečně vrácené hodnotě 459. A po spuštění u testu skutečně vidíme červenou značku. Ostatní testy stále procházejí bez problémů, protože naše úprava je nijak neovlivní.

::fig[]{src=assets/testovani_07.png}

V detailech testu v terminálu vidíme vysvětlení, proč test skončil s výsledkem `FAILED`.

::fig[]{src=assets/testovani_08.png}

Pozor na to, že vedle `SUCCESS` a `FAIL` může být výsledek testu i `ERROR`. Při spuštění testu se totiž může objevit chyba, stejně jako při spuštění jakékoli jiné části programu.

### Cvičení

::exc[excs/testy-kniha]

### Bonusové cvičení

::exc[excs/testy-heslo]
