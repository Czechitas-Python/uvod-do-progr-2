---
title: Knižní série
demand: 2
---

Uvažuj program, který pracuje se slovníkem, který obsahuje informace o knihách a jejich počtech stránek. Program si od uživatele vyžádá název knihy nebo knižní série a počet stránek, které  uživatel přečte každý den. Poté vypočte, kolik dní bude trvat přečtení celé série:

```py
knihy = {
    "1984": 328,
    "Pán Prstenů": [423, 352, 416],
    "Hornblower": [256, 352, 288, 304],
    "Problém tří těles": [400, 512, 608]
}

nazev = input("Zadej název knižní série: ")
stranek_za_den = int(input("Kolik stran přečteš každý den? "))
stranek_celkem = sum(knihy[nazev])

pocet_dni = stranek_celkem / stranek_za_den
pocet_dni = round(pocet_dni)
print(f"Celou sérii přečteš za {pocet_dni} dní.")
```

Vyzkoušej vstup `1984`. Pro něj program skončí chybou `TypeError: 'int' object is not iterable)`. Zamysli se nad tím, v čem může být probém. V tomto případě není vhodné řešení pomocí výjimky, protože ta by nám pravděpodobně překazila výpočet. Místo toho uprav slovník `knihy` tak, aby fungoval i pro vstup `1984`.

Nyní uvažuj, jaké výjimky může program vyvolat. Z těch, které jsme si ukazovali, jsou to opět 2. Připrav si vstupy, které vyvolají obě chyby. Pak opět doplň ošetření obecné výjimky a pomocí krokování opět ověř, jestli program přejde do bloku `exception` tam, kde to očekáváš.

Nakonec program uprav tak, že jednu jednu chybu odchytíš pomocí pomocí podmínky. Pro druhou dále použij výjimku. Protože nyní může nastat jen jedna chyba, zmeň obecnou výjimku `Exception` na tu specifickou, která nyní může nastat.
