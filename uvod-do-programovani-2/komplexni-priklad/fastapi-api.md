## Vytvoření API obchodního rejstříku

Teď, když víme, jak FastAPI nainstalovat a spustit, postavíme něco konkrétnějšího. Vytvoříme zjednodušenou kopii API obchodního rejstříku ARES, která bude pracovat s daty uloženými ve dvou JSON souborech.

FastAPI umožňuje přidat aplikaci název a popis, které se pak zobrazí v automaticky generované dokumentaci na `/docs`. Parametry předáme přímo při vytváření objektu `FastAPI`:

```py
from fastapi import FastAPI

app = FastAPI(
    title="Simulace API obchodního rejstříku",
    description="Zjednodušená kopie API ARES pro domácí úkol.",
)
```

### Načtení dat

Data máme uložená ve složce `data` ve dvou souborech. Načteme je při startu aplikace do paměti pomocí modulu `json`, který už známe:

```py
import json
from fastapi import FastAPI

app = FastAPI(
    title="Simulace API obchodního rejstříku",
    description="Zjednodušená kopie API ARES pro domácí úkol.",
)

data_dir = "data"

with open(f"{data_dir}/ekonomicke_subjekty.json", encoding="utf-8") as f:
    subjekty = json.load(f)

with open(f"{data_dir}/ciselnik_pravni_forma.json", encoding="utf-8") as f:
    ciselnik_pravni_forma = json.load(f)
```

Kód pro načtení dat píšeme na úrovni modulu - mimo jakoukoliv funkci. Python ho proto spustí jednou při startu serveru, a data pak zůstanou uložená v proměnných `subjekty` a `ciselnik_pravni_forma` po celou dobu běhu aplikace.

**Poznámka:** V reálném API by data nebyla načtená ze souborů do paměti, ale uložená v databázi. Do databáze by server posílal dotazy při každém příchozím requestu a vracel jen ta data, která si klient žádá. My jsme v kurzu s databázemi nepracovali, proto volíme tento jednodušší přístup. Má ale zásadní omezení: skutečný obchodní rejstřík obsahuje záznamy o milionech subjektů - ta by se do paměti běžného počítače prostě nevešla.

### Parametr v URL

Přidáme endpoint, který přijme IČO a vrátí informace o konkrétním ekonomickém subjektu.

Dekorátor `@app.get(...)` říká FastAPI, na jakou URL adresu má funkce reagovat. Pokud část URL uzavřeme do složených závorek, FastAPI ji automaticky předá funkci jako parametr. Tak vypadá náš endpoint:

```py
@app.get("/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}")
def najdi_subjekt_podle_ico(ico: str):
    ...
```

`{ico}` ve stringu `/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}` **není** formátovaný f-string. Jde o šablonu URL, kterou FastAPI interpretuje samo - složené závorky jsou jeho konvence pro pojmenování proměnné části adresy. FastAPI pak hodnotu z URL vytáhne a předá funkci jako argument `ico`.

Pokud tedy pošleš request na adresu `/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/27082440`, FastAPI zavolá `najdi_subjekt_podle_ico(ico="27082440")`.

### JSONResponse a stavové kódy

Když funkce vrátí slovník, FastAPI ho automaticky převede na JSON s kódem `200`, což znamená úspěch. Jenže ne každý request skončí úspěchem - IČO může mít špatný formát nebo nemusí existovat. V takových případech chceme vrátit jiný *stavový kód* (status code), který klientovi řekne, co se stalo.

K tomu slouží `JSONResponse` - na rozdíl od prostého slovníku nám umožňuje stavový kód nastavit explicitně:

```py
from fastapi import FastAPI
from fastapi.responses import JSONResponse
```

Nejčastěji použijeme tyto kódy:

- `400` - Bad Request: klient poslal neplatný požadavek (např. IČO v nesprávném formátu)
- `404` - Not Found: požadovaný zdroj neexistuje (subjekt s daným IČO nebyl nalezen)

```py
@app.get("/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/{ico}")
def najdi_subjekt_podle_ico(ico: str):
    """Vrátí jeden ekonomický subjekt podle IČO."""
    if len(ico) != 8 or not ico.isdigit():
        return JSONResponse(status_code=400, content={"chyba": "IČO musí mít 8 číslic."})

    for subjekt in subjekty:
        if subjekt["ico"] == ico:
            return subjekt

    return JSONResponse(
        status_code=404,
        content={
            "chyba": "Subjekt nebyl nalezen.",
        },
    )
```

Funkce nejdříve ověří, že IČO má správný formát. Metoda `isdigit()` vrátí `True`, pokud řetězec obsahuje pouze číslice - hodí se právě na validaci vstupů od uživatele. Pokud IČO nemá přesně 8 číslic, vrátíme kód `400`.

Pak projdeme seznam subjektů a hledáme shodu s `ico`. Pokud subjekt najdeme, vrátíme ho jako slovník - FastAPI ho automaticky převede na JSON s kódem `200`. Pokud projdeme celý seznam a nic nenajdeme, vrátíme kód `404`.

Přejdi na `http://127.0.0.1:8000/docs` a uvidíš, že dokumentace teď obsahuje název i popis aplikace.
