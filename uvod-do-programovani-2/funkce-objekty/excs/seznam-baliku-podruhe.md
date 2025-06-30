---
title: Celková hodnota balíků podruhé
demand: 3
---

Vedení společnosti si uvědomilo, že do hodnoty balíků v autě by se neměly započítávat balíky, které už byly doručeny, protože již byly předány příjemci a nebudou tedy ukradeny nebo zničeny. 

- Uprav kód, který vytváří balíky, aby byl jeden balík vytvořený ve stavu `doručen`.
- Uprav cyklus, aby započítal hodnotu pouze těch balíků, které jsou ve stavu `nedoručen`.

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


package_1 = ValuablePackage("Grimmauldovo náměstí 11", 1.9, "doručen", 5500)
package_2 = Package("Godrikův důl 47", 1.9, "nedoručen")
package_3 = ValuablePackage("Vydrník svatého Drába 13", 1.9, "nedoručen", 5500)
package_list = [package_1, package_2, package_3]

total_value = 0

# Použití hasattr() pro bezpečné zjištění, zda balík má atribut 'value'
for package in package_list:
    if hasattr(package, 'value') and package.state == "nedoručen":
        total_value += package.value
print(f"Celková hodnota cenných balíků v autě je {total_value} Kč.")

# Alternativní způsob s použitím isinstance()
total_value_alt = 0
for package in package_list:
    if isinstance(package, ValuablePackage) and package.state == "nedoručen":
        total_value_alt += package.value
print(f"Celková hodnota cenných balíků v autě (pomocí isinstance) je {total_value_alt} Kč.")

# Alternativní způsob s použitím getattr()
total_value_getattr = 0
for package in package_list:
    if package.state == "nedoručen":
        package_value = getattr(package, 'value', 0)
        total_value_getattr += package_value

print(f"Celková hodnota cenných balíků v autě (pomocí getattr) je {total_value_getattr} Kč.")
```

