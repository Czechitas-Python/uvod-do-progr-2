## Čtení na doma: Dvojité podtržítko a nepovinné parametry

V této části si vysvětlíme dva pojmy, se kterými se v rámci objektově orientovaného programování setkáte.

### Dvojité podtržítko

Dvojité podtržení z jedné strany u atributu nebo metody má svůj význam, a překvapivě docela jiný než dvojité podržítko z obou stran jména metody. Jde o soukromé atributy a metody, které navíc "zdědí" jméno své třídy. Tím dává vývojář nebo vývojářka třídy najevo, že tato by opravdu za žádných okolností neměla být volána zvenku.

Atribut `__holiday_entitlement` ze třídy `Employee` se po spuštění pro veřejnost přemění na `_Employee__holiday_entitlement` a pro svou instanci zůstane jako `__holiday_entitlement`. Díky tomuto nedojde v dědící třídě k přejmenování pomocných funkcí, které jsou zásadní pro fungování ostatních funkcí. I tyto funkce se nezobrazí po dosazení třídy nebo instance do napovídající funkce `help`.

```python
class Employee:
    def __init__(self, name, position, holiday_entitlement):
        self.name = name
        self.position = position
        self.__holiday_entitlement = holiday_entitlement
    
    def __str__(self):
        return f"Zaměstnanec {self.name} pracuje na pozici {self.position}."

    def take_holiday(self, days):
        if self.__holiday_entitlement >= days:
            self.__holiday_entitlement -= days
            return f"Užij si to."
        else:
            return f"Bohužel už máš nárok jen na {self.__holiday_entitlement} dní."

frantisek = Employee("František Novák", "konstruktér", 25)
print(str(frantisek))

# print(frantisek.__holiday_entitlement) # chyba
print(frantisek._Employee__holiday_entitlement)
```

Opět je třeba zdůraznit, že Python je poměrně specifický v tom, že nemá opravdu soukromé atributy. Většina programovacích jazyků rozlišuje mezi veřejnými (`public`) a soukromými (`private`) atributy a neexistuje žádný "trik", jak s nimi pracovat mimo metody dané třídy.

### Nepovinné parametry

Nyní uvažujme, že chceme evidovat nějakou další informaci, například registrační značku (`car_license_plate`) služebního auta. Uvažujme, že většina zaměstnanců a zaměstnankyň služební auto nemá. Pokud auto nemá, použijeme prázdnou hodnotu, kterou v Pythnu označujeme jako `None`. Abychom si ušetřili práci, můžeme nastavit parametr `license_plate` u metody `__init__()` jako nepovinný. To uděláme tak, že mu přiřadíme výchozí hodnotu. To samé nastavíme u parametru `holiday_entitlement`, protože i tam předpokládáme, že bude ve většině případů 25.

Při vytváření objektu pak můžeme zadat hodnoty pouze povinným parametrům. Pokud nezadáme hodnoty pro nepovinné parametry, jsou použity výchozí hodnoty.

```python
class Employee:
    def __init__(self, name, position, holiday_entitlement=25, car_license_plate=None):
        self.name = name
        self.position = position
        self.holiday_entitlement = holiday_entitlement
        self.car_license_plate = car_license_plate
    
    def __str__(self):
        text = f"Zaměstnanec {self.name} pracuje na pozici {self.position}."
        if self.car_license_plate:
            text += f" Má k dispozici služební auto {self.car_license_plate}."
        return text

    def take_holiday(self, days):
        if self.holiday_entitlement >= days:
            self.holiday_entitlement -= days
            return f"Užij si to."
        else:
            return f"Bohužel už máš nárok jen na {self.holiday_entitlement} dní."

frantisek = Employee("František Novák", "konstruktér")
print(str(frantisek))
print(frantisek.take_holiday(15))
print(frantisek.take_holiday(15))
```

Nyní uvažujme, že chceme přidat zaměstnankyni, která má služební auto, ale standardních 25 dní dovolené. Parametr `holiday_entitlement` můžeme přeskočit tak, že hodnotu parametru `car_license_plate` zadáme včetně názvu. Název je nutný, protože kdybychom zadali pouze registrační značku, Python by ji uložil do atributu `holiday_entitlement`. Při volání metody `take_holiday` by poté program skončil chybou.

```py
# Toto není správně, protože hodnota "1P7 4774" by se uložila do atributu holiday_entitlement
# natalie = Employee("Natálie Novotná", "sales manažerka", "1P7 4774")
# Toto je správně, "1P7 4774" se uloží do atributu car_license_plate a pro atribut holiday_entitlement se použije výchozí hodnota
natalie = Employee("Natálie Novotná", "sales manažerka", car_license_plate="1P7 4774")
print(str(natalie))
print(natalie.take_holiday(15))
print(natalie.take_holiday(15))
```

Stejný zápis se jménem parametru můžeme použít pro volání libovolné metody, a to i v případě, že má pouze povinné parametry. Nemusíme pak dodržovat pořadí, ve kterém jsou parametry zadány v definici metody, a pro někoho může být takový kód i lépe čitelný, protože u hodnoty vidí název parametru. Pozor ale na to, že jakmile ve volání toto pojmenování využijeme pro nějaký parametr, musíme to využít i pro všechny následující.

```py
# Toto je špatně. Pojmenování musíme požít pro všechny hodnoty ve volání, které následující po první pojmenované hodnotě.
# natalie = Employee(name="Natálie Novotná", "sales manažerka", car_license_plate="1P7 4774")
# Toto je správně
natalie = Employee(name="Natálie Novotná", position="sales manažerka", car_license_plate="1P7 4774")
# Toto je též správně správně. Přidáme-li názvy parametrů, nemusíme dodržovat jejich pořadí
natalie = Employee(car_license_plate="1P7 4774", position="sales manažerka", name="Natálie Novotná")
print(str(natalie))
print(natalie.take_holiday(15))
print(natalie.take_holiday(15))
```
