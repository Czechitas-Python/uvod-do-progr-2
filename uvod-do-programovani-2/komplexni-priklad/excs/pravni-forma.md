---
title: Endpoint pro konkrétní právní formu
demand: 2
---

Přidej GET endpoint `/ekonomicke-subjekty-v-be/rest/ciselniky-nazevniky/pravni-formy/{kod}`, který vrátí jednu položku číselníku podle kódu (např. `"101"`). Pokud položka s daným kódem neexistuje, vrať kód `404`.

Každá položka číselníku je slovník s klíčem `"kod"`. Položky najdeš na `ciselnik_pravni_forma["ciselniky"][0]["polozkyCiselniku"]`.

:::solution
```py
@app.get("/ekonomicke-subjekty-v-be/rest/ciselniky-nazevniky/pravni-formy/{kod}")
def najdi_pravni_formu(kod: str):
    """Vrátí jednu právní formu podle kódu."""
    polozky = ciselnik_pravni_forma["ciselniky"][0]["polozkyCiselniku"]
    for polozka in polozky:
        if polozka["kod"] == kod:
            return polozka

    return JSONResponse(
        status_code=404,
        content={
            "chyba": "Právní forma nebyla nalezena.",
        },
    )
```
:::
