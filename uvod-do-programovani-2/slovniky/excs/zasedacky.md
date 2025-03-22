---
title: Zasedačky
demand: 2
---

Firma eviduje volné meetingové místnosti v průběhu dne ve slovníku. Klíč slovníku je hodina a hodnotou slovníku seznam zasedaček, které jsou v té době volné. Napiš program, který se zeptá uživatele na číslo hodiny, kdy chce zamluvit nějakou zasedačku. Poté vypíše počet volných místností, které jsou k dispozici.

Pokud není k dispozici žádná místnost, program vypíše `V tuto hodinu již není k dispozici žádná zasedací místnost`.

```python
volnePokoje = {
  9: ["Amadeus", "Goya", "Vlasy"],
  10: ["Forman", "Goya"],
  11: [],
  12: ["Amadeus", "Vlasy"]
}
```
