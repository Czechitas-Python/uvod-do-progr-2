---
title: Kniha podruhé
demand: 4
---

Vrať se k práci se třídou `Book`. Pokud jsi ji nestihl(a) v minulé části vytvořit, vrať se nejprve k zadání příkladu na předchozí stránce a třídu si vytvoř.

- U knihy budeme chtít evidovat, kolik kusů bylo prodáno. Přidej atribut `sold`, jehož hodnotu bude možné nastavit v metodě `__init__()`. Dále přidej atribut `costs`, které představují náklady na jednu knihu (např. tisk, doprava do knihkupectví, podíl autora (autorky) atd.).
- Přidej metodu `profit()`, která vrátí celkový zisk z knihy. Zisk vypočti na základě vzorce: prodané kusy * (cena - náklady).
- Přidej metodu `rating()`, která vrátí hodnocení knihy na základě jejího zisku. Pokud bude zisk méně než 50 tisíc, vrať hodnotu "propadák". Pokud bude zisk mezi 50 tisíc a 500 tisíc, vrať hodnotu "průměr". Pokud bude vyšší než 500 tisíc, vrať hodnotu "bestseller".

Pokud nemáš naprogramovanou třídu `Book`, můžeš použít kód níže.

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

:::solution
```py
class Book:
    def __init__(self, title, pages, price, sold, costs):
        self.title = title
        self.pages = pages
        self.price = price
        self.sold = sold
        self.costs = costs

    def get_info(self):
        return f"Kniha {self.title} má {self.pages} stran a stojí {self.price} Kč."
    
    def get_time_to_read(self, page_minutes=4):
        return self.pages * page_minutes
    
    def profit(self):
        return (self.price - self.costs) * self.sold
    
    def rating(self):
        if self.profit() < 50000:
            return "propadák"
        elif self.profit() < 500000:
            return "průměr"
        else:
            return "bestseller"

book_1 = Book("Day of the Wipers", 528, 646, 340000, 260)
print(f"Zisk z prodeje knihy je {book_1.profit()} Kč.")
print(f"Kniha je {book_1.rating()}.")
```
:::
