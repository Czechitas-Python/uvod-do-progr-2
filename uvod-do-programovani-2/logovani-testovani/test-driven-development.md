## Vývoj řízený testy (TDD)

:term{cs="Vývoj řízený testy" en="Test Driven Development"} (TDD) je přístup k vývoji softwaru, při kterém programátor nebo programátorka nejprve napíše test a teprve poté napíše kód, který tímto testem projde. Postup se opakuje v krátkých cyklech a skládá se ze tří kroků:

1. **Napiš test** (Red). Nejprve napíšeme test pro funkcionalitu, kterou chceme přidat. Test v tuto chvíli selže, protože funkce nebo metoda ještě neexistuje nebo nefunguje správně.
2. **Doplň kód** (Green). Napíšeme minimální množství kódu, které je potřeba k tomu, aby test prošel. Cílem není napsat dokonalé řešení, ale co nejjednodušší kód, který splní požadavek testu.
3. **Uprav kód** (Refactor). Po tom, co test projde, můžeme kód vylepšit, zjednodušit nebo zpřehlednit. Díky testům máme jistotu, že úpravou nic nerozbijeme.

Tento cyklus se neustále opakuje. S každým průchodem přidáváme nový test, rozšiřujeme funkcionalitu a vylepšujeme kód. Ukažme si celý postup na příkladu.

### Převod arabských čísel na římská

Vytvoříme třídu `RomanConverter`, která bude převádět arabská čísla na římská. Projekt bude mít dva soubory:

```
rimska-cisla/
├── roman_converter.py
└── test_roman_converter.py
```

#### Krok 1: Test pro číslo 1

Začneme tím, že napíšeme test. Chceme, aby naše třída uměla převést číslo 1 na řetězec `"I"`. V souboru `test_roman_converter.py` napíšeme:

```py
from unittest import TestCase
from roman_converter import RomanConverter


class TestRomanConverter(TestCase):
    def test_1(self):
        converter = RomanConverter()
        self.assertEqual(converter.convert(1), "I")
```

Soubor `roman_converter.py` zatím neexistuje, takže test selže. Vytvoříme ho s minimálním kódem, který je potřeba k tomu, aby test prošel:

```py
class RomanConverter:
    def convert(self, number):
        return "I"
```

Metoda jednoduše vrací `"I"`. To je naprosto v pořádku - v TDD píšeme jen tolik kódu, kolik je potřeba k tomu, aby aktuální testy prošly. Test nyní projde.

#### Krok 2: Testy pro čísla 2 a 3

Přidáme testy pro další čísla. Číslo 2 se v římských číslicích zapíše jako `"II"` a číslo 3 jako `"III"`.

```py
from unittest import TestCase
from roman_converter import RomanConverter


class TestRomanConverter(TestCase):
    def test_1(self):
        converter = RomanConverter()
        self.assertEqual(converter.convert(1), "I")

    def test_2(self):
        converter = RomanConverter()
        self.assertEqual(converter.convert(2), "II")

    def test_3(self):
        converter = RomanConverter()
        self.assertEqual(converter.convert(3), "III")
```

Nové testy selžou, protože metoda `convert()` vrací vždy `"I"`. Upravíme ji tak, aby prošly všechny testy:

```py
class RomanConverter:
    def convert(self, number):
        return "I" * number
```

Čísla 1, 2 a 3 se v římských číslicích zapisují jako opakování znaku `"I"`. Stačí nám tedy vynásobit řetězec `"I"` hodnotou `number`. Všechny tři testy nyní projdou.

