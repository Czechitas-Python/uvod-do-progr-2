---
title: Čas od startu
demand: 3
---

Satelit Solar Orbiter, který má za cíl pozorování Slunce, odstartoval 10. února 2020 v 5:03. Ulož si hodnotu startu do proměnné.

- Který den v týdnu Solar Orbiter odstartoval?
- Spočítej, kolik času od jeho startu uplynulo.

:::solution
```py
from datetime import datetime


so_start = datetime(2020, 2, 10, 5, 3)
so_start.weekday()
uplynulo = datetime.now() - so_start
print(uplynulo)
```
:::
