## Úvod do FastAPI

Zatím jsme z Pythonu data jen stahovali - posílali jsme `GET` requesty na cizí servery a zpracovávali jejich odpovědi. Dnes si zkusíme roli obrátit: vytvoříme vlastní server, který bude na requesty odpovídat. Takovému serveru se říká *API* (Application Programming Interface) a my ho postavíme pomocí frameworku *FastAPI*.

FastAPI je moderní Python framework určený přesně k tomuto účelu. Nainstalujeme ho spolu s balíčkem `uvicorn`, který slouží jako webový server, jenž naši aplikaci spustí:

```shell
pip install fastapi uvicorn
```

Na Windows použijeme `pip`, na macOS a Linuxu `pip3`.

### Minimální aplikace

Představ si, že chceš vytvořit jednoduchou službu, která na dotaz odpoví pozdravem. Vytvoř soubor `main.py` s tímto obsahem:

```py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"zprava": "Server funguje!"}
```

Aplikaci spustíme příkazem v terminálu:

```shell
uvicorn main:app --reload
```

Přepínač `--reload` zajistí, že se server automaticky restartuje pokaždé, když uložíš změnu v kódu - praktické při vývoji.

Po spuštění uvidíš v terminálu výstup podobný tomuto:

```shell
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

**POZOR!** Terminál, ve kterém běží `uvicorn`, je blokovaný - server v něm běží a čeká na requesty. Abys mohl psát další příkazy, potřebuješ otevřít druhý terminál. Ve VS Code to uděláš kliknutím na ikonku `+` v panelu terminálu (nebo zkratkou `Ctrl+Shift+\``). Oba terminály pak běží vedle sebe.

### Otevření v prohlížeči

Přejdi v prohlížeči na adresu `http://127.0.0.1:8000`. Uvidíš odpověď serveru ve formátu JSON:

```json
{"zprava": "Server funguje!"}
```

FastAPI automaticky vygeneruje i interaktivní dokumentaci. Přejdi na adresu `http://127.0.0.1:8000/docs` a uvidíš přehled všech endpointů, které tvoje API nabízí. Každý si tam můžeš rovnou vyzkoušet kliknutím na tlačítko "Try it out".

### Ověření pomocí knihovny requests

Jak jsme viděli u stahování dat z cizích API, na posílání HTTP requestů v Pythonu slouží knihovna `requests`. Stejně ji použijeme i na testování našeho vlastního serveru.

Ve druhém terminálu (server stále běží v tom prvním) spusť Python nebo vytvoř soubor `test.py`:

```py
import requests

response = requests.get("http://127.0.0.1:8000")
print(response.status_code)
print(response.json())
```

```shell
200
{'zprava': 'Server funguje!'}
```

Stavový kód `200` znamená, že request proběhl úspěšně. Metoda `.json()` převede tělo odpovědi ze JSON řetězce na Python slovník - přesně jako při stahování dat z cizích API.

**Poznámka:** Adresa `127.0.0.1` je speciální adresa, která vždy odkazuje na tvůj vlastní počítač. Říká se jí také *localhost*. Server tedy běží lokálně a je dostupný jen z tvého počítače, ne z internetu.
