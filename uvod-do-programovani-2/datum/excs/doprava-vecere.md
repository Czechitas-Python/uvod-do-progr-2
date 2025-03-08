---
title: Doprava večeře
demand: 3
---

Zákazník si objednal večeři na webu dovážkové služby 13. listopadu 2020 v 19:47. Víme, že převzetí objednávky restaurací v průměru trvá 8 minut a 35 sekund, příprava jídla trvá 30 minut a doprava jídla k zákazníkovi 25 minut a 30 sekund. Kdy očekáváme, že jídlo dorazí zákazníkovi?

:::solution
```py
from datetime import datetime, timedelta


objednavka = datetime(2020, 11, 13, 19, 47)
prevzeti = timedelta(minutes=8,seconds=35)
priprava = timedelta (minutes=30)
doprava = timedelta(minutes=25, seconds=30)


celkem = objednavka +  prevzeti + priprava + doprava
print(celkem)
```
:::
