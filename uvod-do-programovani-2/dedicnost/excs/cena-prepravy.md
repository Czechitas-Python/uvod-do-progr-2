---
title: Cena přepravy
demand: 3
---

Pokračuj ve své práci pro zásilkovou společnost. Společnost nově požaduje, aby náš software uměl dopočítat cenu přepravy balíku.

- U cenných balíků bude k ceně připočteno pojištění. Přidej ke třídě `ValuablePackage` metodu `delivery_price()`. Ta spočítá cenu přepravy s využitím metody mateřské třídy `Package`, kterou jsme vytvořili v předchozí lekci. K tomu připočte pojistné ve výši 5 % ceny balíku.

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
    
    def delivery_price(self):
        return super().delivery_price() + self.value * 0.05


package = Package("Krakovská 583/9, Praha", 0.25, "nedoručen")
valuable_package = ValuablePackage("Pernerova 702/39, Praha", 12.47, "nedoručen", 5000)
print(package.delivery_price())
print(valuable_package.delivery_price())
```
:::
