---
title: Zasedačka
demand: 3
---

Níže máš seznam akcí, které se konaly v zasedačce jedné firmy.

```py
akce = [
    "školení - řízení firemních vozidel",
    "jazykový kurz - angličtina",
    "pohovor - Jan Dvořák",
    "pohovor - Antonín Sova",
    "jazykový kurz - němčina",
    "pohovor - Iveta Hájková",
    "pohovor - Ivan Brož",
    "pohovor - Katarína Martináková",
    "setkání se zákazníkem - Metrostav",
    "jazykový kurz - angličtina",
    "školení - vykazování práce",
    "pohovor - Klaudie Moudrusová",
]
```

Napiš program, který zjistí následující:

- Kolik se uskutečnilo pohovorů?
- V jakých jazycích se mohou zaměstnanci firmy vzdělávat?

Při řešení můžeš využít operátor `in` a slicing, případně metodu `split()`

:::solution
```py
akce = [
    "školení - řízení firemních vozidel",
    "jazykový kurz - angličtina",
    "pohovor - Jan Dvořák",
    "pohovor - Antonín Sova",
    "jazykový kurz - němčina",
    "pohovor - Iveta Hájková",
    "pohovor - Ivan Brož",
    "pohovor - Katarína Martináková",
    "setkání se zákazníkem - Metrostav",
    "jazykový kurz - angličtina",
    "školení - vykazování práce",
    "pohovor - Klaudie Moudrusová",
]
pohovory = 0
jazyky = []
for radek in akce:
    if "pohovor" in radek:
        pohovory = pohovory + 1
    if "jazykový kurz" in radek:
        jazyk = radek.replace("jazykový kurz - ", "")
        if jazyk not in jazyky:
            jazyky.append(jazyk)
print(f"Pohovorů: {pohovory}.")
jazyky = ", ".join(jazyky)
print(f"Jazyky: {jazyky}.")
```
:::
