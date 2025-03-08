## Balíčky z internetu

Internet nabízí obrovské množství frameworků, balíčků a knihoven, které si můžeme přidat do našeho programu, a které výrazně rozšíří možnosti našeho programu a ušetří nám spoustu práce. Řadu z nich můžeme jednoduše nainstalovat pomocí aplikace `pip`. [Web aplikace](https://pypi.org/) současně slouží jako databáze s přehledem dostupných balíčků. Těch je ale obrovské množství, takže projít celou databázi by zabralo příliš mnoho času. Jednodušší je podívat se na přehled nejpoužívanějších balíčků, které získáš např. zadáním dotazu "the most popular python packages" do vyhledávače nebo AI nástroje.

Použití nějakého balíčku v projektu je dobré si rozmyslet. Zde jsou nějaké kritéria, které je dobré vzít v úvahu:

- Popularita a velikost komunity: Obecně platí, že čím je balíček populárnější, tím více různých materiálů (např. blogové články, videa) k němu bude. Pokud narazíte na nějaký problém, s velikostí komunity roste pravděpodobnost, že stejný problém už řešil někdo před vámi a řešení je k dispozici na internetu.
- Dokumentace: Oficiální dokumentace může být cenným zdrojem informací, protože v ní autoři balíčku vysvětlují, jak ho správně používat.
- Aktivní vývoj balíčků: U balíčků, které nejsou aktivně vyvíjeny, hrozí, že přestanou být (nebo možná už nejsou) kompatibilní s novými verzemi Pythonu nebo jinými balíčky. Proto je dobré zkontrolovat datum vydání poslední verze.
- Licence: Některé balíčky mohou být omezeny pro nekomerční užití, placené atd.

Existují i další kritéria (např. pokrytí automatickými testy, potenciální zranitelnost kód, výkon atd.).

### Příklad balíčku

Vyzkoušíme si práci s balíčkem `Faker` (česky "Padělač"). Balíček slouží ke generování náhodných údajů, například umí generovat jména, adresy, názvy firem a další. Balíček se dá využít například k vytváření dat pro ukázkovou nebo tréninkovou verzi aplikace, generování dat pro testování, anonymizaci dat, tvorbu simulací a počítačových her a další.

Na Windows napíšeme příkaz

```
pip install Faker
```

Na MacOS a Linuxu použijeme příkaz

```
pip3 install Faker
```

Základní informace o balíčku jsou na webu [pypi.org](https://pypi.org/project/Faker/). Zdrojový kód balíčku si můžeme prohlédnout [na GitHubu](https://github.com/joke2k/faker). A dokumentace balíčku je dispozici na webu [readthedocs.io](https://faker.readthedocs.io/en/stable/).

Zkusme si nejprve pustit ukázku, která je na stránce [pypi.org](https://pypi.org/project/Faker/).

```py
from faker import Faker
fake = Faker()

fake.name()
# 'Lucy Cechtelar'

fake.address()
# '426 Jordy Lodge
#  Cartwrightshire, SC 88120-6700'

fake.text()

for _ in range(10):
  print(fake.name())
```

### Cvičení

::exc[excs/ceska-jmena]

#### Bonusy

::exc[excs/humanize]
