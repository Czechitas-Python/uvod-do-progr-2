---
title: Streamovací služba
demand: 3
---

Uvažuj, že vyvíjíš software pro službu, která nabízí streamování videa. Služba nabízí dva typy pořadů - filmy a seriály. Firma chce evidovat, které filmy a seriály nabízí a jejich žánry. Dále chce u filmů evidovat délku a u seriálů počet episod a délku jedné episody.

- Vytvoř program, který bude obsahovat dvě datové třídy - `Movie` a `Series`.
- Třída `Movie` bude obsahovat atributy udávající název (`title`), žánr (`genre`) a délku (`runtime`).
- Třída `Series` bude obsahovat atributy udávající název (`title`), žánr (`genre`), počet epizod (`episode_count`) a délka epizody (`episode_runtime`).
- Všem třídám přidej metoda `__str__()`, která vypíše informace o položce, resp. o filmu a seriálu.

Pro naprogramování si vytvoř alespoň jeden objekt reprezentující film a seriál a ověr, že vše funguje.

### Uživatelé a uživatelky

Služba nyní eviduje uživatele uživatele a uživatelky, kteří službu využívají. Vytvoř datovou třídu `User`, která bude mít atributy `user_name` a `total_time`, který udává celkovou délku pořadů, které uživatel zhlédl. Uživatelské jméno získej jako parametr a délka sledování je na začátku 0.

Třídám `Serial` a `Film` přidej funkce `get_runtime()`, která vrátí celkovou délku filmu/seriálu (u seriálu je to počet episod násobený délkou jedné episody). Třídě `User` přidej metodu `record_time()`, která bude mít jeden parametr. Funkce zvýší atribut udávající celkovou délku sledování o zadaný parametr. Vytvoř objekt, který reprezentuje nějakého uživatele. Následně zkus uvažovat situaci, že uživatel zhlédne film a seriál, které jsi vytvořil(a) jako objekty. Uživateli připočti délky děl k délce sledování, využij k tomu metodu `get_runtime()` u objektu a seriálu, abys zjistil(a), kolik minut (nebo hodin) videa celkem uživatel zhlédl.

Nejjednodušší řešení je, pokud si u filmu/seriálu uložíš celkovou délku do pomocné proměnné a tuto pomocnou proměnnou potom předáš jako parametr metodu `record_time()`.

### Bonusová varianta

V pokročilejší variantě neeviduj pouze délku sledování ale i to, jaké pořady uživatel sledoval. Namísto délky sledování vytvoř atribut, který bude udávat zhlédnuté pořady (ideální pro tento účel je seznam). Dále přidej funkci `add_watched_item()`, která do seznamu zhlédnutých pořadů přidánovou položku. Dále vytvoř funkci `get_total_time()` pro uživatele, která projde položky v seznamu a vrátí celkovou délku všech pořadů, které uživatel zhlédl. Vytvoř si ukázkové objekty a ověř, že vše funguje.

:::solution
```py
from dataclasses import dataclass

@dataclass
class Movie:
    title: str
    genre: str
    runtime: int

    def __str__(self):
        return f"Film {self.title} (žánr {self.genre}) má {self.runtime} minut."
    
    def get_runtime(self):
        return self.runtime

@dataclass
class Series:
    title: str
    genre: str
    episode_count: int
    episode_runtime: int

    def __str__(self):
        return f"Film {self.title} (žánr {self.genre}) má {self.episode_count} epizod po {self.episode_runtime} minutách."
    
    def get_runtime(self):
        return self.episode_count * self.episode_runtime

@dataclass
class User:
    user_name: str
    total_time: int = 0

    def record_time(self, time):
        self.total_time = self.total_time + time

apollo_13 = Movie("Apollo 13", "historický", 140)
star_trek = Series("Star Trek: Deep Space Nine", "sci-fi", 173, 45)
jirka = User("jirka")
delka_apollo_13 = apollo_13.get_runtime()
jirka.record_time(delka_apollo_13)
delka_star_trek = star_trek.get_runtime()
jirka.record_time(delka_star_trek)
print(jirka.total_time)
```

Bonusová varianta je níže.

```py
from dataclasses import dataclass

@dataclass
class Movie:
    title: str
    genre: str
    runtime: int

    def __str__(self):
        return f"Film {self.title} (žánr {self.genre}) má {self.runtime} minut."
    
    def get_runtime(self):
        return self.runtime

@dataclass
class Series:
    title: str
    genre: str
    episode_count: int
    episode_runtime: int

    def __str__(self):
        return f"Film {self.title} (žánr {self.genre}) má {self.episode_count} epizod po {self.episode_runtime} minutách."
    
    def get_runtime(self):
        return self.episode_count * self.episode_runtime

@dataclass
class User:
    user_name: str
    watched_items: list

    def get_total_time(self):
        time = 0
        for item in self.watched_items:
            time = time + item.get_runtime()
        return time

    def add_watched_item(self, item):
        self.watched_items.append(item)


apollo_13 = Movie("Apollo 13", "historický", 140)
star_trek = Series("Star Trek: Deep Space Nine", "sci-fi", 173, 45)
jirka = User("jirka", [])
jirka.add_watched_item(apollo_13)
jirka.add_watched_item(star_trek)
print(jirka.get_total_time())
```
:::