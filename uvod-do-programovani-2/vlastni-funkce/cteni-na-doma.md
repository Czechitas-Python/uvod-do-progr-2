## Nepovinné parametry a klíčové slovo assert

### Nepovinné parametry

Na příkladu funkce `round` jsme viděli, že u některých funkcí není třeba vyplňovat všechny parametry. Vraťme se k funkci `get_mark()`. Uvažujme nyní, že studenti mají možnost získat bonusové body (např. za odevzdání úkolů), které se pak připočítávají k bodům z testu.

```py
def get_mark(points, bonus=0):
    if points + bonus <= 60:
        mark = 5
    elif points + bonus <= 70:
        mark = 4
    elif points + bonus <= 80:
        mark = 3
    elif points + bonus <= 90:
        mark = 2
    else:
        mark = 1
    return mark
```

Nyní opět zavoláme funkci. Uvažujeme stále možnost jednoho opravného pokusu, počet bonusových bodů zůstává.

```py
points = int(input("Zadej počet bodů v testu: "))
bonus = int(input("Zadej počet bonusových bodů: "))
mark = get_mark(points, bonus)
if mark == 5:
    points = int(input("Zadej počet bodů v opravném pokusu: "))
    mark = get_mark(points, bonus)
print(f"Výsledná známka je {mark}.")
```

::exc[excs/hotel]

### Klíčové slovo assert

Klíčové slovo `assert` v Pythonu se používá k ověření, zda je daný výraz pravdivý. Pokud je výraz nepravdivý, vyvolá výjimku `AssertionError`. Tento mechanismus je užitečný pro debugování a ověřování, že se kód chová tak, jak má, během vývoje. 

Vraťme se k funkci `sum_two_numbers`, která přijímá dva argumenty `a` a `b` a vrací jejich součet:

```python
def sum_two_numbers(a, b):
    return a + b
```

Pokud chceme ověřit, že tato funkce správně vrací součet dvou čísel, můžeme použít `assert` k testování této funkcionality. Například:

```python
value = sum_two_numbers(2, 3)
assert value == 5, "Sum of 2 a 3 should be 5"
```

Tento příkaz `assert` ověří, že hodnota uložená v proměnné `value`, kterou jsme získali voláním funkce `sum_two_numbers()` s hodnotami 2 a 3, je skutečně 5. Pokud ano, program pokračuje bez přerušení. Pokud ne, Python vyvolá `AssertionError` s uvedenou chybovou zprávou `"Sum of 2 a 3 should be 5"`.

Klíčové slovo `assert` je jedním ze způsobů, jak otestovat funkci. Pro funkci máme nějaký testovací vstup a očekávaný výstup. Pokud funkce vrátí jinou než očekávanou hodnotu, znamená to, že je ve funkci nějaká chyba. Pozor ale na to, že jeden správný výstup funkce nemusí nutně znamenat, že je vše naprosto v pořádku. Uvažujme například, že jsme ve funkci udělali chybu a použili špatný operátor.

```python
def sum_two_numbers(a, b):
    return a * b
```

U hodnot 2 a 2 tato funkce "projde", ale jde čistě o náhodu - pro čísla 2 a 2 je výsledek sčítání i násobení stejný. Je proto dobré při testování využít více různých testovacích vstupů a výstupů.

```python
value = sum_two_numbers(2, 2)
assert value == 5, "Sum of 2 a 2 should be 2"
```

### Typování funkcí

Python patří mezi *dynamicky typové jazyky*, což znamená, že při vytvoření proměnné neříkáme, jaký typ hodnoty do ní budeme ukládat. Od verze 3.5 ale podporuje `typing`. Můžeme tedy říct, jaký typ hodnoty by *měla obsahovat* nějaká proměnná, Python to však nekontroluje a neukončí program s chybou, pokud do proměnné vložíme hodnotu jiného typu. Typování ale funguje jako nápověda pro programátory a především vývojová prostředí, která pak umějí vývojářům lépe napovídat při psaní programů a případně je upozornit, pokud plánují do proměnné vložit něco, co tam nepatří.

Níže je příklad funkce `get_mark()` s typováním. Typovat můžeme jednotlivé parametry i návratovou hodnotu, jejíž typ je za "šipkou" `->`.

```py
def get_mark(points: int, bonus: int = 0) -> int:
    if points + bonus <= 60:
        mark = 5
    elif points + bonus <= 70:
        mark = 4
    elif points + bonus <= 80:
        mark = 3
    elif points + bonus <= 90:
        mark = 2
    else:
        mark = 1
    return mark

print(get_mark(50, 30))
```
