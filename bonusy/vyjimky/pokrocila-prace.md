## Pokročilá práce s výjimkami v Pythonu

V některých částech kódu můžeme odchytávat i více možných výjimek současně. Například čtení ze souboru je typický příklad operace, která může zkrachovat z několika různých důvodů:

- Nejtypičtějším případem je, že soubor neexistuje. To skončí chybou `FileNotFoundError`.
- Může se stát i to, že soubor existuje, ale program nemá přístupová práva pro jeho čtení. To je považováno za jinou chybu, která je označovaná jako `PermissionError`.
- Dalším důvodem může být chybné kódování souboru, např. může být soubor uložený s kódování UTF-16 a my se ho pokoušíme otevřít s kódováním UTF-8.

V případě, že se obáváme nějaké neočekávané chyby, můžeme ošetřit obecnou výjimku `Exception`. Tento přístup ovšem není příliš doporučován. Různé typy chyb totiž vyžadují odlišné způsoby nápravy. Pokud soubor neexistuje, vyřešíme to např. přesunutím souboru do správného adresáře, přejmenováním souboru atd. Naproti tomu nedostatečná oprávnění vyžadují změnu přístupových oprávnění souboru. Chybné kódování znamená nutnost upravit kódování v souboru nebo změnit kódování v programu.

Abychom zjistili, k jaké chybě došlo, můžeme si výjimku uložit do proměnné pomocí klíčového slova `as` a vypsat ji.

Kromě bloku `try` a `except` je možné zařadit i blok `else` (toto `else` se nekamarádí s `if`, ale patří k obsluze výjimek. Je to pouze znovu využité klíčové slovo). Blok `else` se vykoná, pokud chyba v bloku `try` nenastala.

```python
names = []

file_name = "names.txt"

try:
    with open(file_name, encoding="utf-8") as file:
        for line in file:
            names.append(line)
except FileNotFoundError:
    print(f"Soubor '{file_name}' neexistuje.")
except PermissionError:
    print(f"K otevření souboru '{file_name}' nemá program dostatečná práva.")
except Exception as err:
    print(f"Obecná chyba při čtení souboru '{file_name}': {err}")
else:
    print(f"Soubor '{file_name} byl úspěšně přečten.")

print(names)
```


Poslední parťák mezi klíčovými slovy k obsluze výjimek je `finally`. Uvozuje blok kódu, který se vykoná za všech okolností (i kdyby chyba nastala či nenastala). Důležité je zachovat pořadí těchto bloků:

* `try`
* `except`
* (`except`) - více možných bloků `except` pod sebou
* `else`
* `finally`

V bloku `finally` bychom například mohli provést uzavření souboru (pokud bychom nepoužili klíčové slovo `with`) nebo uzavřeli připojení k databázi, pokud bychom pracovali s ní.


### Vyvolání výjimky
Až budeš tvořit složité programy v Pythonu a budeš dobře rozumět obsluze výjimek, může ti přijít na mysl otázka, jestli můžeme výjimku sami vyvolat. V řadě případů totiž můžeme získat (např. od uživatelů) nesmyslná data, i když z pohledu Pythonu je vše v pořádku. Např. věk má smysl pouze jako kladné číslo, ačkoli funkce `int()` by s převodem záporného čísla převod neměla. Výjimku `ValueError` ale můžeme vyvolat sami pomocí klíčového slova `raise`. Záporné číslo pak bude stejný případ jako nečíselná hodnota, tj. program bude pokračovat blokem `except ValueError`.

```python
try:
    vek = input("Zadej věk: ")
    vek = int(vek)

    if vek < 0:
        raise ValueError("Věk nesmí být záporný.")
    
    if vek > 15:
        print("Vítej")
    else:
        print("Představení je až od 15 let.")
except ValueError:
        print("Je třeba zadat pouze číslice a číslo musí být kladné!")

```

Pomocí klíčového slova `raise` jsme zde vyvolali obecnou chybu v běhu programu, kterou poté v příslušném bloku `except` odchytíme výjimkou. `ValueError` byla vybrána ze seznamu vestavěných chyb v Pythonu a nejlépe vystihuje náš problém.

## Cvičení

::exc[excs/banka]

## Bonus

::exc[excs/ukoly]
