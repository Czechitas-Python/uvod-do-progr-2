## Čtení na doma: Vytvoření velmi jednoduchého chatbota

Vyzkoušíme si naprogramovat velice jednoduchého chatbota, který provozuje vysoká škola v USA. V našem jednoduchém případě zvládá odpovědět pouze na dvě otázky - otázku o školném (fees) a otázku o nabízených kurzech (course).

### Verze 1

První verze umí odpovědět pouze na otázku o školném. V seznamu `patterns_fees` máme příklady otázek, které může uživatel položit. Pokud uživatel položí jednu z otázek ze seznamu, program zobrazí řetězec uložený v proměnné `response_fees`. Jinak zobrazí obecnou odpověď `unknown_question_response`.


```python
patterns_fees = [
  "information about fee",
  "college fee",
  "how much is the fees",
  "fees",
]
response_fees = "The annual tuition fees for undergraduate students is $20,000. Graduate students can expect to pay $25,000 per year."
unknown_question_response = "I'm sorry, I don't have an answer for that at this time. Is there something else I can help you with?"

question = input("Please ask your question: ")
if question in patterns_fees:
    print(response_fees)
else:
    print(unknown_question_response)
```
### Verze 2

Ve verzi 2 přibyla otázka o kurzech, které je možné na univerzitě studovat. Otázky přibyly do samostatného seznamu `patterns_courses` a odpovědi jsme vložili do slovníku.


```python
patterns_fees = [
  "information about fee",
  "college fee",
  "how much is the fees",
  "fees",
]

patterns_courses = [
  "list of courses",
  "list of courses offered",
  "courses",
  "courses offered",
]

responses = {
    "fees": "The annual tuition fees for students is $20,000 per semestr.",
    "courses": "Our university offers Information Technology, Computer Engineering, Mechanical engineering, Chemical engineering, Civil engineering and extc Engineering."
} 
unknown_question_response = "I'm sorry, I don't have an answer for that at this time. Is there something else I can help you with?"

question = input("Please ask your question: ")
if question in patterns_fees:
    print(responses["fees"])
elif question in patterns_courses:
    print(responses["courses"])
else:
    print(unknown_question_response)

```

### Verze 3

V průběhu času můžeme například sbírat otázky, kterým chatbot nerozuměl, a upravovat podle nich naše vstupní data. Abychom kvůli tomu nemuseli zasahovat do programu, můžeme si vstupní otázky vložit do souboru. Soubor obsahuje dva sloupce - `pattern` (vzor pro otázku) a `id` (podle něj dohledáme odpověď).

Soubor si můžeš stáhnout [patterns.csv](assets/patterns.csv).


| pattern                  | id      |
|--------------------------|---------|
| information about fee    | fees    |
| college fee              | fees    |
| how much is the fees     | fees    |
| fees                     | fees    |
| list of courses          | courses |
| list of courses offered  | courses |
| courses                 | courses |
| courses offered          | courses |


```python
lines = []

with open('patterns.csv', encoding='utf-8') as file:
    for line in file:
        line = line.strip().split(",")
        lines.append(line)

responses = {
    "fees": "The annual tuition fees for students is $20,000 per semestr.",
    "courses": "Our university offers Information Technology, Computer Engineering, Mechanical engineering, Chemical engineering, Civil engineering and extc Engineering."
}

question = input("Please ask your question: ")
for row in lines:
    if question == row[0]:
        id = row[1]
        print(responses[id])

```

### Verze 4

Nyní přidáme porovnání řetězců pomocí funkce. Ve funkci můžeme například provádět drobné úpravy řetězců, které zvýší naši šanci poskytnout správnou odpověď (například odstranění zbytečných mezer, otazníku atd.).


```python
def compare_strings(user_input, pattern):
    user_input = user_input.lower()
    user_input = user_input.strip()
    user_input = user_input.replace("?", "")
    if user_input == pattern:
        return True
    else:
        return False

lines = []

with open('patterns.csv', encoding='utf-8') as file:
    for line in file:
        line = line.strip().split(",")
        lines.append(line)

responses = {
    "fees": "The annual tuition fees for students is $20,000 per semestr.",
    "courses": "Our university offers Information Technology, Computer Engineering, Mechanical engineering, Chemical engineering, Civil engineering and extc Engineering."
}

question = input("Please ask your question: ")
for row in lines:
    if compare_strings(question, row[0]):
        id = row[1]
        print(responses[id])
```
