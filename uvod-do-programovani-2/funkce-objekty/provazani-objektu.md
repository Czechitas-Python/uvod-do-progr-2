## Provázání objektů

V reálných aplikacích často potřebujeme objekty mezi sebou provázat. V našem personálním systému by bylo užitečné provázat podřízené s jejich manažerem. To by usnadnilo některé procesy, například vytváření pracovní smlouvy a jejích dodatků, usnadní plánování meetingů atd. Nejprve přidejme třídě `Employee` atribut `manager` a nastavme ho v metodě `__init__`.

```py
class Employee:
    def __init__(self, name, position, holiday_entitlement, manager):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement
        self.manager = manager
    
    def __str__(self):
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}, přímým nadřízeným je {self.manager.name}"
```

Manažera pak můžeme přidat do výpisu, který poskytuje metoda `__str__()`.

```py
marian = Manager("Marian Přísný", "vedoucí konstrukčního oddělení", 25, 2, "Škoda Octavia")
klara = Employee("Klára Nová", "konstruktérka", 25, marian)
print(klara)
frantisek = Employee("František Novák", "konstruktér", 25, marian)
print(frantisek)
```

Jméno manažera získáme pomocí dvou teček, postupně se přes atribut `manager` dostaneme k atributu `name`.

```py
print(frantisek.manager.name)
```

### Cvičení

::exc[excs/auta-a-baliky]

### Čtení na doma: Provázání pomocí seznamu

Zaměstnance a objekty je možné provázat i obráceně, můžeme každému manažerovi vytvořit seznam jeho podřízených. K provázání objektů můžeme použít seznamy. Atribut `subordinates` nahradíme atributem `subordinates_list`, do kterého v metodě `__init__()` uložíme prázdný seznam. Tento seznam pak budeme plnit s využitím metody `add_subordinate()`. Metoda přijme nového zaměstnance jako parametr `subordinate` a pomocí metody `append()` ho vloží do seznamu `subordinates_list`. Dále přidáme metodu `get_subordinates()`, která vypíše jména všech podřízených ze seznamu `subordinates_list`.

```py
class Manager(Employee):
    def get_subordinates(self):
        for item in self.subordinates_list:
            print(item.name)

    def add_subordinate(self, subordinate):
        self.subordinates_list.append(subordinate)

    def __init__(self, name, position, holiday_entitlement, car):
        self.name = name
        self.position = position
        self._holiday_entitlement = holiday_entitlement
        self.subordinates_list = []
        self.car = car
```

Dále vytvoříme objekt reprezentující manažera a dva zaměstnance, kteří budou jeho podřízení. U manažera již nezadáváme počet podřízených jako číslo, oproti zaměstnanci je zde tedy navíc pouze služební auto.

```py
marian = Manager("Marian Přísný", "vedoucí konstrukčního oddělení", 25, "Škoda Octavia")
klara = Employee("Klára Nová", "konstruktérka", 25)
frantisek = Employee("František Novák", "konstruktér", 25)
```

Nyní přidáme podřízené do seznamu s využitím metody `add_subordinate()`.

```py
marian.add_subordinate(klara)
marian.add_subordinate(frantisek)
```

Nakonec můžeme podřízené vypsat s využitím metody `get_subordinates()`

```py
marian.get_subordinates()
```

```py
    def add_subordinate(self, subordinate):
        if isinstance(subordinate, Employee):
            self.subordinates_list.append(subordinate)
        else:
            print("Je třeba vložit objekt třídy Employee.")
```
