## Chyby v programu

Mnohokrát jsme se již setkali s tím, že náš program neudělal, co jsme si mysleli, a skončil s chybovou hláškou. V tuto chvíli je nejdůležitější nepanikařit a v klidu si přečíst co nám Python interpret říká. Drtivá většina základních chyb nejsou žádné záludnosti a Python interpret nám často přímo radí, jak chybu opravit. Důležité je nemít z těchto chyb špatný pocit. Programování je často neustálé zkoušení různých pokusů dokud to nebude dělat to, co chceme.

Chybové hlášky jsou taky ta lepší varianta chyby. Pokud nám ji Python vypíše a skončí, tak jistě víme, že je něco špatně. Mnohem hůř se hledají chyby v programu, který Python interpret vyhodnotí jako syntakticky a sémanticky správný, ale ve skutečnosti vůbec nedělá to, co si myslíme, že má dělat.

V ostatních programovacích jazycích můžete narazit na obdobné chyby, jaké si popíšeme níže. Jazyky se ale liší v tom, na které situace reagovat vypsáním chyby a které jen "mlčky" přejdou. Pokud bychom například chtěli přečíst hodnotu seznamu s příliš vysokým indexem, Python zobrazí chybu `IndexError`. JavaScript by ale v obdobné situaci (čtení hodnoty z pole s příliš vysokým indexem) vrátil hodnotu `undefined` a program by pokračoval. To na jednu stranu může znít lákavě, na druhou stranu se program může v určité situaci chovat nekorektně a pokud není chyba odhalena během vývoje a testování, můžou na ni narazit až uživatelé a uživatelky našeho programu.

### Syntaktické chyby

První chybou, kterou zmíníme, je syntaktická chyba, tj. porušení "gramatiky" programovacího jazyka. V případě syntaktické chyby se program ani nespustí.

```py
vek = int(input("Zadej věk: "))
if vek > 15
    print("Vítej")
```

Spuštění programu ihned vypíše chybu, tj. program se ani nezeptá na věk, přestože samotná chyba se vyskytuje až v podmínce.

```shell
    if vek > 15
               ^
SyntaxError: expected ':'
```

Syntatických chyb si obvykle všimne i vývojové prostředí a místo s chybou zvýrazní.

Speciálním případem syntaktické chyby je chyba odsazení, která nastane, pokud např. zapomeneme na odsazení bloku uvnitř podmínky.

```py
vek = int(input("Zadej věk: "))
if vek > 15:
print("Vítej")
```

Pro Python je odsazení řádků klíčové, protože se podle něj orientuje. Z toho důvodu se program ani nespustí a vypíše chybu.

```py
    print("Vítej")
    ^
IndentationError: expected an indented block after 'if' statement on line 2
```

Vše co je shodně odsazeno, patří do jednoho bloku, který končí prvním řádkem, který je odsazen o jedno méně. V tomto případě je problém, že volání funkce `print()` není v bloku odsazeno vůbec. Python ale vyžaduje, aby každá podmínka měla alespoň jeden odsazený řádek. Dále dbej na správné nastavení editoru a nemíchej odsazování různým počtem mezer nebo tabulátorů. Pozor na kód, který kopíruješ z internetu!

### Chyby v logice programu

Níže máme příklady chyb, které musíme opravit, protože by jinak vždy vedly k předčasnému ukončení běhu programu.

Pokud provádíme operaci nepodporovanou mezi dvěma typy hodnot, program obvykle skončí chybou `TypeError`. Níže jsme například zapomněli na převod proměnné `vek` na číslo, proměnná je tedy stále řetězec (`str`). Python nepodporuje operaci porovnání řetězce a celého čísla (`int`) a program skončí chybou `TypeError`.

```py
vek = input("Zadej věk: ")
# Zde porovnáváme číslo a řetězec
if vek > 15:
    print("Vítej")
```

Níže je výpis chyby.

```shell
    if vek > 15:
       ^^^^^^^^
TypeError: '>' not supported between instances of 'str' and 'int'
```

Program se ale spustil a vypsal dotaz na věk, chyba se projevila až v podmínce. To je typické chování tzv. interpretovaných jazyků. V případě interpretovaných jazyků je program čtený (a převáděný do jazyka nižší úrovně, který je více srozumitelný pro počítač) řádek po řádku a Python tedy na chybu narazí až na řádku 2. Na prvním řádku o žádné chybě zatím neví.

