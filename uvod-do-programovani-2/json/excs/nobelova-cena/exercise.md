---
title: Nobelova cena
---

Stáhni si soubor [laureates.json](assets/laureates.json), který obsahuje data o nositelích a nositelkách Nobelovy ceny. Soubor obsahuje seznam, kde každý prvek představuje jednoho laureáta/ku. Každý záznam má mimo jiné následující strukturu (zkráceno):

```json
{
  "knownName": {"en": "Albert Einstein"},
  "birth": {
    "place": {
      "countryNow": {"en": "Germany"}
    }
  },
  "nobelPrizes": [
    {
      "category": {"en": "Physics"}
    }
  ]
}
```

Tvým úkolem je zjistit, kolik nositelů Nobelovy ceny pochází z jednotlivých zemí, a to **pro každou kategorii zvlášť**. Výsledkem bude slovník, kde:

- **klíčem** je název kategorie (např. `"Physics"`), který najdeš v `nobelPrizes` → `category` → `"en"`,
- **hodnotou** je vnořený slovník, kde **klíčem** je název země a **hodnotou** počet laureátů narozených v dané zemi. Zemi narození najdeš v `birth` → `place` → `countryNow` → `"en"`.

Při zpracování dávej pozor na dvě věci:

1. Některé záznamy nemají klíč `birth` — jedná se o organizace (např. Červený kříž). Tyto záznamy přeskoč.
1. Jeden člověk může mít více Nobelových cen (seznam `nobelPrizes` může mít více prvků). Každou cenu počítej samostatně.

Očekávaný výstup programu je zobrazen níže.

