---
title: Kostky
demand: 2
---

Vytvoř jednoduchou hru, která simuluje hodu třemi kostkami.

Na začátku hry uživatel zadá částku, kterou chce vsadit, a jestli sází na sudý nebo lichý součet. Pomocí funkce `randint` z modulu `random` vygeneruj tři čísla v rozsahu 1 až 6 a vypočti jejich součet. Pokud uživatel vsadil správně, vypiš, že vyhrává dvojnásobek. V opačném případě vypiš, že nevyhrává nic.

Všechny důležité události v průběhu hry by měly být zaznamenány pomocí logování. To zahrnuje:

- začátek a konec hry,
- výši sázky a číslo, na které uživatel vsadil,
- Výsledek hodů a výsledek hry (výhra/prohra).


Vytvoř vlastní formát logovacích zpráv, který bude obsahovat časové razítko, úroveň logování, název souboru, číslo řádku, název funkce a logovací zprávu. Nastav logger tak, aby logovací zprávy byly ukládány do souboru `game.log`.
