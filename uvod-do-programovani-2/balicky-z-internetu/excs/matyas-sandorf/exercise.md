---
title: Matyáš Sandorf
demand: 2
---

Matyáš Sandorf, hrdina románu Julese Vernea, byl maďarský vlastenec, který připravoval povstání svého lidu. Zprávy, které si vyměňoval s dalšími spiklenci pomocí poštovních holubů, šifroval s využitím šifrovací mřížky. Ta fungovala na následujícím principu: Uvažujme, že chceme kódovat zprávu o 16 znacích. K zašifrování použijeme čtvercovou mřížku o rozměrech 4x4, která má přesně čtyři otvory (viz obrázek). Do volných otvorů zapíšeme první 4 znaky zprávy. Následně otočíme mřížku o 90 stupňů zapíšeme další 4 znaky. Postup opakujeme ještě dvakrát, čímž zapíšeme všech 16 znaků.

Zašifrovaný text je na obrázku níže, můžeme ho přepsat do řádky.

::fig[]{src=assets/mrizka.png}

Šifra tedy přehází pořadí znaků, ale samotné znaky nijak nemění. Dekódování probíhá obdobným způsobem. Vezmeme matici se zašifrovaným textem a přiložíme na něj mřížku. Pak si vypíšeme 4 písmena, která jsou vidět. Následně otočíme mřížku o 90 stupňů a přepíšeme další písmena atd. Tvůj úkol je rozšifrovat tento text: *GTYJOIROEUBDIATD* Šifrovací mřížka je stejná jako na ilustračním obrázku.

Využij knihovnu [numpy](https://pypi.org/project/numpy/).

```py
import numpy as np
```

Šifrovací mřížku ulož do proměnné pomocí příkazu

```py
coding_matrix = np.array([[1, 0, 0, 0],
        [0, 0, 1, 0],
        [1, 0, 0, 0],
        [0, 1, 0, 0]])
```

Otočení mřížky provedeš pomocí příkazu

```py
coding_matrix = np.rot90(coding_matrix, -1)
```

Musí tam být ta -1, jinak se mřížka otočí obráceně.

Matici, kam si postupně vložíte znaky zašifrovaného řetězce, vytvoř takto:

```py
input_matrix = np.empty([4, 4], dtype=str)
```

A do matice zapisuj takto:

```py
input_matrix[x, y] = hodnota
```