```
{'Economic Sciences': {'USA': 47, 'India': 2, 'Scotland': 2, 'Finland': 1, 'Sweden': 2, 'Cyprus': 1, 'United Kingdom': 6, 'Israel': 1, 'France': 4, 'Norway': 3, 'Italy': 1, 'Austria': 1, 'the Netherlands': 2, 'Hungary': 1, 'Russia': 3, 'Canada': 3, 'Poland': 1, 'Germany': 1, 'Belarus': 1, 'Saint Lucia': 1}, 'Physics': {'Denmark': 2, 'Pakistan': 2, 'USA': 69, 'Poland': 8, 'Germany': 25, 'France': 10, 'Australia': 2, 'Russia': 10, 'United Kingdom': 22, 'Canada': 6, 'Scotland': 1, 'Italy': 5, 'Switzerland': 6, 'China': 5, 'Algeria': 1, 'Hungary': 2, 'Ireland': 1, 'Austria': 3, 'Belgium': 1, 'the Netherlands': 9, 'Luxembourg': 1, 'Sweden': 4, 'Japan': 11, 'Norway': 1, 'Azerbaijan': 1, 'Czech Republic': 1, 'Slovakia': 1, 'Morocco': 1, 'India': 1, 'Belarus': 1}, 'Chemistry': {'Israel': 4, 'Lithuania': 1, 'Germany': 26, 'Egypt': 2, 'Japan': 7, 'USA': 54, 'New Zealand': 2, 'France': 9, 'United Kingdom': 24, 'Sweden': 4, 'Finland': 1, 'Hungary': 3, 'Turkey': 1, 'the Netherlands': 4, 'South Korea': 1, 'China': 1, 'Poland': 4, 'Slovenia': 1, 'Italy': 1, 'Canada': 4, 'Russia': 4, 'Switzerland': 3, 'Czech Republic': 1, 'Denmark': 1, 'Australia': 1, 'Norway': 2, 'Croatia': 1, 'Scotland': 3, 'Mexico': 1, 'Austria': 5, 'South Africa': 1, 'Ukraine': 1, 'Romania': 1, 'India': 1, 'Bosnia and Herzegovina': 1, 'Latvia': 1, 'Taiwan': 1, 'Belgium': 1}, 'Peace': {'Ethiopia': 1, 'Argentina': 2, 'USA': 19, 'Switzerland': 3, 'Zimbabwe': 1, 'France': 10, 'Mexico': 1, 'Austria': 1, 'Sweden': 5, 'Russia': 2, 'Egypt': 3, 'Scotland': 2, 'Belgium': 3, 'Myanmar': 1, 'Czech Republic': 1, 'Northern Ireland': 4, 'Germany': 5, 'East Timor': 2, 'Norway': 2, 'Democratic Republic of the Congo': 1, 'South Africa': 3, 'Japan': 1, 'Romania': 1, 'Liberia': 2, 'Italy': 1, 'Denmark': 1, 'Poland': 2, 'Colombia': 1, 'India': 1, 'South Korea': 1, 'Ghana': 1, 'Vietnam': 1, 'Canada': 1, 'China': 2, 'Pakistan': 1, 'Finland': 1, 'Belarus': 2, 'North Macedonia': 1, 'Bangladesh': 1, 'Iraq': 1, 'Costa Rica': 1, 'United Kingdom': 5, 'Guatemala': 1, 'Iran': 1, 'Yemen': 1, 'the Netherlands': 1, 'Kenya': 1, 'Israel': 1}, 'Physiology or Medicine': {'United Kingdom': 24, 'Belgium': 3, 'Hungary': 2, 'Germany': 18, 'France': 12, 'USA': 76, 'South Africa': 3, 'Sweden': 7, 'Lithuania': 1, 'Denmark': 3, 'Australia': 7, 'Venezuela': 1, 'Argentina': 2, 'Italy': 5, 'Czech Republic': 2, 'Canada': 4, 'the Netherlands': 2, 'Switzerland': 6, 'China': 2, 'Norway': 2, 'Portugal': 1, 'Poland': 6, 'Austria': 6, 'Russia': 2, 'Romania': 1, 'India': 2, 'Ukraine': 2, 'Scotland': 3, 'Luxembourg': 1, 'New Zealand': 1, 'Faroe Islands (Denmark)': 1, 'Brazil': 1, 'Finland': 1, 'Spain': 2, 'Japan': 5, 'Indonesia': 1, 'Ireland': 1}, 'Literature': {'Algeria': 1, 'Russia': 5, 'Canada': 2, 'France': 11, 'United Kingdom': 6, 'Norway': 2, 'USA': 9, 'Spain': 5, 'Switzerland': 1, 'Madagascar': 1, 'Lithuania': 1, 'Italy': 6, 'Saint Lucia': 1, 'Iran': 1, 'Austria': 2, 'Bulgaria': 1, 'Sweden': 7, 'Finland': 1, 'Colombia': 1, 'Chile': 2, 'China': 2, 'Ireland': 3, 'Poland': 7, 'Turkey': 2, 'Iceland': 1, 'Germany': 7, 'Denmark': 4, 'Romania': 1, 'Hungary': 1, 'Bosnia and Herzegovina': 1, 'South Africa': 2, 'Czech Republic': 1, 'Portugal': 1, 'Japan': 3, 'Peru': 1, 'Belgium': 1, 'Guatemala': 1, 'Egypt': 1, 'Mexico': 1, 'Greece': 1, 'India': 2, 'Guadeloupe Island': 1, 'Northern Ireland': 1, 'Ukraine': 2, 'Trinidad and Tobago': 1, 'Nigeria': 1}}
```

:::solution

```py
import json

with open("json_laureates.json", encoding="utf-8") as file:
    data = json.load(file)


prizes_per_category_and_country = {}

for item in data:
    if "birth" in item:
        birth_country = item["birth"]["place"]["countryNow"]["en"]
        for prize in item["nobelPrizes"]:
            category = prize["category"]["en"]
            if category not in prizes_per_category_and_country:
                prizes_per_category_and_country[category] = {}
            if birth_country not in prizes_per_category_and_country[category]:
                prizes_per_category_and_country[category][birth_country] = 0
            prizes_per_category_and_country[category][birth_country] += 1
print(prizes_per_category_and_country)

```
:::