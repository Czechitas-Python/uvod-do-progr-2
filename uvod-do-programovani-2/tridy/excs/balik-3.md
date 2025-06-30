---
title: Balík potřetí
demand: 1
---

Vrať se k návrhu software pro zásilkovou společnost. U třídy `Package` uprav atribut `state` tak, aby byl chráněný. Ověř, že vytváření objektů i výpisy informací o něm fungují.

Pokud nemáš vytvořenou třídu `Package` z předchozí části, můžeš použít kód níže.

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
    
    def deliver(self):
        if self.state == "doručen":
            return "Balík již byl doručen"
        else:
            self.state = "doručen"
            return "Doručení uloženo"

    def __str__(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}."
    

package_1 = Package("Krakovská 583/9, Praha", 0.25, "nedoručen")
package_2 = Package("Pernerova 702/39, Praha", 12.47, "nedoručen")
print(package_1)
print(package_1.deliver())
print(package_1)
print(package_1.deliver())
```

:::solution
```py
class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self._state = state
    
    def delivery_price(self):
        if self.weight < 10:
            return 129
        if self.weight < 20:
            return 159
        return 359
    
    def deliver(self):
        if self._state == "doručen":
            return "Balík již byl doručen"
        else:
            self._state = "doručen"
            return "Doručení uloženo"

    def __str__(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self._state}."
    

package_1 = Package("Krakovská 583/9, Praha", 0.25, "nedoručen")
package_2 = Package("Pernerova 702/39, Praha", 12.47, "nedoručen")
print(package_1)
print(package_1.deliver())
print(package_1)
print(package_1.deliver())
```
:::
