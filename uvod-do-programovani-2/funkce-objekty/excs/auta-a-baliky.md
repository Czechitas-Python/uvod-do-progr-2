---
title: Auta a balíky
demand: 2
---

U našich balíků budeme nově evidovat, který řidič(ka) balík doručuje. Díky tomu pak bude možné odeslat SMS zprávu s číslem řidiče (řidičky), aby mohli zákazníci v případě potřeby řidiče (řidičku) kontaktovat.

Vytvoř třídu `Driver`, která bude mít atributy `name` a `phone_number`. Dále uprav třídu `Package`. Třída bude mít nově atribut `driver`, ve kterém bude uložen(a) řidič(ka) doručující balík. Uprav i třídu `ValuablePackage`, aby v metodě `__init__()` předala hodnotu parametru `driver` metodě `__init__` rodičovské třídy. Přidej třídě `Package` metodu `send_message()`, která odešle zprávu s textem: "Dnes budeme doručovat váš balík. V případě potřeby kontaktujte řidiče na čísle: " Na konec zprávy doplň telefonní číslo.

:::solution
```py
class Driver:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

class Package:
    def __init__(self, address, weight, state, driver):
        self.address = address
        self.weight = weight
        self.state = state
        self.driver = driver

    def __str__(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} kg a je ve stavu {self.state}."

    def delivery_price(self):
        if self.weight < 10:
            return 129
        elif self.weight < 20:
            return 159
        else:
            return 359
    
    def send_message(self):
        return f"Dnes budeme doručovat váš balík. V případě potřeby kontaktujte řidiče na čísle: {self.driver.phone_number}"


class ValuablePackage(Package):
    def __init__(self, address, weight, state, value, driver):
        super().__init__(address, weight, state, driver)
        self.value = value

    def __str__(self):
        return super().__str__() + f" Balík má hodnotu {self.value} Kč."


driver_1 = Driver("Antonín Boháček", "+420 123 456 789")
driver_2 = Driver("Josef Novák", "+420 987 654 321")

package_1 = ValuablePackage("Grimmauldovo náměstí 11", 1.9, "nedoručen", 5500, driver_1)
package_2 = Package("Godrikův důl 47", 1.9, "nedoručen", driver_2)
package_3 = ValuablePackage("Vydrník svatého Drába 13", 1.9, "nedoručen", 5500, driver_1)


print(package_1.send_message())
print(package_2.send_message())
print(package_3.send_message())
```
:::
