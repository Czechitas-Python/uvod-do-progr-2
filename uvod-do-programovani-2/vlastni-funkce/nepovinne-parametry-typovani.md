## Nepovinné parametry a typování

### Nepovinné parametry

Na příkladu funkce `round` jsme viděli, že u některých funkcí není třeba vyplňovat všechny parametry. Vraťme se k funkci `kilometry_na_mile()`. Vedle "klasické" míle existuje ještě námořní míle, která je o něco "delší" (má přesně 1.852 kilometru). Namísto vytvoření nové funkce rozšíříme stávající funkci `kilometry_na_mile()` o nepovinný parametr `namorni`, který bude mít hodnotu `True` anebo `False`. Protože práce s klasickou mílí je mnohem častější než práce s námořní, nastavíme výchozí hodnotu parametru `namorni` na `False`.

```py
def mile_na_kilometry(mile, namorni=False):
    if not namorni:
        return mile * 1.609344
    else:
        return mile * 1.852

london_oxford_km = mile_na_kilometry(59.7)
belfast_new_york = mile_na_kilometry(2758.13, True)
```


### Typování funkcí

Python patří mezi *dynamicky typové jazyky*, což znamená, že při vytvoření proměnné neříkáme, jaký typ hodnoty do ní budeme ukládat. Od verze 3.5 ale podporuje `typing`. Můžeme tedy říct, jaký typ hodnoty by *měla obsahovat* nějaká proměnná, Python to však nekontroluje a neukončí program s chybou, pokud do proměnné vložíme hodnotu jiného typu. Typování ale funguje jako nápověda a především vývojová prostředí, která pak umějí vývojářům a vývojářkám lépe napovídat při psaní programů a případně je upozornit, pokud plánují do proměnné vložit něco, co tam nepatří.

Níže je příklad funkce `mile_na_kilometry()` s typováním. Typovat můžeme jednotlivé parametry i návratovou hodnotu, jejíž typ je za "šipkou" `->`.

```py
def mile_na_kilometry(mile: float, namorni: bool = False) -> float:
    if not namorni:
        return mile * 1.609344
    else:
        return mile * 1.852
```

Chceme-li, aby nás VS Code na nesprávné používání typů hodnot při volání funkcí upozornila, můžeme do nastavení přidat následující možnost.

```
"python.analysis.typeCheckingMode": "basic"
```

Následující volání funkce se pak VS Code určitě líbit nebude.

```py
belfast_new_york = mile_na_kilometry(2758.13, "nazdar")
```
