## Závorky v Pythonu

Níže najdeš přehled toho, jaké typy závorek v Pythonu používáme.

### Kulaté závorky

Jedno z nejčastějších použití kulatých závorek je při volání funkcí.


```python
cislo = 8.3454
zaokrouhlene_cislo = round(cislo)
print(zaokrouhlene_cislo)
```

Též je využijeme při volání metod. Kulaté závorky při volání funkcí i metod musíme použít i v případě, že do nich nic nepíšeme, tj. nepředáváme funkci nebo metodě žádné honoty (argumenty).


```python
predmet = "Python"
predmet = predmet.upper()
print(predmet)
```

Dále je používáme při klasických výpočtech (podle stejných pravidel jako v matematice).

```python
cena_za_prespani = 1200
cena_snidane = 200
pocet_osob = 2
cena_celkem = (cena_za_prespani + cena_snidane) * pocet_osob
print(pocet_osob)
```

Využijeme je i při vytváření (definici) nových funkcí.


```python
def secti_cisla(a, b):
    return a + b
```

A můžeme na ně narazit i při vytváření tuple (tam ale nejsou povinné):


```python
polozka = ("Čajová konvička s hrnky", 899, True)
```

### Hranaté závorky

Hranaté závorky využijeme při práci se seznamy.


```python
# Vytvoření nového seznamu
znamky = [2, 3, 2, 4, 2]
# Přečtení hodnoty ze seznamu
posledni_znamka = znamky[-1]
# Uložení hodnoty na konkrétní pozici v seznamu
# Zde například zlepšíme poslední známku o jeden stupeň, protože student odevzdal výbornou písemnou práci
znamky[-1] = posledni_znamka - 1
print(znamky)
```

Pomocí slicing můžeme získat více hodnot najednou - například tři hodnoty ze začátku. Slicing má smysl jen ve chvíli, kdy chci pouze část hodnot ze seznamu. Pokud chci celý seznam, napíšu jen název proměnné a hranaté závorky nepoužívám.

```python
znamky = [2, 3, 2, 4, 2]
pocatecni_tri_znamky = znamky[:3]
print(pocatecni_tri_znamky)
```

Získávat hodnotu pomocí hranatých závorek můžeme i z řetězců.


```python
jmeno = "Jirka"
prijmeni = "Pešík"
inicialy = jmeno[0] + prijmeni[0]
```

## Složené závorky
Složené závorky využíváme při práci s formátovanými řetězci.


```python
znamky = [2, 3, 2, 4, 2]
posledni_znamka = znamky[-1]
print(f"Moje poslední známka je {posledni_znamka}.")
```

Dále je používáme při vytváření slovníků.

```python
polozka = {"title": "Čajová konvička s hrnky", "price": 899, "in_stock": True}
```

Poněkud matoucí může být jejich použití i při vytváření množiny. Rozdíl je v tom, že při vytváření množiny nepoužíváme dvojtečky, protože ve množině nejdou data ve dvojicích.

```python
polozky = {"Čajová konvička s hrnky", "Kleště na cukr", "Sada lžiček"}
```
