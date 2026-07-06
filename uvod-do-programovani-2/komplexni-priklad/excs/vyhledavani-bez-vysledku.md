---
title: Vyhledávání bez výsledků
demand: 1
---

Přidej test, který ověří, že endpoint pro vyhledávání subjektů správně zvládne případ, kdy zadaný řetězec neodpovídá žádnému záznamu. Pošli request s obchodním jménem `"xyzxyzxyz"` a ověř, že:

- server vrátil kód `200` - i prázdný výsledek je platná odpověď,
- `pocetCelkem` je `0`,
- `ekonomickeSubjekty` je prázdný seznam.

:::solution
```py
def test_vyhledavani_bez_vysledku():
    response = requests.post(URL, json={"obchodniJmeno": "xyzxyzxyz"})
    assert response.status_code == 200
    data = response.json()
    assert data["pocetCelkem"] == 0
    assert data["ekonomickeSubjekty"] == []
```
:::
