## Podmínky

Naše programy se často musejí *rozhodovat* a některé bloky kódu se spouštějí pouze za předpokladu splnění nějaké podmínky. Podmínku začínáme klíčovým slovem `if`. Blok, který se spouští při splnění podmínky, je vždy odsazený (standardně čtyřmi mezerami).

Uvažujme například divadlo, které dává slevu 10 % při nákupu lístků za celkovou cenu více než 500 Kč. Pokud tedy zákazník zakoupí větší množství lístků, dostaneme informaci o získané slevě. Každý zákazník pak získá informaci o celkové ceně, protože tento blok již není odsazený.

Poznámka: Kód níže se sice v pořádku spustí a vypíše výsledek, ale ten není úplně správně. Přijdeš na to, kde je chyba?

```py
number_of_tickets = 4
price_per_ticket = 190
total_price = number_of_tickets * price_per_ticket
if total_price >= 500:
    # Sleva 10 %
    total_price = total_price * 0.1
    print("Získáváte slevu 10 %!")

print(f"Celková cena nákupu je {total_price} Kč.")
```

#### Na co si dát pozor

* Na konci řádku s podmínkou musíme zapsat dvojtečku (`:`). Poté Visual Studio Code provádí odsazení automaticky.
* Každá podmínka musí obsahovat alespoň jeden řádek, tj. minimálně jeden řádek po podmínce musí být odsazený.

#### Komplexnější podmínky

Pokud si přejeme spustit nějaký blok kódu v případě, že podmínka není splněná, použijeme klíčové slovo `else`.

```py
number_of_tickets = 2
price_per_ticket = 190
total_price = number_of_tickets * price_per_ticket
if total_price >= 500:
    total_price = total_price * 0.1
    print("Získáváte slevu 10 %!")
else:
    print("Bohužel nezískáváte slevu.")

print(f"Celková cena nákupu je {total_price} Kč.")
```

Větví podmínek můžeme mít i několik za sebou. Klíčové slovo `elif` je kombinací `else` a `if`. Uvažujme například, že od nákupu za 500 Kč dáváme slevu 10 % a od nákupu za 1500 Kč dáváme slevu 20 %.

```py
number_of_tickets = 12
price_per_ticket = 190
total_price = number_of_tickets * price_per_ticket
if total_price >= 1500:
    total_price = total_price * 0.2
    print("Získáváte slevu 20 %")
elif total_price >= 500:
    total_price = total_price *  0.1
    print("Získáváte slevu 10 %")
else:
    print("Bohužel nezískáváte slevu.")

print(f"Celková cena nákupu je {total_price} Kč.")
```
