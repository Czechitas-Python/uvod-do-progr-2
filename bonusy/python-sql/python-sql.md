## Python vs SQL — srovnávací tabulka

Níže najdeš srovnání nejčastěji používaných operací v Pythonu a SQL.

### Základy a datové typy

| Popis | Python | SQL (Snowflake) |
|---|---|---|
| Číslo | `42` | `42` |
| Text (řetězec) | `'Czechitas'` | `'Czechitas'` |
| Převod na typ hodnoty — číslo | `int('42')` | `CAST('42' AS INT)` nebo `'42'::INT` |
| Převod na typ hodnoty — text | `str(42)` | `CAST(42 AS VARCHAR)` nebo `42::VARCHAR` |
| Komentář | `# toto je komentář` | `-- toto je komentář` |
| Proměnná | `mesto = 'Praha'` | alias: `'Praha' AS mesto` |


### Text — práce s řetězci

Porovnání si ukážeme s využitím proměnných níže. V SQL bychom uvažovali stejně nazvané sloupce.

```python
pozdrav = 'ahoj'
nazev = 'Czechitas'
veta = 'ahoj svete'
ip = '127.0.0.1'
inzerat = 'Hledáme Python developera'
```

| Popis | Python | SQL (Snowflake) |
|---|---|---|
| Délka řetězce | `len(pozdrav)` → 4 | `LENGTH(pozdrav)` → 4 |
| Velká písmena | `pozdrav.upper()` | `UPPER(pozdrav)` |
| Malá písmena | `pozdrav.lower()` | `LOWER(pozdrav)` |
| Spojení řetězců | `nazev + ', ' + 'CZ'` | `nazev \|\| ', ' \|\| 'CZ'` nebo `CONCAT(nazev, ', ', 'CZ')` |
| Výřez — první 3 znaky | `nazev[:3]` → `'Cze'` | `SUBSTRING(nazev, 1, 3)` → `'Cze'` |
| Výřez — od 3. do 6. znaku | `nazev[2:6]` | `SUBSTRING(nazev, 3, 4)` |
| První znak | `nazev[0]` | `LEFT(nazev, 1)` nebo `SUBSTRING(nazev, 1, 1)` |
| Poslední 3 znaky | `nazev[-3:]` | `RIGHT(nazev, 3)` |
| Nahrazení textu | `veta.replace('svete', 'Czechitas')` | `REPLACE(veta, 'svete', 'Czechitas')` |
| Rozdělení textu | `ip.split('.')` | `SPLIT(ip, '.')` |
| Hledání podřetězce | `'Python' in inzerat` | `inzerat ILIKE '%Python%'` |
| Hledání podřetězce case insensitive | `'anti' in nazev.lower()` | `nazev ILIKE '%anti%'` |

**Pozor na indexování!** Python počítá od `0`, SQL počítá od `1`.
- `nazev[0]` = první písmeno v Pythonu
- `SUBSTRING(nazev, 1, 1)` = první písmeno v SQL


### Čísla — matematické funkce

Porovnání si ukážeme s využitím proměnných níže. V SQL bychom uvažovali stejně nazvané sloupce.

```python
cislo = 1.5
zaporne = -5
seznam = [3, 1, 4]
```

| Popis | Python | SQL (Snowflake) |
|---|---|---|
| Zaokrouhlení | `round(cislo)` | `ROUND(cislo)` |
| Vždy nahoru | `math.ceil(cislo)` | `CEIL(cislo)` |
| Vždy dolů | `math.floor(cislo)` | `FLOOR(cislo)` |
| Absolutní hodnota | `abs(zaporne)` | `ABS(zaporne)` |
| Minimum ze seznamu | `min(seznam)` | `MIN(sloupec)` |
| Maximum ze seznamu | `max(seznam)` | `MAX(sloupec)` |
| Součet | `sum(seznam)` | `SUM(sloupec)` |
| Průměr | `statistics.mean(seznam)` | `AVG(sloupec)` |
| Počet prvků | `len(seznam)` | `COUNT(*)` |

### Podmínky

| Popis | Python | SQL (Snowflake) |
|---|---|---|
| Rovná se | `a == b` | `a = b` |
| Nerovná se | `a != b` | `a <> b` nebo `a != b` |
| Větší než | `a > b` | `a > b` |
| Menší nebo rovno | `a <= b` | `a <= b` |
| A zároveň | `a > 0 and b > 0` | `a > 0 AND b > 0` |
| Nebo | `a > 0 or b > 0` | `a > 0 OR b > 0` |
| Jednoduchá podmínka | `if cena >= 500:` | `WHERE cena >= 500` |
| Je v seznamu | `mesto in ['Praha', 'Brno']` | `mesto IN ('Praha', 'Brno')` |
| Není v seznamu | `mesto not in ['Praha', 'Brno']` | `mesto NOT IN ('Praha', 'Brno')` |
| V rozsahu | `40 <= x <= 60` | `x BETWEEN 40 AND 60` |
| Chybí hodnota | `x is None` | `x IS NULL` |
| Hodnota existuje | `x is not None` | `x IS NOT NULL` |


### Filtrování a výběr dat

| Popis | Python | SQL (Snowflake) |
|---|---|---|
| Omezení počtu | `seznam[:10]` | `LIMIT 10` |
| Seřazení vzestupně | `sorted(seznam)` | `ORDER BY sloupec ASC` |
| Seřazení sestupně | `sorted(seznam, reverse=True)` | `ORDER BY sloupec DESC` |
| Unikátní hodnoty | `set(seznam)` | `SELECT DISTINCT sloupec` |
| Počet unikátních | `len(set(seznam))` | `COUNT(DISTINCT sloupec)` |
