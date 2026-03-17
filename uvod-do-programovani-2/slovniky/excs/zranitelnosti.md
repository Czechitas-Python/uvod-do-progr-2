---
title: Zranitelnosti
demand: 4
---

Bezpečnostní analytik má k dispozici dva seznamy:

1. **Seznam zranitelností** (`vulnerabilities`) — pro každou zranitelnost je uveden její identifikátor CVE, název zranitelného produktu a seznam rozsahů verzí, kterých se zranitelnost týká. Zranitelnost se týká verze, pokud leží v libovolném z uvedených rozsahů (včetně krajních hodnot).

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
            {"low_range": "1.0.0", "high_range": "3.0.17"},
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

Pro řešení můžeš využít porovnávání seznamů. Porovnávání seznamů v Pythonu funguje prvek po prvku — nejprve se porovná první prvek, při shodě druhý, při shodě třetí. Například:

- `[119, 0, 5790] < [120, 0, 0]` — první prvky se liší (`119 < 120`), výsledek je ihned znám.
- `[120, 0, 4745] < [120, 0, 5615]` — první prvky jsou shodné (`120 == 120`), porovnají se druhé (`0 == 0`), pak třetí (`4745 < 5615`).

Pro verze tedy stačí převést řetězce na seznamy celých čísel a porovnat je přímo.

Např. máme zranitelnost Google Chrome s rozsahem `120.0.0` až `120.0.5615`. Počítač `maria` není zranitelný, protože má starší verzi `119.0.5790`. Počítač `jakub` není zranitelý, protože má novější verzi `120.0.6099`. Počítač `anna` je zranitelný, protože verze Google Chrome `120.0.4745` se nachází ve specifikovaném rozsahu. Počítač `petra` nemá Google Chrome nainstalovaný vůbec, takže není zranitelný.

Výstup tvého kódu by měl vypadat takto:

```
{'maria': ['CVE-2023-4863', 'CVE-2024-20656', 'CVE-2022-41325'], 'jakub': ['CVE-2023-21608'], 'anna': ['CVE-2023-2136', 'CVE-2022-41325'], 'petra': ['CVE-2023-21608']}
```

:::solution

```py
computers_vulnerability = {}
for computer in computers:
    for software in computer["installed_software"]:
        for vulnerability in vulnerabilities:
            if software["software"] == vulnerability["product_name"]:
                for version in vulnerability["version_ranges"]:
                    vulnerability_high_range = version["high_range"].split(".")
                    installed_version = software["version"].split(".")
                    vulnerability_low_range = version["low_range"].split(".")
                    low = [int(vulnerability_low_range[0]), int(vulnerability_low_range[1]), int(vulnerability_low_range[2])]
                    high = [int(vulnerability_high_range[0]), int(vulnerability_high_range[1]), int(vulnerability_high_range[2])]
                    installed = [int(installed_version[0]), int(installed_version[1]), int(installed_version[2])]
                    if low <= installed <= high:
                        if computer["computer_name"] not in computers_vulnerability:
                            computers_vulnerability[computer["computer_name"]] = []
                        computers_vulnerability[computer["computer_name"]].append(vulnerability["cve"])
print(computers_vulnerability)
```
:::

