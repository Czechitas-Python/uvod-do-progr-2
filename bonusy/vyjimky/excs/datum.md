---
title: Datum
demand: 2
---

Požádej uživatele o zadání data narození ve formátu `RRRR-MM-DD`.

Nejprve ověř pomocí podmínek, že je zadáno správné datum - tj. v datu jsou dvě pomlčky a po rozdělení na jednotlivé části obsahuje každá z částí číslo. Stále je ale možné, že je zadáno nesmyslné datum. Například je možné zadat datum 31. dubna nebo 29. února pro nepřestupný rok. Proto přidej modul `datetime` a pomocí metody `fromisoformat()` vyzkoušej převod na typ `datetime`. Ošetři `ValueError`, která může být způsobena výše uvedenými případy.


```py
from datetime import datetime

datum_narozeni = input("Zadej datum ve formátu RRRR-MM-DD: ")
datum_narozeni = datetime.fromisoformat(datum_narozeni)
```
