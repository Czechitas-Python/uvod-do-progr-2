---
title: Auta
demand: 3
---

Vytvoř program pro evidenci aut malé autopůjčovny. Půjčovna má 2 automobily:

| Registrační značka | Značka a typ vozidla | Počet najetých kilometrů  |
| ------------- |-------------| -----:|
| 4A2 3020 | Peugeot 403 Cabrio | 47534 |
| 1P3 4747 | Škoda Octavia |   41253 |

Vytvoř třídu `Car`, která bude obsahovat informace o autech, které půjčovna nabízí. Třída bude mít tyto atributy:

- registrační značka automobilu,
- značka a typ vozidla,
- počet najetých kilometrů,
- informaci o tom, jestli je vozidlo aktuálně volné (pravdivostní hodnota -- `True` pokud je volné a `False` pokud je vypůjčené).

Vytvoř funkci `__init__` pro třídu `Car`. Registrační značku, značku a typ vozidla a počet kilometrů získej jako parametry funkce `__init__` a ulož je jako atributy objektu. Poslední atribut nastav jako `True`, tj. na začátku je vozidlo volné.

Vytvoř objekty, které reprezentují všechny automobily půjčovny.

### Půjčení auta

Třídě `Car` přidej metodu `rent_car()`, která nebude mít (kromě obligátního `self`) žádný parametr. Funkce zkontroluje, jestli je vozidlo aktuálně volné. Pokud je volné, změní hodnotu atributu, který určuje, zda je vozidlo půjčené, a vrátí text `"Potvrzuji zapůjčení vozidla"`. Pokud je vozidlo již půjčené, vrátí text `"Vozidlo není k dispozici"`.

Dále tříde `Car` přidej metodu `__str__()`, která vrátí informaci o vozidle (stačí registrační značka a značka a typ vozidla) jako řetězec.

Nakonec do programu (mimo třídu) napiš dotaz na uživatele, jakou značku si uživatel přeje půjčit. Uživatel může zadávat hodnoty `Peugeot` nebo `Škoda`. Jakmile si uživatel vybere značku, vypiš informaci o vozidle pomocí funkce `__str__()` a následně použij metodu `rent_car`.

Dotaz na uživatele a výpis výsledků si v programu zkopíruj, abys dokázala otestovat, že funkce nedovolí půjčit stejné auto dvakrát.

### Vrácení auta

Nyní to svého programu přidej metodu `return_car()`, která bude mít (krom obligátního `self`) 2 parametry, a to je stav tachometru při vrácení a počet dní, po které zákazník auto používal. Ulož stav tachometru do atributu objektu. Nastav vozidlo jako volné.

Dále v metodě vypočti cenu za půjčení. Cena je 400 Kč na den, pokud měl zákazník celkem auto méně než týden, a 300 Kč na den, pokud měl zákazník auto déle. Cena je stejná pro obě auta. Vlož cenu do nějakého informativního textu a ten vrať pomocí klíčového slova `return`.

Na konec programu (mimo třídu) přidej dotaz na uživatele, kolik kilometrů zákazník ujel a jak dlouho ho měl půjčené. Poté vypiš informaci o ceně.
