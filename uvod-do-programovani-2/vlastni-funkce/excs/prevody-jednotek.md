---
title: Funkce pro převody jednotek
---

Začni vytvořením funkce `kilometry_na_mile(kilometry)` a `mily_na_kilometry(mile)`, které provedou převod mezi kilometry a mílemi.

Z následujících zadání si **vyber jedno**, které se ti líbí nejvíce, a to vyřeš.

- Vytvoř funkce `metry_na_stopy(metry)` a `stopy_na_metry(stopy)`, které umožňují převod mezi metry a stopami.
- Vytvoř funkce `centimetry_na_palec(centimetry)` a `palce_na_centimetry(palce)`, které umožní převod mezi centimetry a palci.
- Vytvoř funkce `kilogramy_na_libry(kilogramy)` a `libry_na_kilogramy(libry)`, které provedou převod mezi kilogramy a librami.
- Vytvoř funkce `litry_na_galony(litry)` a `galony_na_litry(galony)`, které umožní převod mezi litry a galony.
- Vytvoř funkce `kmh_na_mph(kmh)` a `mph_na_kmh(mph)`, které umožní převod rychlosti mezi kilometry za hodinu a míli za hodinu.
- Vytvoř funkce `celsia_na_fahrenheit(teplota)` a `fahrenheit_na_celsia(teplota)`, které umožňují převod teploty mezi stupni Celsia a stupni Fahrenheit.

:::box{type=tip}
Výsledky si ověř pomocí online kalkulátoru, že vycházejí správně.
:::

:::solution

Převod kilometrů na míle a zpět

```py
def kilometry_na_mile(kilometry):
    return kilometry * 0.621371
def mile_na_kilometry(mile):
    return mile / 0.621371
```

Převod metrů na stopy a zpět

```py
def metry_na_stopy(metry):
    return metry * 3.28084
def stopy_na_metry(stopy):
    return stopy / 3.28084
```

Převod centimetrů na palce a zpět

```py
def centimetry_na_palec(centimetry):
    return centimetry * 0.393701
def palce_na_centimetry(palce):
    return palce / 0.393701
```

Převod hmotnosti kilogramů na libry a zpět

```py
def kilogramy_na_libry(kilogramy):
    return kilogramy * 2.20462
def libry_na_kilogramy(libry):
    return libry / 2.20462
```

Převod objemu litrů na galony a zpět

```py
def litry_na_galony(litry):
    return litry * 0.264172
def galony_na_litry(galony):
    return galony / 0.264172
```

Převod rychlosti kilometrů za hodinu na míle za hodinu a zpět

```py
def kmh_na_mph(kmh):
    return kmh * 0.621371
def mph_na_kmh(mph):
    return mph / 0.621371
```

Převod teploty ze stupňů Celsia na Fahrenheit a zpět

```py
def celsia_na_fahrenheit(teplota):
    return teplota * 1.8 + 32
def fahrenheit_na_celsia(teplota):
    return (teplota - 32) / 1.8
```
:::
