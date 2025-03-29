---
title: Kočky
demand: 2
---

Použij modul requests k otevřené následujícího API: `https://catfact.ninja/fact`. API vrátí náhodnou informaci o kočkách. Příklad výstupu je níže:

```py
{
   "fact":"A cats field of vision is about 185 degrees.",
   "length":44
}
```

Získej jednu informaci a ulož ji do souboru ve formátu JSON. Ulož pouze informace (`fact`), délku neukládej. Níže je příklad, jak by soubor měl vypadat.

```py
{
   "fact":"A cats field of vision is about 185 degrees."
}
```


:::solution
```py
import json
import requests

response = requests.get("https://catfact.ninja/fact")
data = response.json()
data.pop("length")

with open("kocky.json", "w", encoding="utf-8") as file:
    json.dump(data, file)
```
:::
