---
title: Počet slov
demand: 3
---

Stáhněte si odevzdanou [slohovou práci](assets/praha.txt). Zadání bylo sepsat text pojednávající o našem hlavním městě. Napište program, který spočítá počet slov v tomto textu, abychom věděli, zda bylo zadání formálně splněno. Nechte se vést následujícím návodem.

1. Nechte váš program otevřít soubor a načíst jednotlivé řádky do seznamu
1. Každý řádek převeďte na seznam slov. Slovem se rozumí vše, co je odděleno mezerou nebo novým řádkem
1. Vypište na výstup počty slov na každém řádku
1. Vypište na výstup celkový počet všech slov v souboru

:::solution
```py
lines = []
word_count = []

with open("praha.txt", encoding="utf-8") as file:
    for line in file:
        line_list = line.split()
        lines.append(line_list)
        word_count.append(len(line_list))

all_words = 0
for line in lines:
    all_words += len(line)
print(all_words)
```
:::
