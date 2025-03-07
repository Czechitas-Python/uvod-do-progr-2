---
title: Obsazenost zasedaček
demand: 2
---

Naše společnost má aktuálně kanceláře se 4 zasedačkami: Forman, Vlasy, Goya a Amadeus. Aktuálně plánuje stěhování do nových prostor a řeší, kolik zasedacích místností by tam mělo být. Proto chce spočítat, jak moc jsou v současnosti zasedačky využívané.

Níže máš přehled naplánovaných meetingů v jednotlivých zasedačkách během jednoho vybraného dopoledne. Každý meeting trvá právě jednu hodinu, začíná v celou hodinu (např. v 8:00). Tvým úkolem je spočítat pro každou hodinu vypsat počet volných zasedaček.

```py
meetingy = [
    ["8:00-8:59", "Forman", "Pravidelný meeting managementu"],
    ["8:00-8:59", "Vlasy", "Plánování vánočního večírku"],
    ["9:00-9:59", "Forman", "Pohovor - paní Krejcarová"],
    ["9:00-9:59", "Amadeus", "Pohovor - paní Řeháková"],
    ["9:00-9:59", "Goya", "Příprava marketingové kampaně"],
    ["9:00-9:59", "Vlasy", "Plán cash-flow"],
    ["10:00-10:59", "Forman", "Pohovor - paní Hrachovcová"],
    ["10:00-10:59", "Goya", "Setkání se zákazníkem (pan Klimeš)"],
    ["11:00-11:59", "Amadeus", "Stěhování - plánování prohlídek"],
    ["11:00-11:59", "Forman", "Scrum - Python tým"],
    ["11:00-11:59", "Goya", "Pohovor - paní Vašků"],
]
```

Příklad výstupu je níže. Jednotlivé položky seznamu udávají počet volných zasedaček v hodinových intervalech. V čase od 8:00 do 8:59 jsou volné dvě zasedačky, v čase od 9:00 a 9:59 není volná žádná atd.

```
[2, 0, 2, 1]
```
