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

:::solution

```py
rates = {"Polcoin": 0.47, "PyCoin": 0.21, "Czechitacoin": 0.13}
total_usd = 0
with open("transaction_list.csv", encoding="utf-8") as file:
    for line in file:
        date, amount_str, crypto_with_newline = line.split(";")
        # množství kryptoměny jako číslo
        amount = float(amount_str)
        # název měny bez \n na konci
        crypto = crypto_with_newline.strip()
        # kurz dané měny
        rate = rates[crypto]
        # přičtu hodnotu této transakce v dolarech
        total_usd += amount * rate
# převedu na celé dolary (můžeš použít int nebo round)
total_usd_int = round(total_usd)
print(f"Hodnota úspor Markéty je {total_usd_int} dolarů.")
```

:::
