---
title: Cenný balík
demand: 3
---

Pokračuj ve své práci pro zásilkovou společnost. Společnost nově doručuje i cenné balíky, které mají zadanou určitou hodnotu.

- Vytvoř třídu `ValuablePackage`, která dědí od třídy `Package`. `ValuablePackage` má navíc atribut `value`, ostatní atributy dědí od třídy `Package`.
- Atribut `value` nastav pomocí funkce `__init__`. Ostatní parametry předej funkci `__init__` třídy `Package`.
- Přidej do výpisu informací o cenném balíku (metoda `__str__`) informaci o ceně balíku.
- Vytvoř si alespoň jeden objekt a zkus volání jeho metod. Současně si vytvoř "obyčejný" balík o zkontroluj, že u něj se nic nezměnilo.

Pokud nemáš třídu `Package` z minulé lekce, můžeš použít tento kód.

```py
class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state

    def __str__(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}."

    def delivery_price(self):
        if self.weight < 10:
            return 129
        elif self.weight < 20:
            return 159
        else:
            return 359
```


:::solution
```py
class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state

    def __str__(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}."

    def delivery_price(self):
        if self.weight < 10:
            return 129
        elif self.weight < 20:
            return 159
        else:
            return 359

class ValuablePackage(Package):
    def __init__(self, address, weight, state, value):
        super().__init__(address, weight, state)
        self.value = value

    def __str__(self):
        return f"{super().__str__()} Jeho hodnota je {self.value}."


package = Package("Krakovská 583/9, Praha", 0.25, "nedoručen")
valuable_package = ValuablePackage("Pernerova 702/39, Praha", 12.47, "nedoručen", 5000)
print(package)
print(valuable_package)
print(valuable_package.delivery_price())
```
:::
