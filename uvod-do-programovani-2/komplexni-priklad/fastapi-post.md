## POST requesty a vyhledávání

Dosud jsme pracovali jen s GET requesty, které slouží k načítání dat. Dnes přidáme *POST request* - ten se používá tehdy, když chceme serveru předat i nějaká vstupní data. Typicky se POST používá při vyhledávání podle více kritérií nebo při vytváření nových záznamů.

Rozdíl oproti GET je v tom, že POST request má kromě adresy i *tělo* (body) - JSON objekt s parametry dotazu.

### Pydantic

Aby FastAPI vědělo, jakou strukturu tělo requestu má mít, popíšeme ji pomocí knihovny *Pydantic*. Pydantic jsme viděli už u datových tříd - slouží k validaci dat a definici jejich struktury. Nainstalujeme ho příkazem:

```shell
pip install pydantic
```

Pydantic je ve skutečnosti součástí FastAPI, takže ho pravděpodobně máš nainstalovaný už z dřívějška. Příkaz výše ho doinstaluje jen v případě, že chybí.

Strukturu těla requestu popíšeme třídou, která dědí od `BaseModel`:

```py
from pydantic import BaseModel

class SubjektFiltr(BaseModel):
    obchodniJmeno: str
```

FastAPI pak třídu použije k automatické validaci - pokud tělo requestu nebude obsahovat pole `obchodniJmeno` nebo nebude řetězec, server vrátí chybu `422` ještě před tím, než se zavolá naše funkce.

### Vyhledávání subjektů podle jména

Přidáme endpoint, který přijme filtr a vrátí všechny subjekty, jejichž obchodní jméno obsahuje hledaný řetězec. Parametr funkce pojmenujeme `filtr` a typem bude naše třída `SubjektFiltr` - FastAPI z toho pozná, že data má číst z těla requestu:

```py
@app.post("/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat")
def vyhledej_subjekty(filtr: SubjektFiltr):
    """Vyhledá subjekty, které mají zadaný řetězec v obchodním jménu."""
    hledane = filtr.obchodniJmeno.lower()
    nalezene = []
    for subjekt in subjekty:
        if hledane in subjekt["obchodniJmeno"].lower():
            nalezene.append(subjekt)

    nalezene.sort(key=lambda subjekt: subjekt["ico"])
    return {
        "pocetCelkem": len(nalezene),
        "ekonomickeSubjekty": nalezene,
    }
```

Porovnávání provádíme po převodu na malá písmena metodou `lower()`, takže vyhledávání není citlivé na velikost písmen. Výsledky seřadíme podle IČO a vrátíme slovník s počtem nalezených subjektů a jejich seznamem.

### Číselník právních forem

Přidáme ještě jeden endpoint, který vrátí číselník právních forem. Tělo requestu tentokrát nepotřebujeme, funkce prostě vrátí data načtená při startu serveru:

```py
@app.post("/ekonomicke-subjekty-v-be/rest/ciselniky-nazevniky/vyhledat")
def vyhledej_ciselniky():
    """Vrátí číselník právních forem (jediný, který simulace obsahuje)."""
    return ciselnik_pravni_forma
```

### Cvičení

::exc[excs/pravni-forma]
