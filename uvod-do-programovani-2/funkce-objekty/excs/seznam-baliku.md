---
title: Celková hodnota balíků
demand: 3
---

Pokračuj ve své práci pro zásilkovou společnost. Společnost chce doplnit do aplikace funkci pro výpočet celkového hodnoty nákladu nějakého auta, aby pak (např. v případě nehody nebo krádeže) mohla snadno spočítat celkovou hodnotu cenných balíků v autě a předat informaci pojišťovně. Příklad je podobný bonusu na výpočet celkové hmotnosti z předchozí části, liší se ale v tom, že hodnotu mají pouze cenné balíky, zatímco hmotnost mají všechny balíky.

Níže je příklad balíků, které můžeš použít pro tvorbu svého programu.

```py
package_1 = ValuablePackage("Grimmauldovo náměstí 11", 1.9, "nedoručen", 5500)
package_2 = Package("Godrikův důl 47", 1.9, "nedoručen")
package_3 = ValuablePackage("Vydrník svatého Drába 13", 1.9, "nedoručen", 5500)
package_list = [package_1, package_2, package_3]
```

- Vytvoř si proměnnou `total_value`, do které si s využitím cyklu budeš ukládat celkovou hodnotu všech balíků. Na začátku bude mít hodnotu 0.
- Vytvoř cyklus, který projde seznam `package_list`.
- Vyber funkci, která je podle tebe nejvhodnější pro zajištění bezpečného čtení atributu `value`. Můžeš použít funkci `isinstance()`, `hasattr()` i `getattr()`. Přičti hodnotu balíku k proměnné `total_value`, aniž by program skončil chybou u objektu `package_2`.
- Na konci programu vypiš, jaká je celková hodnota balíků v autě.

Pokud nemáš naprogramované třídy `Package` a/nebo `ValuablePackage`, můžeš využít kód níže.

```py
class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state

    def get_info(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}."

class ValuablePackage(Package):
    def __init__(self, address, weight, state, value):
        super().__init__(address, weight, state)
        self.value = value

    def __str__(self):
        return super().__str__() +  f"Balík má hodnotu hodnotu {self.value} Kč."
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


package_1 = ValuablePackage("Grimmauldovo náměstí 11", 1.9, "nedoručen", 5500)
package_2 = Package("Godrikův důl 47", 1.9, "nedoručen")
package_3 = ValuablePackage("Vydrník svatého Drába 13", 1.9, "nedoručen", 5500)
package_list = [package_1, package_2, package_3]

total_value = 0

# Použití hasattr() pro bezpečné zjištění, zda balík má atribut 'value'
for package in package_list:
    if hasattr(package, 'value'):
        total_value += package.value
print(f"Celková hodnota cenných balíků v autě je {total_value} Kč.")

# Alternativní způsob s použitím isinstance()
total_value_alt = 0
for package in package_list:
    if isinstance(package, ValuablePackage):
        total_value_alt += package.value
print(f"Celková hodnota cenných balíků v autě (pomocí isinstance) je {total_value_alt} Kč.")

# Alternativní způsob s použitím getattr()
total_value_getattr = 0
for package in package_list:
    # getattr(objekt, atribut, výchozí_hodnota) - vrátí výchozí hodnotu, pokud atribut neexistuje
    package_value = getattr(package, 'value', 0)
    total_value_getattr += package_value

print(f"Celková hodnota cenných balíků v autě (pomocí getattr) je {total_value_getattr} Kč.")
```
:::
