---
title: Knihy
demand: 2
---

Uvažuj program, který přečte název knížky ze seznamu na základě indexu. Nejprve se zamysli nad tím, jaké různé chyby můžou při spuštění nastat. Z chyb, o kterých jsme si povídali, jsou to dvě. Před spuštěním programu identifikuj řádky, které chybu vyvolají. Pro každou z těchto chyb vytvoř vstup, který ji vyvolá, a vyzkoušej, že se tak opravdu stane. Podívej se na chybu a najdi v něm odkaz na řádek. Je to stejný řádek, jaký jsi předpokládal/a?

```py
knihy = ["Problém tří těles", "Temný les", "Vzpomínka na Zemi"]
index = input("Zadej index knihy: ")
index = int(index)
print(knihy[index])
```

Nyní do programu přidej ošetření pomocí obecné výjimky `Exception`. Na začátek programu umísti break point. Proveď krokování programu pro oba vstupy, které sis připravil/a v první části. Ze kterého řádku programu přejde do bloku `ęxcept`? Jde o stejný řádek pro oba vstupy, nebo se řádek liší?
