---
title: Testy pro knihu
demand: 2
---

V jednom z předchozích cvičení jsi vytvořil třídu `Book`, která reprezentuje knihu. Třída má atributy `title`, `pages` a `price` a metody `get_info()` a `get_time_to_read()`.

```py
class Book:
    def __init__(self, title, pages, price):
        self.title = title
        self.pages = pages
        self.price = price

    def get_info(self):
        return f"Kniha {self.title} má {self.pages} stran a stojí {self.price} Kč."

    def get_time_to_read(self, page_minutes=4):
        return self.pages * page_minutes
```

Napiš unit testy pro tuto třídu. Vytvoř testovací třídu `TestGetTimeToRead` a v ní následující testy:

- `test_default_speed` - ověří, že pro knihu s 200 stránkami metoda vrátí 800 minut (při výchozí rychlosti 4 minuty na stránku).
- `test_custom_speed` - ověří, že pro knihu s 200 stránkami a rychlostí 2 minuty na stránku metoda vrátí 400 minut.

Dále vytvoř testovací třídu `TestGetInfo` a v ní následující testy:

- `test_contains_title` - ověří, že výstup metody `get_info()` obsahuje název knihy.
- `test_contains_price` - ověří, že výstup metody `get_info()` obsahuje cenu knihy.

:::solution
```py
from unittest import TestCase
from book import Book


class TestGetTimeToRead(TestCase):
    def test_default_speed(self):
        book = Book("Testovací kniha", 200, 299)
        self.assertEqual(book.get_time_to_read(), 800)

    def test_custom_speed(self):
        book = Book("Testovací kniha", 200, 299)
        self.assertEqual(book.get_time_to_read(2), 400)


class TestGetInfo(TestCase):
    def test_contains_title(self):
        book = Book("Pán prstenů", 1200, 599)
        self.assertIn("Pán prstenů", book.get_info())

    def test_contains_price(self):
        book = Book("Pán prstenů", 1200, 599)
        self.assertIn("599", book.get_info())
```
:::
