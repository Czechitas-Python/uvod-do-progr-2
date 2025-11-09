## Čtení na doma: Funkce na plánování dovolené

Podíváme se na plánování dovolené. Protože vybráme na poslední chvíli, máme již k dispozici předpověď počasí. Protože si během dovolené chceme užít turistiku po městech nebo v horách, preferujeme spíše teploty do 30 stupňů.

V seznamu `teploty` máme týdenní předpověď pro jednu potenciální lokalitu. Kolik dní tam můžeme čekat teplotu do 30 stupňů?

```python
teploty = [22, 32, 28, 30, 21, 33, 29]

pocet = 0
for hodnota in teploty:
    if hodnota <= 30:
        pocet = pocet + 1
print(pocet)
```

Dále uvažujeme, že nechceme utratit příliš mnoho peněz a chceme tedy v lokalitě mít několik možností ubytování s cenou do 35 tisíc. V seznamu `ceny_ubytovani` máme ceny za několik hotelů, kde mají volné místo. Kolik hotelů vyhovuje naší cenové podmínce?

```python
ceny_ubytovani = [42000, 30000, 18000, 40000, 25000, 27000]
```

Když se zamyslíš nad tímto úkolem, v podstatě řešíme stejnou věc jako předtím. Chceme spočítat, kolik hodnot v seznamu je menších nebo rovno nějaké námi definované hranici. Pro řešení můžeme využít funkci.


```python
def pocet_hodnot_mensich_nez_hranice(seznam, hranice):
    pocet = 0
    for hodnota in seznam:
        if hodnota <= hranice:
            pocet = pocet + 1
    return pocet
```

Výsledek funkce můžeme uložit do proměnné a dál s ním pracovat, můžeme ho vypsat atd.

```python
vysledek = pocet_hodnot_mensich_nez_hranice(teploty, 30)
if vysledek > 2:
    print("Je tam vedro.")
else:
    print("Je to v pohodě.")
print(pocet_hodnot_mensich_nez_hranice(ceny_ubytovani, 28000))
```
