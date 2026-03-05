---
title: Rodná čísla
demand: 3
---

V následujícím seznamu máš seznam rodných čísel pacientů, kteří navštívili v jeden konkrétní den lékařskou ordinaci.

```py
rodna_cisla = [
    "845128/6219",
    "801002/5021",
    "900116/8291",
    "790501/7894",
    "850706/9259",
    "891222/1824",
    "870327/9582",
    "810602/6883",
    "850512/5070",
    "790531/7081"
]
```

- Kolik přišlo mužů a kolik žen?
- Kdy se narodil nejstarší a kdy nejmladší pacient?

Pokud nevíš, jak funguje rodné číslo, vysvětlení je níže:

Rodné číslo je identifikační číslo, které slouží k jednoznačné identifikaci osoby. V České republice se rodné číslo skládá z 10 číslic a jednoho lomítka, které ho rozděluje na části.

- Prvních 6 číslic udává datum narození v pořadí rok (2 číslice), měsíc (2 číslice) a den (2 číslice). Například pro narození 2. února 1990 by prvních 6 číslic mělo být 900202. Zbytek rodného čísla (tj. část za lomítkem) slouží k identifikaci konkrétní osoby.
- Ženy mají k číslu měsíce přičteno 50, např. 845128/6219 je číslo patřící ženě.

Vytvoř kód, který bude fungovat pouze pro pacienty a pacientky narozené před rokem 2000. Též uvažuj, že se v datech nebude objevovat dvojice narozená ve stejný den.

Tip: Pro porovnání dvou různých čísel je možné použít operátor větší než a menší než pro řetězce. Pouze je potřeba v případě žen vytvořit upravené rodné číslo, které bude obsahovat číslo měsíce ve standardním tvar, tj. bez přičtené 50. Pozor na to, že číslo měsíce musí mít vždy dva znaky.

```py
if rodne_cislo_1 < rodne_cislo_2:
    print("Pacient(ka) 1 je starší")
else:
    print("Pacient(ka) 2 je starší")
```
