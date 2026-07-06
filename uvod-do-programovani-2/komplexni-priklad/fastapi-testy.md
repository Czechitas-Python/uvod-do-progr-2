## Automatické testy API

V části o testování jsme psali *unit testy* - testovali jsme jednotlivé funkce izolovaně, bez závislosti na okolním světě. Dnes si ukážeme jiný typ testu: *integrační test* (integration test). Ten místo volání funkce přímo pošle skutečný HTTP request na běžící server a zkontroluje, co dostane zpět. Testujeme tedy celou cestu: od přijetí requestu přes zpracování dat až po vrácení odpovědi.

### Spuštění serveru z testu

Aby mohl test posílat requesty, musí server při jeho spuštění běžet. Místo abychom ho spouštěli ručně v druhém terminálu, spustíme ho přímo z testu pomocí modulu `subprocess`:

```py
import atexit
import subprocess
import time

import requests

BASE_URL = "http://127.0.0.1:8001"
URL = f"{BASE_URL}/ekonomicke-subjekty-v-be/rest/ekonomicke-subjekty/vyhledat"

process = subprocess.Popen(["uvicorn", "main:app", "--port", "8001"])
atexit.register(process.terminate)
time.sleep(1)
```

`subprocess.Popen` spustí příkaz jako samostatný proces na pozadí - stejně jako kdybychom ho napsali do terminálu, ale Python ho spustí sám a nečeká na jeho dokončení. Server poběží souběžně s testem. Používáme port `8001`, aby se server nepletl s případnou instancí, která už běží na výchozím portu `8000`.

`atexit.register(process.terminate)` zaregistruje funkci, která se zavolá automaticky ve chvíli, kdy Python skončí. Tím zajistíme, že se server po doběhnutí testů vždy ukončí - i kdyby test selhal nebo vyhodil výjimku.

`time.sleep(1)` pozastaví Python na jednu sekundu. Server totiž potřebuje chvilku, než nastartuje a začne přijímat requesty. Bez pauzy by test poslal request dřív, než je server připravený, a dostal by chybu.

### Klíčové slovo assert

Jak jsme viděli v části o unit testech, `assert` ověří, že platí zadaná podmínka. Pokud podmínka neplatí, Python vyhodí výjimku `AssertionError` a test selže:

```py
assert response.status_code == 200   # selže, pokud server vrátí jiný kód
assert data["pocetCelkem"] >= 1      # selže, pokud nejsou nalezeny žádné subjekty
```

Testovací frameworky jako `pytest` výjimku `AssertionError` zachytí a reportují ji jako selhání testu s přehlednou zprávou.

### Samotný test

```py
def test_vyhledavani_vraci_odpovidajici_subjekty():
    response = requests.post(URL, json={"obchodniJmeno": "Czechitas"})
    assert response.status_code == 200
    data = response.json()
    assert data["pocetCelkem"] >= 1
    for subjekt in data["ekonomickeSubjekty"]:
        assert "czechitas" in subjekt["obchodniJmeno"].lower()
```

Test pošle POST request s filtrem `{"obchodniJmeno": "Czechitas"}` a ověří tři věci:

- Server odpověděl kódem `200` - request byl úspěšně zpracován.
- V odpovědi je alespoň jeden subjekt - vyhledávání něco našlo.
- Každý vrácený subjekt skutečně obsahuje slovo "czechitas" v obchodním jménu - server nevrátil nesouvisející výsledky.

Třetí podmínka je klíčová: nestačí zkontrolovat, že server vrátil nějaká data, ale musíme ověřit, že jsou správná.

Stejně důležité je testovat, jak se server chová při neplatném requestu. Vzpomeňme si, že Pydantic validuje tělo requestu automaticky - pokud chybí povinné pole, server vrátí kód `422` (Unprocessable Entity) ještě před tím, než se zavolá naše funkce. Ověříme, že tomu tak skutečně je:

```py
def test_chybejici_pole_obchodni_jmeno():
    response = requests.post(URL, json={})
    assert response.status_code == 422
```

Test pošle prázdné tělo requestu bez pole `obchodniJmeno` a ověří, že server správně odmítl neplatný vstup.

### Cvičení

::exc[excs/vyhledavani-bez-vysledku]
