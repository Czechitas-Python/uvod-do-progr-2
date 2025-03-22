## Čtení na doma: API o vývojářkách

Při práci s REST API využijeme následující postup:

1. Najdeme API, ze kterého chceme data získat. U API potřebujeme znát jeho adresu.
2. Podíváme se, jestli je API volně přístupné či zda vyžaduje registraci. Registrace může být i zdarma, jejím účelem je snaha zabránit přetížení služby velkým množstvím dotazů (existují samozřejmě i placená API).
3. Podíváme se na to, jaká data API nabízí (a v jakém formátu) a pokusíme se v nich zorientovat.
4. Zpracujeme data pomocí Pythonu.

Využijeme data z webu [DataUSA.io](https://datausa.io/), konkrétně data o pozici [vývojář(ka) software](https://datausa.io/profile/soc/software-developers). Data bychom si mohli stáhnout ručně, ale to vyžaduje lidský zásah. API nám umožní automatickou aktualizaci dat, takže se do reportu budou automaticky stahovat nová data.

::fig[]{src=assets/datausa-io-1.png size=50}

Web [DataUSA.io](https://datausa.io/) registraci nevažaduje, můžeme tedy začít API používat. K prohlídnutí formátu dat můžeme použít i webový prohlížeč. Pro Google Chrome je k dispozici doplněk [JSON Formatter
](https://chrome.google.com/webstore/detail/json-formatter/bcjindcccaagfpapjjmafapmmgkkhgoa?hl=en), který data zformátuje do přehlednější podoby. Prohlížeč Mozilla Firefox umí data hezky zformátovat automaticky. Další možností je použití online nástrojů jako [JSON Formatter](https://jsonformatter.curiousconcept.com/), do kterého překopírujeme textový výstup. (On-line nástroje bychom neměli používat pro citlivá data, např. data o zákaznících firmy).

::fig[]{src=assets/datausa-io-2.png size=50}

```python
import requests
import json

response = requests.get("http://fargo-app.datausa.io/api/data?drilldowns=Year,Gender&measures=Total Population,Total Population MOE Appx&Workforce Status=true&Nation=01000US&Detailed Occupation=151252&Record Count>=5")
# Převedeme data na slovník
sw_gender_data = json.loads(response.text)
```

Data si před zpracováním můžeme uložit. To je praktické hlavně u větších objemů dat a pomalejších API. Většinou je rychlejší načíst data ze souboru na disku než z internetu. V některých případech může být navíc počet přístupů na API omezen.


```python
with open("data_zapis.json", "w", encoding="utf-8") as soubor:
    json.dump(sw_gender_data, soubor, indent=4)
```

Při použití modulu `json` je *úplně jedno*, jestli data stahujeme z internetu nebo nahráváme ze souboru. Data se vždy převedou do stejné struktury (slovníku) a pracujeme se s nimi stejně. Stejně bychom se slovníkem pracovali i v případě, že bychom si jej zapsali do programu sami.

Soubor je zde: [data_zapis.json](assets/data_zapis.json)


```python
with open('data_zapis.json', encoding='utf-8') as soubor:
    sw_gender_data = json.load(soubor)
```

Zkusme si nyní načíst některé hodnoty.

```python
# Nultý slovník s daty
print(sw_gender_data["data"][0])
# Kterého roku se týká nultý slovník?
print(sw_gender_data["data"][0]["Year"])
```

Zkusme data uložit v nějakém přehlednějším formátu, abychom z nich snaději vytvořili vizualizace (např. v Tableau nebo Power BI). Výstup by měl vypadat jako tabulka níže.

| Gender | Year | People   |
|--------|------|----------|
| Male   | 2022 | 1416848  |
| Female | 2022 | 313469   |
| Male   | 2021 | 1287477  |
| Female | 2021 | 282186   |
| Male   | 2020 | 1162491  |
| Female | 2020 | 256190   |
| Male   | 2019 | 1051297  |
| Female | 2019 | 229473   |
| Male   | 2018 | 944390   |
| Female | 2018 | 204170   |

Využijeme formát CSV, tj. jednotlivé hodnoty oddělíme čárkou.

```python
data_zapis = []
for item in sw_gender_data["data"]:
    radek_zapis = [item["Gender"], item["Year"], str(item["Total Population"])]
    data_zapis.append(radek_zapis)

with open("data_zapis.csv", "w", encoding="utf-8") as soubor:
    zahlavi = "Gender,Year,People"
    print(zahlavi, file=soubor)
    for radek_zapis in data_zapis:
        retezec = ",".join(radek_zapis)
        print(retezec, file=soubor)
```

Pojďme si zkusit zapsat data ve formátu JSON. Budeme chtít zapsat data do dvourozměrného slovníku, kde jako klíče využijeme roky a jako klíče vnořených slovníků budou pohlaví.

```json
{
    "2020": {
        "Male": 1268944,
        "Female": 295706
    },
    "2019": {
        "Male": 1145155,
        "Female": 267806
    },
    "2018": {
        "Male": 1029080,
        "Female": 238581
    }
}
```

Data můžeme transformovat a zapsat opět s využitím Pythonu.

```python
data_zapis = {}
for item in sw_gender_data["data"]:
    year = item["Year"]
    gender = item["Gender"]
    if year not in data_zapis:
        data_zapis[year] = {}
    data_zapis[year][gender] = item["Total Population"]

with open('data_zapis_2.json', "w", encoding='utf-8') as soubor:
    json.dump(data_zapis, soubor, indent=4)
```

Dále si můžeme vyzkoušet tabulku, ve které bude vývoj poměru žen a mužů v jednotlivých letech. 

| Year | Female percentage |
|------|-------------------|
| 2022 | 0.18116275803797802 |
| 2021 | 0.1797748943563045  |
| 2020 | 0.18058323188933947 |
| 2019 | 0.1791680004996994  |
| 2018 | 0.17776171902207982 |

Pro tvorbu tabulky můžeme využít data ve slovníku `data_zapis`.

```python
female_percentage_list = []
for key, value in data_zapis.items():
    row_percentage = str(value["Female"] / (value["Male"] + value["Female"]))
    row = [key, row_percentage]
    female_percentage_list.append(row)


with open("data_zapis_2.csv", "w", encoding="utf-8") as soubor:
    zahlavi = "Year,Female percentage"
    print(zahlavi, file=soubor)
    for radek_zapis in female_percentage_list:
        retezec = ",".join(radek_zapis)
        print(retezec, file=soubor)

```
