---
title: Zranitelnosti
demand: 4
---

Bezpečnostní analytik má k dispozici dva seznamy:

1. **Seznam zranitelností** (`vulnerabilities`) — pro každou zranitelnost je uveden její identifikátor CVE, název zranitelného produktu a seznam rozsahů verzí, kterých se zranitelnost týká. Zranitelnost se týká verze, pokud leží v libovolném z uvedených rozsahů (včetně krajních hodnot). Rozsah může mít pouze `high_range` bez `low_range` — to znamená, že zranitelnost se týká všech verzí až po danou verzi.

2. **Seznam počítačů** (`computers`) — pro každý počítač je uveden jeho název a seznam nainstalovaného softwaru s verzemi.

```py
vulnerabilities = [
    {
        "cve": "CVE-2023-2136",
        "product_name": "Google Chrome",
        "version_ranges": [
            {"low_range": "120.0.0", "high_range": "120.0.5615"},
        ],
    },
    {
        "cve": "CVE-2023-4863",
        "product_name": "Google Chrome",
        "version_ranges": [
            {"low_range": "119.0.0", "high_range": "119.0.6099"},
        ],
    },
    {
        "cve": "CVE-2023-21608",
        "product_name": "Adobe Acrobat Reader",
        "version_ranges": [
            {"low_range": "20.0.0", "high_range": "20.5.9"},
            {"low_range": "22.0.0", "high_range": "22.3.9"},
        ],
    },
    {
        "cve": "CVE-2024-20656",
        "product_name": "VLC Media Player",
        "version_ranges": [
            {"low_range": "3.0.0", "high_range": "3.0.9"},
        ],
    },
    {
        "cve": "CVE-2022-41325",
        "product_name": "VLC Media Player",
        "version_ranges": [
            {"high_range": "3.0.17"},
            {"low_range": "4.0.0", "high_range": "4.0.3"},
        ],
    },
]

computers = [
    {
        "computer_name": "maria",
        "installed_software": [
            {"software": "Google Chrome", "version": "119.0.5790"},
            {"software": "Adobe Acrobat Reader", "version": "23.1.4"},
            {"software": "VLC Media Player", "version": "3.0.8"},
        ],
    },
    {
        "computer_name": "jakub",
        "installed_software": [
            {"software": "Microsoft Edge", "version": "124.0.2478"},
            {"software": "Adobe Acrobat Reader", "version": "22.3.0"},
            {"software": "Google Chrome", "version": "120.0.6099"},
        ],
    },
    {
        "computer_name": "anna",
        "installed_software": [
            {"software": "Google Chrome", "version": "120.0.4745"},
            {"software": "VLC Media Player", "version": "4.0.1"},
        ],
    },
    {
        "computer_name": "petra",
        "installed_software": [
            {"software": "Microsoft Edge", "version": "121.0.2277"},
            {"software": "Adobe Acrobat Reader", "version": "20.4.3"},
            {"software": "VLC Media Player", "version": "3.1.1"},
        ],
    },
]
```

Napiš program, který vytvoří report ve formě seznamu slovníků. Každý slovník bude obsahovat název počítače a seznam CVE identifikátorů zranitelností, které se ho týkají.

Verze softwaru se často zapisují ve formátu **sémantického verzování** — například `124.0.5735`. Číslo se skládá ze tří částí oddělených tečkou:

- **major** (`124`) — mění se při velkých změnách, které nejsou zpětně kompatibilní,
- **minor** (`0`) — mění se při přidání nových funkcí při zachování zpětné kompatibility,
- **patch** (`5735`) — mění se při opravě chyb.

Při porovnávání dvou verzí nestačí porovnat celý řetězec jako text — Python by například vyhodnotil `"9.0.0" > "10.0.0"`, protože porovnává znak po znaku a `"9" > "1"`. Správný postup je rozdělit verzi na části pomocí metody `split()`, převést je na celá čísla a porovnat jako seznam čísel.

Porovnávání seznamů v Pythonu funguje prvek po prvku — nejprve se porovná major, při shodě minor, při shodě patch.

Např. máme zranitelnost Google Chrome s rozsahem `120.0.0` až `120.0.5615`. Počítač `maria` není zranitelný, protože má starší verzi `119.0.5790`. Počítač `jakub` není zranitelý, protože má novější verzi `120.0.6099`. Počítač `anna` je zranitelný, protože verze Google Chrome `120.0.4745` se nachází ve specifikovaném rozsahu. Počítač `petra` nemá Google Chrome nainstalovaný vůbec, takže není zranitelný.
