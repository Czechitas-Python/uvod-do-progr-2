## Sekvence

Sekvence jsou hodnoty, které v sobě obsahují jiné hodnoty. Zatím jsme poznali základní dva typy sekvencí - řetězec (`string`) a seznam (`list`).

### Řetězce jako sekvence

Řetězce jsou vlastně sekvence skládající se z jednotlivých písmen. K jednotlivým prvkům sekvence přistupujeme pomocí hranatých závorek, které píšeme za název řetězce. Písmena jsou číslovaná (indexovaná) od 0.

Uvažujme například, že naše aplikace má zjistit leteckou společnost podle čísla letu. Pro zjednodušení ji naučíme rozpoznat pouze dvě společnosti: 

* British Airways (číslo letu začíná BA),
* Lufthansa (číslo letu začíná LH).

```py
flight_number = "BA 853"
prefix = flight_number[0] + flight_number[1]
if prefix == "BA":
    company = "British Airways"
elif prefix == "LH":
    company = "Lufthansa"
else:
    company = "Neznámá společnost"
print(f"Letíte se společností {company}")
```

### Seznamy

Seznamy zapisujeme do hranatých závorek. Do seznamu můžeme vložit libovolný datový typ, jaký už známe. Začněme například s řetězci.

```py
guest_list = ["Jirka", "Klára", "Natálie"]
```

Poslední jméno na seznamu získáme opět pomocí hranatých závorek

```py
print(guest_list[-1])
```

Sekvence v sobě mohou obsahovat i jiné sekvence. Je to podobné, jako polička na knihy. Ta obsahuje několik knih, každá kniha má několik kapitol, každá kapitola se skládá ze spousty slov a písmen. Níže máš příklad seznamu uvnitř seznamu, který obsahuje jména a známky studentů v nějakém předmětu.

Data si nejprve ukážeme jako tabulku.

```py
school_marks = [
    ["Jiří", 1, 4, 3, 2],
    ["Natálie", 2, 3, 4, 3],
    ["Tereza", 1, 1, 2, 1],
]

print(f"První student(ka) v seznamu je {school_marks[0][0]}.")
print(f"Její/jeho poslední známka je {school_marks[0][-1]}.")
```
