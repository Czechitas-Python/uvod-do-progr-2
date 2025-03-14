---
title: Polidštění
demand: 2
---

Nainstaluj si balíček `humanize` z webu [pip](https://pypi.org/project/humanize/). Balíček umožní zobrazit některé údaje ve více lidském formátu, např. velká čísla. Vytvoř si nějaké velké číslo (větší než miliarda) a vyzkoušej jeho převod na slovo pomocí funkce `intword`. Dále vyzkoušej převod malého čísla na slovo pomocí metody `apnumber`.

Podívej se, jestli balíček podporuje češtinu. Pokud ne, vyber si některý z jiných nabízených jazků a zkus zobrazit výstup v tomto jazyce.

:::solution

Čeština podporovaná není, vyzkoušíme tedy němčinu.

```py
import humanize

humanize.activate("de_DE")

print(humanize.intword(1200000000))
print(humanize.apnumber(9))
```
:::
