---
title: Převod času
demand: 1
---

V proměnné `apollo_start` máme uložený datum a čas startu Apolla 11. Vypiš datum na obrazovku ve formátu, na který jsou zvyklí Američané, tj. na první místo napiš měsíc, dále den a nakonec rok, jako oddělovače použij lomítka. Čas vypisovat nemusíš.

:::solution
```py
from datetime import datetime, timedelta


apollo_start = datetime(1969, 7, 16, 14, 32)
print(apollo_start.strftime("%#m/%d/%Y")) 
```
:::
