---
title: Kryptoměny
demand: 4
---

Markéta má své úspory ve třech kryptoměnách: Czechitacoinu, Polcoinu a PyCoinu. Potřebovala by zjistit, kolik je celková hodnota jejích úspor v celých dolarech. Bohužel její aplikace toto zobrazit neumí, má pouze k dispozici přehled všech transakcí, které jsou v souboru [transaction_list.csv](assets/transaction_list.csv). V prvním sloupci je datum transakce, ve druhém sloupci hodnota transakce a ve třetím sloupci kryptoměna, ve které transakce proběhla. Níže máš slovník s aktuáními kurzy těchto měn v dolarech. Zápis znamená, že 1 Polcoin má hodnotu 0.47 dolarů, 1 PyCoin 0.21 dolarů atd.

Pozor na to, že po použití metody `.split()` na proměnnou s řádkem budeš mít součástí řetězce s názvem kryptoměny i znak pro konec řádků `\n`. Toho se můžeš zbavit s využitím metody `.strip()`.

```python
rates = {"Polcoin": 0.47, "PyCoin": 0.21, "Czechitacoin": 0.13}
```

Vzorový výstup je níže.

```
Hodnota úspor Markéty je 53314 dolarů.
```
