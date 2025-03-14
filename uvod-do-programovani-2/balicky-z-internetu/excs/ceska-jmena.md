---
title: Česká jména
demand: 2
---

Pro náš program by se spíše hodila česká jména. Zkus si otevřít [část o lokalizaci na GitHubu](https://faker.readthedocs.io/en/stable/#localization). Všimni si, že při vytváření objektu `fake` z třídy `Faker` je použit parametr `"it_IT"`, který udává, pro jaký jazyk a "lokálního nastavení" mají být data generována. Namísto italských bychom preferovali česká. Podívej se na [stránku o českém lokálním nastavení](https://faker.readthedocs.io/en/stable/locales/cs_CZ.html). Jaký je kód nastavení pro češtinu? Formát názvu je stejný jako pro italštinu, tj. řetezec složený ze dvou malých písmen, podtržítka a dvou velkých písmen. Určitě ho najdeš rychle, je přímo v nadpisu stránky.

Zkusme se nyní podívat na to, co přesně česká lokalizace "padělače" umí. Uvažujme například, že generujeme tréninkovou verzi aplikace pro správu kurzů Czechitas. Standardní metoda `.name()`, která náhodně generuje mužská i ženská jména, není úplně to pravé. Podívej se na metodu, která [generuje pouze ženská jména](https://faker.readthedocs.io/en/stable/locales/cs_CZ.html#faker.providers.person.cs_CZ.Provider.name_female) a vyzkoušej ji ve svém programu. Nakonec zkus vygenerovat i nějaké [adresy](https://faker.readthedocs.io/en/stable/locales/cs_CZ.html#faker.providers.address.cs_CZ.Provider.address).

:::solution
```py
from faker import Faker
fake = Faker("cs_CZ")

for _ in range(10):
  print(fake.name_female())
  print(fake.address())
```
:::
