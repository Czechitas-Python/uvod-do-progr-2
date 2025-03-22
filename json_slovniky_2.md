# JSON a slovníky

Budeme pracovat s daty o procentuálním počtu [vývojářů a vývojářek software](https://datausa.io/profile/soc/software-developers). Data jsou uložena v souboru [data_vstupni.json](data_vstupni.json). Data načteme pomocí modulu `json`.


```python
import json
with open('data_vstupni.json', encoding='utf-8') as soubor:
    sw_gender_data = json.load(soubor)
```

Strukturu si můžeme [zobrazit graficky](assets/JSON.drawio.svg).

Zkusme si nyní načíst některé hodnoty.


```python
# Nultý slovník s daty
print(sw_gender_data["data"][0])
```

    {'ID Gender': 1, 'Gender': 'Male', 'ID Year': 2020, 'Year': '2020', 'Total Population': 1268944, 'Total Population MOE Appx': 27602.637285017023, 'Record Count': 59010, 'PUMS Occupation': 'Software developers', 'ID PUMS Occupation': '151252', 'Slug PUMS Occupation': 'software-developers'}



```python
# Kterého roku se týká nultý slovník?
print(sw_gender_data["data"][0]["Year"])
```

    2020


Dále můžeme zjistit například:
- Kolik lidí (klíč `Total Population`) máme v posledním záznamu?
- Kterého pohlaví se poslední záznam týká?
- Je taky dobré zkontrolovat, zda se nám tam nevloudilo nějaké jiné povolání. Jaké povolání (`PUMS Occupation`) je u předposledního záznamu?
- Pokud budeme chtít data veřejně prezentovat, určitě bude dobré uvést zdroj (`source_name`).

V další části budeme chtít sledovat vývoj relativního počtu žen na dané pozici. Služba nám poskytuje (absolutní) počet lidí, proto si relativní počet musíme vypočítat sami. K tomu se nám bude hodit transformovat data do následující tabulky. Využijeme k tomu dvourozměrný slovník. Klíči vnějšího slovníku budou roky a klíči vnitřního slovníku pohlaví.

Data máme nyní v tomto formátu (uvažuji pouze sloupečky, které nás zajímají):

| Year | Gender | Count    |
|------|--------|----------|
| 2020 | Male   | 1268944  |
| 2020 | Female | 295706   |
| 2019 | Male   | 1145155  |
| 2019 | Female | 267806   |
| 2018 | Male   | 1029080  |
| 2018 | Female | 238581   |

Naším cílem je získat data v tomto formátu. Jak se tato operace ve světě datový analýzy nazývá?


| Year | Male     | Female   |
|------|----------|----------|
| 2020 | 1268944  | 295706   |
| 2019 | 1145155  | 267806   |
| 2018 | 1029080  | 238581   |

Pro konkrétní uložení dat v tomto formátu využijeme

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

Všimni si, že dvourozměrný slovník mám předpřipravený. Taková ruční příprava by byla pro delší časovou řadu nepraktická. Jak to můžu udělat bez ní?


```python
data_zapis = {2020: {}, 2019: {}, 2018: {}}
for item in sw_gender_data["data"]:
    year = item["ID Year"]
    gender = item["Gender"]
    data_zapis[year][gender] = item["Total Population"]
print(data_zapis)

with open('data_zapis_2.json', "w", encoding='utf-8') as soubor:
    json.dump(data_zapis, soubor, indent=4)
```

    {2020: {'Male': 1268944, 'Female': 295706}, 2019: {'Male': 1145155, 'Female': 267806}, 2018: {'Male': 1029080, 'Female': 238581}}


Musím si vždy před vložením dat do slovníku zkontrolovat, zda už tam daný klíč je. Pokud ne, vložím ho a přidám k němu prázdný vnořený slovník.


```python
data_zapis = {}
for item in sw_gender_data["data"]:
    year = item["ID Year"]
    gender = item["Gender"]
    if year not in data_zapis:
        data_zapis[year] = {}
    data_zapis[year][gender] = item["Total Population"]
print(data_zapis)

with open('data_zapis_2.json', "w", encoding='utf-8') as soubor:
    json.dump(data_zapis, soubor, indent=4)
```

    {2020: {'Male': 1268944, 'Female': 295706}, 2019: {'Male': 1145155, 'Female': 267806}, 2018: {'Male': 1029080, 'Female': 238581}}


Dále si můžeme vyzkoušet tabulku, ve které bude vývoj poměru žen a mužů v jednotlivých letech. Pro tvorbu tabulky můžeme využít data ve slovníku `data_zapis`.

|Year|Female percentage  |
|----|-------------------|
|2020|0.18899178730067429|
|2019|0.18953530918404685|
|2018|0.18820567959415016|


```python
female_percentage = {}
for key, value in data_zapis.items():
    row_percentage = str(value["Female"] / (value["Male"] + value["Female"]))
    female_percentage[key] = row_percentage


with open("data_zapis_3.json", "w", encoding="utf-8") as soubor:
    json.dump(female_percentage, soubor)

```

Můžu zkusit i zápis do CSV.


```python
with open("data_zapis_3.csv", "w", encoding="utf-8") as soubor:
    print("year,country", file=soubor)
    for year, country in female_percentage.items():
        print(f"{year},{country}", sep=",", file=soubor)

```

# Soubory a JSON

Nyní uvažujme data o počtech žen v ICT v evropských státech za roky 2014 až 2012. Data máme tentokrát ve formátu TSV. Načteme je do dvourozměrného seznamu.


```python
data_eurostat = []
with open("isoc_sks_itsps_page_tabular_percentage.tsv", encoding="utf-8") as soubor:
    for radek in soubor:
        radek = radek.split("\t")
        data_eurostat.append(radek)

print(data_eurostat)
```

    [['freq,unit,sex,geo\\TIME_PERIOD', '2014 ', '2015 ', '2016 ', '2017 ', '2018 ', '2019 ', '2020 ', '2021 \n'], ['A,PC,F,AT', '13.4 s', '14.3 s', '17.1 ', '15.7 s', '18.4 ', '20.4 ', '20.3 ', '19.0 b\n'], ['A,PC,F,BE', '15.2 ', '15.1 ', '14.1 ', '15.6 b', '16.8 ', '17.2 s', '17.4 ', '19.6 b\n'], ['A,PC,F,BG', '31.2 s', '30.6 s', '28.7 s', '28.9 s', '29.7 s', '28.1 ', '28.2 ', '28.2 b\n'], ['A,PC,F,CH', '13.8 s', '14.2 ', '15.0 ', '15.2 ', '14.5 ', '16.6 s', '16.3 s', '16.3 b\n'], ['A,PC,F,CY', '15.9 s', '20.8 s', '23.7 s', '18.2 s', '18.8 s', '19.2 s', '18.2 s', '19.3 bs\n'], ['A,PC,F,CZ', '9.9 s', '9.8 s', '10.0 s', '10.1 ', '9.7 ', '10.2 s', '10.3 ', '10.0 b\n'], ['A,PC,F,DE', '16.5 ', '16.3 ', '16.6 ', '16.6 ', '16.8 ', '16.8 ', '17.6 b', '19.0 b\n'], ['A,PC,F,DK', '18.2 s', '20.4 s', '21.1 bs', '20.3 bs', '20.5 s', '21.6 s', '23.0 s', '22.9 bs\n'], ['A,PC,F,EE', '19.4 s', '22.4 s', '20.5 s', '20.3 s', '22.5 ', '23.8 s', '22.7 s', '22.6 bs\n'], ['A,PC,F,EL', '21.6 s', '18.2 s', '17.8 s', '15.8 s', '15.9 s', '20.7 s', '27.7 s', '21.0 b\n'], ['A,PC,F,ES', '18.4 s', '18.1 s', '17.4 s', '16.7 s', '17.5 s', '19.2 s', '19.3 s', '19.4 bd\n'], ['A,PC,F,EU27_2020', '16.3 s', '16.5 s', '17.0 s', '17.2 s', '17.2 s', '17.8 s', '18.5 s', '19.1 bs\n'], ['A,PC,F,FI', '20.8 ', '22.3 ', '21.0 ', '20.4 ', '19.9 ', '21.1 ', '23.3 ', '23.9 b\n'], ['A,PC,F,FR', '16.9 b', '15.8 ', '17.6 ', '18.5 ', '19.2 ', '19.7 ', '20.1 ', '20.9 bd\n'], ['A,PC,F,HR', '14.7 u', '17.2 u', '13.8 u', '14.5 u', '18.2 s', '20.5 s', '18.1 s', '20.8 bs\n'], ['A,PC,F,HU', '11.7 ', '12.1 s', '13.2 s', '9.1 s', '8.6 s', '10.6 ', '12.3 s', '14.0 bs\n'], ['A,PC,F,IE', '21.1 s', '20.2 s', '21.5 s', '21.1 bs', '18.6 s', '21.4 s', '20.7 s', '20.0 bs\n'], ['A,PC,F,IS', '20.5 s', '23.0 s', '21.9 s', '17.0 s', '16.9 s', '19.2 s', '20.9 bs', '24.0 bs\n'], ['A,PC,F,IT', '14.2 s', '14.7 s', '15.4 s', '16.1 s', '15.1 s', '15.1 s', '15.7 s', '16.1 bs\n'], ['A,PC,F,LT', '16.9 u', '20.5 s', '25.1 s', '26.0 s', '25.9 s', '24.3 s', '23.6 s', '23.7 bs\n'], ['A,PC,F,LU', '11.8 s', '13.7 bs', '12.5 s', '11.5 s', '13.6 s', '15.5 s', '20.0 s', '19.7 bs\n'], ['A,PC,F,LV', '25.3 s', '26.6 s', '26.0 s', '24.9 s', '19.1 s', '23.7 s', '22.8 s', '22.6 bs\n'], ['A,PC,F,ME', ': u', ': u', ': u', '29.4 u', '27.6 u', ': u', ': u', ': \n'], ['A,PC,F,MK', '28.8 s', '21.7 s', '27.3 s', '27.0 s', '24.1 s', '24.4 s', '23.3 s', ': \n'], ['A,PC,F,MT', '15.2 s', '17.0 s', '12.3 s', '10.8 s', '17.7 s', '10.9 s', '10.7 s', '25.7 bs\n'], ['A,PC,F,NL', '13.2 ', '13.9 ', '15.0 ', '16.3 ', '15.9 ', '17.3 ', '17.6 ', '17.5 b\n'], ['A,PC,F,NO', '16.6 s', '18.8 s', '17.3 s', '18.7 s', '22.1 s', '20.6 s', '19.4 s', '19.2 bs\n'], ['A,PC,F,PL', '14.0 s', '13.6 s', '14.6 s', '14.8 ', '14.0 ', '14.4 s', '15.0 s', '15.5 bs\n'], ['A,PC,F,PT', '15.2 s', '17.6 s', '17.9 s', '17.6 s', '17.7 s', '17.8 s', '21.2 s', '20.7 b\n'], ['A,PC,F,RO', '21.5 ', '27.3 s', '26.3 ', '25.7 ', '23.7 s', '23.5 s', '26.2 s', '26.0 bs\n'], ['A,PC,F,RS', '15.0 bs', '17.2 s', '20.9 s', '22.3 s', '19.3 s', '21.6 s', '25.0 s', '23.5 b\n'], ['A,PC,F,SE', '19.1 ', '18.9 ', '20.8 ', '20.9 ', '20.9 b', '20.5 s', '21.3 s', '21.9 b\n'], ['A,PC,F,SI', '13.5 s', '16.2 s', '17.3 ', '16.4 s', '16.6 s', '19.5 s', '17.2 s', '16.6 bs\n'], ['A,PC,F,SK', '12.1 s', '11.9 s', '9.7 s', '14.4 s', '13.1 s', '14.0 s', '15.8 s', '14.9 bs\n'], ['A,PC,F,TR', '14.5 bs', '13.8 s', '13.2 s', '13.8 s', '14.6 s', '13.0 s', '16.8 s', ': \n'], ['A,PC,F,UK', '16.5 s', '17.2 s', '16.5 s', '17.6 s', '17.0 s', '17.1 s', ': ', ': \n']]


Nyní si chceme vytáhnou vývoj v rámci České republiky. Údaj o zemi máme ve sloupci na nulté pozici. Sloupec ovšem obsahuje řetězec s větším množstvím informací oddělených čárkami, např. `A,PC,F,CZ`. Význam zaklínadla je následující:

* `A` = annual (roční údaje),
* `PC` = percent (údaje jsou v procentech),
* `F` = female (procenta se týkají žen),
* `CZ` = Česká republika (dvoupísmenná zkratka země).


```python
vyvoj_cr = []

for radek in data_eurostat[1:]:
    zeme = radek[0].split(",")[-1]
    if zeme == "CZ":
        for hodnota in radek[1:]:
            hodnota_cislo = float(hodnota.replace("b", "").replace("u", "").replace("s", "").strip())
            vyvoj_cr.append(hodnota_cislo)

print(vyvoj_cr)

```

    [9.9, 9.8, 10.0, 10.1, 9.7, 10.2, 10.3, 10.0]


Čísla u nás nám moc radost nedělají. Možná bylo zajímavé podívat se na ostatní státy. Podíváme se na vývoj v jednotlivých zemích. Vezememe vždy počáteční a poslední hodnotu časové řady a spočítáme rozdíl mezi nimi.


```python
zmena_dle_zeme = {}

def ziskej_cislo(retezec):
    hodnota_cislo = retezec.replace("b", "").replace("u", "").replace("s", "").replace("d", "").replace(":", "").strip()
    if len(hodnota_cislo) > 0:
        return float(hodnota_cislo)

for radek in data_eurostat[1:]:
    zeme = radek[0].split(",")[-1]
    cislo_zacatek = ziskej_cislo(radek[1])
    cislo_konec = ziskej_cislo(radek[-1])
    if cislo_zacatek and cislo_konec:
        zmena_dle_zeme[zeme] = round(cislo_konec - cislo_zacatek, 2)

print(zmena_dle_zeme)
```

    {'AT': 5.6, 'BE': 4.4, 'BG': -3.0, 'CH': 2.5, 'CY': 3.4, 'CZ': 0.1, 'DE': 2.5, 'DK': 4.7, 'EE': 3.2, 'EL': -0.6, 'ES': 1.0, 'EU27_2020': 2.8, 'FI': 3.1, 'FR': 4.0, 'HR': 6.1, 'HU': 2.3, 'IE': -1.1, 'IS': 3.5, 'IT': 1.9, 'LT': 6.8, 'LU': 7.9, 'LV': -2.7, 'MT': 10.5, 'NL': 4.3, 'NO': 2.6, 'PL': 1.5, 'PT': 5.5, 'RO': 4.5, 'RS': 8.5, 'SE': 2.8, 'SI': 3.1, 'SK': 2.8}


Výsledek uložíme do souboru ve formátu json.


```python
with open("data_zapis_4.json", "w", encoding="utf-8") as soubor:
    json.dump(zmena_dle_zeme, soubor, indent=4)
```

Nyní nás bude zajímat, jak se změnil absolutní počet pracovníků v ICT sektoru. Žen totiž mohlo přibýt hodně, ale současně přibylo hodně mužů. Použijeme nyní soubor (isoc_sks_itsps_page_tabular_thousands.tsv)[isoc_sks_itsps_page_tabular_thousands.tsv]. Krása programování spočívá v tom, že na nová data můžeme použít ten samý program. Výsledkem nyní bude změna počtu žen v tisících.


```python
data_eurostat = []
with open("isoc_sks_itsps_page_tabular_thousands.tsv", encoding="utf-8") as soubor:
    for radek in soubor:
        radek = radek.split("\t")
        data_eurostat.append(radek)

zmena_dle_zeme = {}

def ziskej_cislo(retezec):
    hodnota_cislo = retezec.replace("b", "").replace("u", "").replace("s", "").replace("d", "").replace(":", "").strip()
    if len(hodnota_cislo) > 0:
        return float(hodnota_cislo)

for radek in data_eurostat[1:]:
    zeme = radek[0].split(",")[-1]
    cislo_zacatek = ziskej_cislo(radek[1])
    cislo_konec = ziskej_cislo(radek[-1])
    if cislo_zacatek and cislo_konec:
        zmena_dle_zeme[zeme] = round(cislo_konec - cislo_zacatek, 2)

print(zmena_dle_zeme)
```

    {'AT': 16.8, 'BE': 24.2, 'BG': 7.2, 'CH': 12.2, 'CY': 1.6, 'CZ': 5.9, 'DE': 147.5, 'DK': 15.1, 'EE': 4.3, 'EL': 6.7, 'ES': 53.0, 'EU27_2020': 670.6, 'FI': 13.2, 'FR': 114.9, 'HR': 6.3, 'HU': 8.6, 'IE': 10.0, 'IS': 0.4, 'IT': 34.0, 'LT': 8.5, 'LU': 2.5, 'LV': 1.8, 'MT': 2.4, 'NL': 56.8, 'NO': 8.9, 'PL': 32.7, 'PT': 25.7, 'RO': 22.8, 'RS': 14.6, 'SE': 36.1, 'SI': 3.3, 'SK': 8.5}



```python
vyvoj_dle_zeme = []

def ziskej_cislo(retezec):
    hodnota_cislo = retezec.replace("b", "").replace("u", "").replace("s", "").replace("d", "").replace(":", "").strip()
    if len(hodnota_cislo) > 0:
        return float(hodnota_cislo)
    else:
        return ""

for radek in data_eurostat[1:]:
    zeme = radek[0].split(",")[-1]
    vyvoj_aktualni_zeme = [zeme]
    for hodnota in radek[1:]:
        hodnota = ziskej_cislo(hodnota)
        vyvoj_aktualni_zeme.append(str(hodnota))
    vyvoj_dle_zeme.append(vyvoj_aktualni_zeme)

with open("data_zapis_5.csv", "w", encoding="utf-8") as soubor:
    for radek in vyvoj_dle_zeme:
        print(",".join(radek), file=soubor)
```
