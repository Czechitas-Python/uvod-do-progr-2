---
title: Zpřeházená písmena
demand: 4
---

Slovo je stále možné pohodlně přečíst, když jsou pomíchaná písmena. Stačí, když první a poslední písmeno je na své pozici zachováno. Napiš funkci, která bude mít jako vstupní parametr slovo a vrátí slovo, kde zpřehází všechny znaky kromě prvního a posledního.

Nápověda: `random.shuffle()`

Super bonus: Napiš program, který takovou funkci využije na delší text více slov.

```py
text = '''Slovo je stále možné pohodlně přečíst, když jsou pomíchaná písmena.
Stačí, když první a poslední písmeno je na své pozici zachováno. Napiš funkci,
která bude mít jako vstupní parametr slovo a vrátí slovo, kde zpřehází všechny
znaky kromě prvního a posledního.
'''
```

Výstup:

```shell
Slvoo je sátle mnžoé pdhlnooě pseířčt, když jsou pcnhíoamá psímnea. 
Stčaí, kydž pvrní a ponsldeí pmínseo je na své pozcii znaáhvoco. Nipaš fcnkui, 
kretá bude mít jkao vsntpuí paaremtr solvo a vátrí solvo, kde zhpezáří všhecny 
zanky krmoě pírhnvo a plísoednho.
```

:::solution
```py
import random


def shuffle_word(word):
    if word.endswith(".") or word.endswith(","):
        interpunction = word[-1]
        word = word[:-1]
    else:
        interpunction = ""
    if len(word) <= 3:
        return f"{word}{interpunction}"
    else:
        shuffled_part = list(word[1:-1])
        random.shuffle(shuffled_part)
        shuffled_part = "".join(shuffled_part)
        return f"{word[0]}{shuffled_part}{word[-1]}{interpunction}"


text = '''Slovo je stále možné pohodlně přečíst, když jsou pomíchaná písmena.
Stačí, když první a poslední písmeno je na své pozici zachováno. Napiš funkci,
která bude mít jako vstupní parametr slovo a vrátí slovo, kde zpřehází všechny
znaky kromě prvního a posledního.
'''

for row in text.split("\n"):
    for item in row.split(" "):
        print(shuffle_word(item), end=" ")
    print()
```
:::
