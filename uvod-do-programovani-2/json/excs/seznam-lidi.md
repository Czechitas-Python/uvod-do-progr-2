---
title: Seznam lidí
demand: 2
---

Jak už jsme si ověřili v lekci, datové API na adrese `https://api.kodim.cz/python-data/people` obsahuje seznam lidí. Napište program, který tento seznam z API stáhne a převede z formátu JSON na Python slovníky. Proveďte následující úkoly.

1. Zjistěte kolik lidí celkem seznam obsahuje.
1. Zjistěte jaké všechny informace máme o jednotlivých osobách.
1. Zjistěte, kolik je v souboru mužů a žen.

:::solution
```py
import json
import requests

response = requests.get("https://api.kodim.cz/python-data/people")
data = response.json()

print(len(data))
print(data[0].keys())

gender_count = {}
for item in data:
    gender_count[item["gender"]] = gender_count.get(item["gender"], 0) + 1
print(gender_count)
```
:::
