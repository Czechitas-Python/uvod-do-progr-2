## Dotazník JetBrains

Zatím jsme pracovali s daty z knižní fantasy série. Zkusme si teď něco z reálného světa - data z průzkumu Developer Ecosystem Survey 2024, který každý rok provádí firma JetBrains a který mapuje zvyky a preference vývojářů z celého světa. Průzkumu se zúčastnilo přes 23 000 respondentů. Data jsou volně ke stažení ze stránky [JetBrains Developer Ecosystem Survey 2024](https://www.jetbrains.com/lp/devecosystem-2024/).

Originální soubor s daty má přes 6 000 sloupců. Pro naši analýzu stačí dva: pohlaví respondenta a pořadí Pythonu v žebříčku nejpoužívanějších jazyků. Připravili jsme proto zmenšený soubor [jetbrains_2024.tsv](assets/jetbrains_2024.tsv) ve formátu TSV.

Nás bude zajímat otázka: **má Python větší zastoupení v TOP 3 jazycích u mužů, nebo u žen?**

Sloupec `gender` odpovídá otázce *"What is your gender?"* a obsahuje hodnoty `Male`, `Female`, `Non-binary, genderqueer, or gender non-conforming`, `Prefer not to say` nebo `Other`. Sloupec `python_rank` odpovídá otázce *"Please rank your primary programming languages by frequency of use."* - hodnota `1` znamená nejpoužívanější jazyk, `2` druhý nejpoužívanější, `3` třetí. Prázdný řetězec znamená, že Python v žebříčku respondenta vůbec není.

### Načtení dat

Soubor je ve formátu TSV, takže každý řádek rozdělíme metodou `split("\t")`. První řádek je hlavička - přeskočíme ho pomocí `readlines()[1:]`.

```py
with open("jetbrains_2024.tsv", encoding="utf-8") as soubor:
    radky = soubor.readlines()

SL_GENDER = 0
SL_RANK = 3
```

### Počítání podle pohlaví

Budeme procházet všechny řádky a u každého si poznamenáme pohlaví a to, zda má respondent Python na místě 1, 2 nebo 3.

```py
celkem = {}
python_top3 = {}

for radek in radky[1:]:
    sloupce = radek.rstrip("\n").split("\t")
    gender = sloupce[SL_GENDER]
    rank = sloupce[SL_RANK]

    celkem[gender] = celkem.get(gender, 0) + 1
    if rank in ("1", "2", "3"):
        python_top3[gender] = python_top3.get(gender, 0) + 1
```

Použijeme `.rstrip("\n")` místo `.strip()` - odstraníme pouze znak nového řádku na konci, ale tabulátory uvnitř řádku zachováme. Kdybychom použili `.strip()`, odstranilo by i koncový tabulátor u řádků, kde je poslední sloupec prázdný, a `split("\t")` by pak vrátil seznam s méně prvky, než očekáváme.

### Výpis výsledků

```py
for gender, c in sorted(celkem.items(), key=lambda x: -x[1]):
    podil = round(python_top3.get(gender, 0) / c * 100, 1)
    print(f"Skupina {gender}: Python v TOP 3 u {podil} % respondentů")
```

```shell
Skupina Male: Python v TOP 3 u 30.7 % respondentů
Skupina Female: Python v TOP 3 u 32.5 % respondentů
Skupina Prefer not to say: Python v TOP 3 u 34.2 % respondentů
Skupina Non-binary, genderqueer, or gender non-conforming: Python v TOP 3 u 39.0 % respondentů
Skupina : Python v TOP 3 u 33.3 % respondentů
Skupina Other: Python v TOP 3 u 21.4 % respondentů
```

Výsledek je překvapivý - ženy mají Python mezi svými třemi hlavními jazyky o něco častěji než muži (32,5 % vs. 30,7 %). Python tedy není jen jazyk, který ženy znají - je to jazyk, který aktivně používají jako jeden z primárních.

**Poznámka:** Procenta počítáme vždy z celku dané skupiny, ne z celkového počtu respondentů. Jinak bychom jen odráželi, že mužů je v průzkumu téměř šestnáctkrát více než žen, a nic bychom se o popularitě Pythonu nedozvěděli.

### Srovnání s SQL

Průzkum obsahuje 39 programovacích jazyků z otázky *"Which programming languages have you used in the last 12 months?"*, každý jako samostatný sloupec. Kdybychom chtěli zjistit, kolik respondentů používá každý jazyk, v SQL bychom museli napsat jeden blok pro každý jazyk ručně:

```sql
SELECT jazyk, COUNT(*) AS pocet
FROM (
    SELECT 'Python'     AS jazyk FROM jetbrains WHERE Python != ''
    UNION ALL
    SELECT 'Java'       AS jazyk FROM jetbrains WHERE Java != ''
    UNION ALL
    SELECT 'JavaScript' AS jazyk FROM jetbrains WHERE JavaScript != ''
    -- ... a dalších 36 jazyků stejným způsobem
) AS jazyky
GROUP BY jazyk
ORDER BY pocet DESC;
```

Přibyde nový jazyk v příštím průzkumu - dotaz je neúplný a ty to nepoznáš. Python přečte hlavičku souboru a seznam jazyků sestaví sám z dat. Pracujeme se souborem [jetbrains_jazyky.tsv](assets/jetbrains_jazyky.tsv), který obsahuje jeden sloupec pro každý jazyk.

```py
with open("jetbrains_jazyky.tsv", encoding="utf-8") as soubor:
    radky = soubor.readlines()

hlavicka = radky[0].rstrip("\n").split("\t")
pocty = {}

for radek in radky[1:]:
    sloupce = radek.rstrip("\n").split("\t")
    for i in range(len(hlavicka)):
        nazev = hlavicka[i]
        if sloupce[i]:
            pocty[nazev] = pocty.get(nazev, 0) + 1

def vrat_hodnotu(dvojice):
    return dvojice[1]

serazene = sorted(pocty.items(), key=vrat_hodnotu, reverse=True)

for poradi, (jazyk, pocet) in enumerate(serazene[:10], start=1):
    print(f"{poradi}. {jazyk}: {pocet}")
```

```shell
1. JavaScript: 14450
2. Python: 12786
3. HTML / CSS: 12366
4. SQL: 12159
5. Java: 10319
6. Shell scripting: 9754
7. TypeScript: 9688
8. C#: 7205
9. C++: 4900
10. PHP: 4525
```

Funkce `vrat_hodnotu` říká `sorted()`, podle které části dvojice má řadit - vrací druhý prvek, tedy počet respondentů. `reverse=True` zajistí sestupné pořadí. Zápis `[:10]` v hlavičce cyklu pak ze seřazeného seznamu vezme prvních deset položek.

Kód funguje stejně, ať má soubor 10 nebo 100 jazykových sloupců - seznam jazyků se vždy sestaví přímo z hlavičky souboru.
