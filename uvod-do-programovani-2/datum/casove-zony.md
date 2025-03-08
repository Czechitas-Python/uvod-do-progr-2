## Čtení na doma: Časové zóny

Aktuální čase se v různých místech na světě liší z důvodu různých časových zón. Běžně se za "základní" časovou zónu považuje UTC (Coordinated Universal Time) a ostatní časové zony jsou definovány posunem vůči UTC. UTC odpovídá zimnímu času na nultému poledníku. Praha je oproti nultému poledníku posunutá při zimním času o 1 hodinu a při letním času o 2 hodiny.

Vytvořme si objekt, který odpovídá 26. květnu 2024, 18:20 v UTC časové zóně.

```py
from datetime import datetime, timedelta, timezone

zacatek_zapasu_utc = datetime(2024, 5, 26, 18, 20, tzinfo=timezone.utc)
```

Převeďme tento čas do pražské časové zóny.

```py
praha_posun = timedelta(hours=2)
praha_casova_zona = timezone(praha_posun)
zacatek_zapasu_praha = zacatek_zapasu_utc.astimezone(praha_casova_zona)
```

Nyní zkusme převod do bostonského času.

```py
boston_posun = timedelta(hours=-4)
boston_casova_zona = timezone(boston_posun)
zacatek_zapasu_boston = zacatek_zapasu_utc.astimezone(boston_casova_zona)
```

Ve výpisu je časová zóna uvedená na konci.

```py
print(f"Začátek zápasu v UTC: {zacatek_zapasu_utc}.")
print(f"Začátek zápasu v Praze: {zacatek_zapasu_praha}.")
print(f"Začátek zápasu v Bostonu: {zacatek_zapasu_boston}.")
```

Pokud bychom od sebe oba údaje odečetli, výsledkem je 0. Python správně spočte, že oba časové údaje se vztahují ke stejnému okamžiku, pouze jsou uvedeny v různých časových zónách.

```py
print(zacatek_zapasu_boston - zacatek_zapasu_praha)
```
