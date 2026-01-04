---
title: Výkazy
demand: 4
---

Uvažuj data o pracovních výkazech, která jsou uložena v souboru [work_hours.json](assets/work_hours.json). 

Data obsahují pracovní výkazy 5 zaměstnanců za srpen 2023. Pro každý pracovní den jsou v datech následující informace:
- `date` - datum,
- `employee` - jméno zaměstnance/zaměstnankyně,
- `drecord_typeate` - typ záznamu, který říká, co zaměstnanec/zaměstnankyně daný den dělal(a), možnosti jsou: "work" (práce), "holiday" (dovolená), "care" (péče o člena rodiny), "unpaid" (neplacené volno),
- `worked_on` - pokud je typ záznamu "work", je tam vnořený slovník s počty odpracovaných hodin na jednotlivých projektech.

U záznaů typu dovolená, péče o člena rodiny nebo neplacené volno vždy uvažujeme délku 8 hodin. Pokud zaměstnanec pracoval, jsou odpracované hodiny dané součtem práce na jednotlivých projektech a může to být jiné číslo než 8. Tvým úkolem je vytvořit dva reporty: report o odpracovaných hodinách a absencích každého zaměstnance a report odpracované práce na projektu.

Začnemě s reportem o zaměstnancích. Vstupem pro něj je zbývající dovolená, tj. nárok na dovolenou, který ještě zaměstnanci v tomto kalendářním roce nevyčerpali. Podle nového zákoníku práce je nárok v hodinách.

```py
remaining_holiday = {"Marta Nováková": 120, "Michael Rostock-Poplar": 96, "Ondřej Bartoš": 40, "Daniela Bérová": 168, "Ivan Pilný": 32}
```

Tvým úkolem je spočítat pro každého zaměstnance (zaměstnankyni):

- kolik odpracoval(a) hodin,
- kolik si vybral(a) dovolené (v hodinách),
- kolik zbývá dovolené na konci září,
- kolik hodin strávil(a) péčí o člena rodiny,
- kolik hodin strávil na neplaceném volnu.

Příklad výstupu je níže.

```json
{
    "Marta Nováková": {
        "work_hours": 117,
        "holiday_taken": 64,
        "holiday_remaining": 56,
        "care": 0,
        "unpaid": 0
    },
    "Michael Rostock-Poplar": {
        "work_hours": 101,
        "holiday_taken": 48,
        "holiday_remaining": 48,
        "care": 24,
        "unpaid": 0
    },
    "Ondřej Bartoš": {
        "work_hours": 144,
        "holiday_taken": 32,
        "holiday_remaining": 8,
        "care": 8,
        "unpaid": 0
    },
    "Daniela Bérová": {
        "work_hours": 104,
        "holiday_taken": 64,
        "holiday_remaining": 104,
        "care": 8,
        "unpaid": 0
    },
    "Ivan Pilný": {
        "work_hours": 135,
        "holiday_taken": 32,
        "holiday_remaining": 0,
        "care": 8,
        "unpaid": 0
    }
}
```

Dále vytvoř report odpracovaných hodin na projektu.

Můžeš si zvolit jednodušší variantu, tj. spočítat hodiny za každý projekt celkem:

```json
{
    "TrendVision": 133,
    "DataDive": 89,
    "PulseCheck": 116,
    "Mandala": 119,
    "FinanceFlare": 144
}
```

Alternativně můžeš spočítat, kolik na každém projektu odpracovali jednotliví zaměstnanci.

```json
{
    "TrendVision": {
        "Marta Nováková": 98,
        "Michael Rostock-Poplar": 35
    },
    "DataDive": {
        "Marta Nováková": 19,
        "Daniela Bérová": 70
    },
    "PulseCheck": {
        "Michael Rostock-Poplar": 28,
        "Daniela Bérová": 34,
        "Ivan Pilný": 54
    },
    "Mandala": {
        "Michael Rostock-Poplar": 38,
        "Ivan Pilný": 81
    },
    "FinanceFlare": {
        "Ondřej Bartoš": 144
    }
}
```
