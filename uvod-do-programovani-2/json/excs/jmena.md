---
title: Jména
demand: 2
---

Služba Nationalize poskytuje odhad národnosti na základě jména. Příklad volání služby pro jméno "jiri" je `https://api.nationalize.io/?name=jiri`.

```py
{
   "country":[
      {
         "country_id":"CZ",
         "probability":0.842
      },
      {
         "country_id":"SK",
         "probability":0.029
      },
      {
         "country_id":"FI",
         "probability":0.028
      },
      {
         "country_id":"AT",
         "probability":0.013
      },
      {
         "country_id":"IE",
         "probability":0.009
      }
   ],
   "name":"jiri"
}
```

Projdi celý seznam a zobraz národnost (hodnota s klíčem `country_id` s nejvyšší hodnotou `probability`), která je dle služby nejvíce pravěpodobná. Vyzkoušej program na jménu "Oksana", "Hans" nebo na jakémkoli jiném, které tě zajímá.

Níže je příklad výstupu pro jméno "jiri":

```py
{
   "country_id":"CZ",
   "probability":0.842
}
```
