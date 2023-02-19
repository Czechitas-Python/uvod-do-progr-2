## Zadání příkladu

V rámci této lekce si vyzkoušíme vyřešit příklad, ve kterém využijeme koncepty, které jsme si ukazovali v předchozích lekcích.

Zadání příkazu je následující:

Ze souboru [battles.tsv](assets/battles.tsv) si načti informace o bitvách, které se odehrály ve knižní sérii Písně ohně a ledu, jejímž autorem je spisovatel George R. R. Martin a podle níž byl natočen slavný seriál Hra o trůny. Naším úkolem je ze zadaných dat zjistit následující:

- Statistiku, kolikrát byl který rod v pozici útočníků. Výsledná data ulož do CSV souboru `attackers.csv`.
- Pokud je zadaná síla obou armád (sloupce `attacker_size` a `defender_size`, indexy sloupců jsou 17 a 18), vytvoř seznam bitev, kde slabší armáda zvítězila nad silnější (vítěze poznáš podle sloupce attacker_outcome, sloupec má index 13 a obsahuje hodnoty `win` a `loss`, do seznamu vlož název bitvy ze sloupce name, sloupec má index 0). Kolik takových bitev je?

Abychom příklad vyřešili, je potřeba postupně provést následující kroky:

- načíst soubor a uložit data do vhodné struktury,
- projít data řádek po řádku a pro každý řádek si uložit všechny útočících rody,
- vytvořenou strukturu zapsat do souboru.
