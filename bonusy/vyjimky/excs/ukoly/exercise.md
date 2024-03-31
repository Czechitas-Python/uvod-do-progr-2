---
title: Úkoly
demand: 2
---

Implementujme systém pro správu seznamu úkolů (*todo list*). Stáhni si soubor [tasks.txt](assets/tasks.txt). Každý řádek obsahuje název úkolu a jeho prioritu (1=vysoká, 2=střední, 3=nízká), hodnoty jsou oddělené čárkou.

Tvůj program by měl nejprve načíst existující úkoly ze souboru `tasks.txt`` a uložit je do seznamu. Pokud soubor neexistuje, program jen vypíše informaci o tom, že seoubor neexistuje a že ho založí. Samotné založení souboru v této části řešit nemusíš, o to se postaráme v další části.

Poté program umožní uživateli přidat nový úkol a jeho prioritu. Pokud jako prioritu nezadá číslo nebo zadá jiné číslo než 1 až 3, vyvolej `ValueError`j. Pokud je vstup v pořádku, ulož seznam s přidaným úkolem do souboru `tasks.txt`. Pokud soubor neexistuje, stačí ho pomocí funkce `open` s módem `w` otevřít.
