## Datové třídy

Obsah metody `__init__` je příklad `boilerplate code`. Název se odkazuje na kovové štítky, které jsou umístěny na bojlerech. V programování to znamená kód, který se často opakuje bez nějakých velkých změn.

V Pythonu ve verzi 3.7 přibyly datové třídy (`dataclass`), které si obsah metody vytvoří samy. Do datové třídy pouze napíšeme seznam jejích atributů spolu s jejich typy hodnot. Můžeme přidat i výchozí hodnotu, jak je vidět u atributu `holiday_entitlement`

```py
from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    position: str
    holiday_entitlement: int = 25

    def take_holiday(self, days):
        if self.holiday_entitlement >= days:
            self.holiday_entitlement -= days
            return f"Užij si to."
        else:
            return f"Bohužel už máš nárok jen na {self.holiday_entitlement} dní."

    def __str__(self):
        return f"{self.name} pracuje na pozici {self.position}."

frantisek = Employee("František Novák", "konstruktér")
print(frantisek.take_holiday(5))
print(frantisek.take_holiday(15))
print(frantisek.take_holiday(10))
```

### Dědičnost

V datových třídách můžeme využívat i dědičnost. Potomek též musí mít `@dataclass`, ale atributy rodiče opakovat nemusíme. Komplikací jsou atributy s výchozí hodnotou u rodiče, v našem případě tedy `holiday_entitlement`. Situaci si výrazně zjednodušíme tím, že výchozí hodnotu odebereme. Poté bude bez problémů fungovat datová třída `Manager`.

```py
@dataclass
class Manager(Employee):
    subordinates: int
    car: str

    def __str__(self):
        return super().__str__() + f" Má {self.subordinates} podřízených."
```

## Cvičení: Datové třídy

::exc[excs/streamovaci-sluzba]
