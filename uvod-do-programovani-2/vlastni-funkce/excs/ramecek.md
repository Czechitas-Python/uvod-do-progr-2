---
title: Rámeček
demand: 3
---

Napiš funkci, která jako parametr převezme řetězec a vytiskne jej obalen hvězdičkami.

```shell
Zadej slovo: ahoj
********
* ahoj *
********
```

Nápověda: `8 * '*' == '********'`

Bonus: Znak, kterým se má text obalit, bude zadán také jako parametr.

:::solution
```py
def frame(word, character="*"):
    print(character * (len(word) + 4))
    print(f"{character} {word} {character}")
    print(character * (len(word) + 4))

word = input("Zadej slovo: ")
frame(word)
frame(word, "X")
```
:::
