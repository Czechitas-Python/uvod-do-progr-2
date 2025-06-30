## Funkce pro práci s objekty

### Funkce `isinstance()`

Často potřebujeme v programu zkontrolovat, zda nějaká funkce je objektem určité třídy. V opačném případě se může stát, že budeme volat metodu, kterou objekt vůbec nemá, protože pochází z jiné třídy, než jsme předpokládali. K tomu slouží funkce `isinstance()`. Ta ověří, zda je objekt založený na nějaké třídě, a vrátí pravdivostní hodnotu. Jako parametry funkce zadáváme objekt a třídu, u které prověřujeme, zda z ní projekt pochází.

Funkce `isinstance()` vrátí hodnnotu `True` i v případě, že objekt pochází z některého z potomků třídy, na které se ptáme. Například pokud bychom kontrolovali, zda objekt `marian` pochází ze třídy `Employee`, výsledkem je opět hodnota `True`.

```python
marian = Manager("Marian Přísný", "vedoucí konstrukčního oddělení", 25, 5, "Škoda Octavia 1.5 TSI")
# Podmínka bude vyhodnocena jako pravda
if isinstance(marian, Manager):
    print("Objekt pochází ze třídy Manager (nebo jejích potomků).")
else:
    print("Objekt nepochází ze třídy Manager (nebo jejích potomků).")

# Podmínka bude vyhodnocena jako pravda (třída Manager dědí od třídy Employee)
if isinstance(marian, Employee):
    print("Objekt pochází ze třídy Employee (nebo jejích potomků).")
else:
    print("Objekt nepochází ze třídy Employee (nebo jejích potomků).")
```

Naopak pro objekt `frantisek` vrácí funkce `isinstance()` hodnotu `False`, pokud bychom se ptali na třídu `Manager`.

```python
frantisek = Employee("František Novák", "konstruktér", 25)
# Podmínka bude vyhodnocena jako nepravda
if isinstance(frantisek, Manager):
    print("Objekt pochází ze třídy Manager (nebo jejích potomků).")
else:
    print("Objekt nepochází ze třídy Manager (nebo jejích potomků).")
```

Uvažujme nyní například, že naše firma pořádá školení leadershipu. Naším úkolem je připravit pozvánky, ty ale logicky budeme posílát pouze lidem, kteří mají nějaké podřízené.

```py
marian = Manager("Marian Přísný", "vedoucí konstrukčního oddělení", 25, 5, "Škoda Octavia 1.5 TSI")
marketa = Manager("Markéta Polková", "teamleader", 25, 12, "Škoda Octavia RS")
frantisek = Employee("František Novák", "konstruktér", 25)
employee_list = [marian, marketa, frantisek]

expected_people = 0

for item in employee_list:
    if isinstance(item, Manager):
        # Připravíme si pozvánku
        print(f"Pozvánka pro {item.name} na školení leadershipu.")
        # Započítáme si jednoho člověka navíc
        expected_people = expected_people + 1

print(f"Čekáme {expected_people} osob.")
```

### Funkce hasattr

Další funkce je funkce `hasattr()`. Ta nám umožňuje zkontrolovat, zda má nějaký objekt atribut nebo metodu daného jména. Přidejme si do našeho programu ještě jednu třídu, která se bude jmenovat `Salesman`. Tato třída reprezentuje zaměstnance (zaměstnankyni), která se zabývá prodejem. Všichni tito zaměstnanci potřebují služební auto, aby mohli jezdit na obchodní schůzky. Vytvoříme tedy třídu `Salesman`, která bude mít atribut `car` (stejně jako třída `Manager`), ale nebude mít atribut `subordinates`.

```py
class Salesman(Employee):
    def __init__(self, name, position, holiday_entitlement, car):
        # Volám metodu __init__() mateřské třídy
        super().__init__(name, position)
        self.car = car
```

Dvakrát do roka je u všech firemních aut nutné vyměnit pneumatiky (ze zemních na letní a naopak). Z toho důvodu potřebujeme získat seznam všech aut, která jsou ve firmě k dispozici. Chceme tedy vzít seznam všech zaměstnanců a u těch, kteří mají auta, chceme informace o autě vypsat. Vyzkoušejme následující kód.

```py
marian = Manager("Marian Přísný", "vedoucí konstrukčního oddělení", 25, 5, "Škoda Octavia 1.5 TSI")
marketa = Manager("Markéta Polková", "teamleader", 25, 12, "Škoda Octavia RS")
frantisek = Employee("František Novák", "konstruktér", 25)
jakub = Salesman("Jakub Čmelák", "business development manager", 25, "Škoda Octavia Scout")
employee_list = [marian, marketa, frantisek, jakub]

for item in employee_list:
    # Skončí chybou pro objekt frantisek
    print(item.car)
```

Ten bohužel skončí chybou `AttributeError`, protože objekt `frantisek` atribut `car` nemá. Mohli bychom samozřejmě použít metodu `isinstance()`, ale pak bychom tento kód museli upravit vždy, když do aplikace přidáme nějakou třídu, která atribut `car` bude mít? Místo toho můžeme podmínku nastavit tak, aby byla vyhodnocená jako pravdivá, pokud má objekt atribut `car`, aniž bychom kontrolovali, jaké třídy objekty je. K tomu můžeme využít funkce `hasattr()`, která vrátí `True`, pokud objekt atribut má, a `False`, pokud atribut nemá. V každém případě je použití této funkce "bezpečné", tj. program neskončí chybou.

```py
for item in employee_list:
    # Vyhodnoceno jako nepravda pro objekt frantisek
    if hasattr(item, "car"):
        print(item.car)
```

Nyní nám program vypíše informace o třech autech. V případě objektu `frantisek` funkce `hasattr()` vrátí `False`, tj. podmínka je vyhodnocená jako nepravda a "nebezpečný" řádek s výpisem informací o autě nebude spuštěný.

### Funkce getattr

Pro práci s atributy objektů v Pythonu můžeme také použít funkci `getattr()`. Tato funkce umožňuje získat hodnotu atributu objektu na základě jeho názvu. Pokud funkci zadáme dva parametry (objekt a název atributu), funguje jako tečková notace, tj. vrátí hodnotu požadovaného atributu (pokud ji má) nebo spustí chybu `AttributeError` (pokud objekt atribut nemá). Použití funkce `getattr()` je užitečné v situacích, kdy název atributu známe až za běhu programu a nemůžeme jej proto přímo zapsat do kódu. Tato flexibilita nám umožňuje psát obecnější a opakovaně použitelný kód.

```py
marian = Manager("Marian Přísný", "vedoucí konstrukčního oddělení", 25, 5, "Škoda Octavia 1.5 TSI")
atribut = input("Jaký atribut mám vypsat? ")

hodnota = getattr(marian, atribut)
print(hodnota)
```

Funkci `getattr()`ale můžeme volat i se třetím parametrem, který specifikuje výchozí hodnotu, jež se má vrátit v případě, že objekt zadaný atribut nemá (a program pokračuje bez chyby `AttributeError`).

```python
marian = Manager("Marian Přísný", "vedoucí konstrukčního oddělení", 25, 5, "Škoda Octavia 1.5 TSI")
auto = getattr(marian, "car", "Neznámé auto")
# Vypíše "Škoda Octavia 1.5 TSI"
print(auto)

frantisek = Employee("František Novák", "konstruktér", 25)
auto = getattr(frantisek, "car", "Neznámé auto")
# Vypíše "Nemá auto"
print(auto)
```

## Cvičení

::exc[excs/seznam-baliku]

## Bonus

::exc[excs/seznam-baliku-podruhe]
::exc[excs/vypraveci]