Vedle interpretovaných jazyků existují tzv. kompilované jazyky. Ty provádějí proces kompilace, který vezme celý program a přeloží jej na jazyk nižší úrovně ještě před spuštěním. Kompilované jazyky (např. C\#, Java) by si tedy takové chyby často všimly už při kompilaci, protože by jim došlo, že tento řádek provádí neplatnou operaci a tím pádem program nemůže fungovat. Program by tedy nešel spustit, jako tomu bylo u syntaktické chyby.

Podobná situace nastane, pokud chceme pracovat se neznámou proměnnou.

```py
promenna = 10
print(promenna)  # vypíše 10
print(promena)   # chyba v programu
```

Níže je chybový výpis. Python si v tomto případě dokonce všiml, že v programu je proměnná s velmi blízkým názvem a ptá se nás, jestli jsme nechtěli použít právě tuto proměnnou.

```shell
10
    print(promena)   # chyba v programu
          ^^^^^^^
NameError: name 'promena' is not defined. Did you mean: 'promenna'?
```

`NameError` nastává v momentě, kdy Python narazí na slovo, které nezná. Vzhledem k tomu, že klíčová slova, jako `if`, `else`, `def` nebo `import` všechna Python musí znát, zbývají jako další možnosti názvy našich proměnných, funkcí nebo tříd. Pokud v názvu uděláme překlep, nebo použijeme něco, co jsme si vůbec nedefinovali, Python zahlásí _NameError_ a my musíme tuto chybu v programu opravit.


### Potenciálně nebezpečné situace

Některé řádky kódu nemusí nutně způsobit chybu, jsou ale potenciálně nebezpečné. Toto nebezpečí obvykle souvisí se vstupem informací z "vnějšího světa", např. uživatelským vstupem, čtením ze souboru, stahováním dat z internetu atd.

Pokud například chceme převést uživatelský vstup na číslo, hrozí, že dostaneme na vstupu řetězec obsahující jiné znaky než čísla, např. *text*.

```py
vek = int(input("Zadej věk: "))
if vek > 15:
    print("Vítej")
```

V takovém případě program skončí chybou `ValueError`.

```py
    vek = int(input("Zadej věk: "))
          ^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'test'
```

Na rozdíl od předchozí části k této chybě nedojde vždy, ale pouze v případě, že dostaneme na vstupu nějaké nečíselné znaky. Další častá chyba je čtení indexu ze sekvence (např. ze seznamu nebo řetězce), který už neexistuje.

```py
knihy = ["Problém tří těles", "Temný les", "Vzpomínka na Zemi"]
index = int(input("Zadej index knihy: "))
print(knihy[index])
```

Pokud na vstupu dostaneme číslo vyšší než 2, program skončí chybou `IndexError`.

```py
    print(knihy[index])
          ~~~~~^^^^^^^
IndexError: list index out of range
```

Při práci se slovníky můžeme narazit na `KeyError`.

```py
zvirata = {'dog': 'pes', 'cat': 'kočka'}
klic = input("Zadej zvíře pro překlad: ")
print(zvirata[klic])
```

Pokud zadáme na vstup např. *rat*, program skončí chybou.

```shell
    print(zvirata['rat'])
          ~~~~~~~^^^^^^^
KeyError: 'rat'
```

V případě objektově orientovaného programování můžeme u objektu narazit na `AttributeError`, a to v případě, že se pokoušíme číst neexistující atribut nebo používat neexistující metodu. Při používání modulů můžeme narazit na `ImportError`, která se objeví např. v případě, že importujeme modul z knihovny, kterou nemáme nainstalovanou. Pokud program překročí maximální povolené množství využité paměti, objeví se chyba `MemoryError`.

Specifická chyba, která se využívá například při testování, souvisí s klíčovým slovem `assert`. Klíčové slovo `assert` může být využito např. pro testování funkce. Například pokud je funkce `is_odd` naprogramovaná špatně, může vracet `True` pro sudá čísla namísto pro lichá. Python neví, že toto je chyba, ale můžeme využít test, který ověří, že např. pro číslo 3 vrací funkce hodnotu `True`.

```py
def is_odd(number):
    return number % 2 == 0
assert is_odd(3) == True
```

Pokud funkce vrací něco jiného, program skončí chybou `AssertionError`.

```py
    assert is_odd(3) == True
AssertionError
```

Ve správné verzi programu by totiž měla funkce vypadat takto:

```py
def is_odd(number):
    return number % 2 == 1
```
