## Čtení na doma: Vývojářky podle Eurostatu

Uvažujme data o počtech žen v ICT v evropských státech. Data si můžeš stáhnout přímo [z webu Eurostatu](https://ec.europa.eu/eurostat/databrowser/view/isoc_sks_itsps/default/table?lang=en&category=isoc.isoc_sk.isoc_sks.isoc_skslf). Stažená data jsou v souboru [estat_isoc_sks_itsps_filtered_1.tsv](assets/estat_isoc_sks_itsps_filtered_1.tsv).

Data jsou ve formátu TSV. Formát je podobný CSV, jen je jako oddělovač použitý tabulátor místo čárky.

::fig[]{src=assets/eurostat-stazeni-1.png size=50}

```python
data_eurostat = []
with open("estat_isoc_sks_itsps_filtered_1.tsv", encoding="utf-8") as soubor:
    for radek in soubor:
        radek = radek.split("\t")
        data_eurostat.append(radek)
```

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
            hodnota_cislo = float(hodnota.strip(" :bdeu\n"))
            vyvoj_cr.append(hodnota_cislo)
```

Možná bylo zajímavé podívat se na ostatní státy. Podíváme se na vývoj v jednotlivých zemích. Vezememe vždy počáteční a poslední hodnotu časové řady a spočítáme rozdíl mezi nimi.

::fig[]{src=assets/eurostat-stazeni-2.png size=50}


```python
zmena_dle_zeme = {}

def ziskej_cislo(retezec):
    retezec = retezec.strip(" :bdeu\n")
    if len(retezec):
        return float(retezec)

for radek in data_eurostat[1:]:
    zeme = radek[0].split(",")[-1]
    cislo_zacatek = ziskej_cislo(radek[1])
    cislo_konec = ziskej_cislo(radek[-1])
    if cislo_zacatek and cislo_konec:
        zmena_dle_zeme[zeme] = round(cislo_konec - cislo_zacatek, 2)
```

Výsledek uložíme do souboru ve formátu json.


```python
with open("ict_female_change.json", "w", encoding="utf-8") as soubor:
    json.dump(zmena_dle_zeme, soubor, indent=4)
```

Nyní nás bude zajímat, jak se změnil absolutní počet pracovníků v ICT sektoru. Žen totiž mohlo přibýt hodně, ale současně přibylo hodně mužů. Použijeme nyní soubor (estat_isoc_sks_itsps_filtered_2.tsv)[estat_isoc_sks_itsps_filtered_2.tsv]. Krása programování spočívá v tom, že na nová data můžeme použít ten samý program. Výsledkem nyní bude změna počtu žen v tisících.

Stačí upravit první část programu a vložit tam nové jméno souboru. Zbytek programu může zůstat stejný. V seznamu `vyvoj_cr` tentokrát budeme mít počet žen pracujících v ICT v tisících a ve slovníku `zmena_dle_zeme` změnu počtu žen pracujících v ICT opět v tisících.

```python
data_eurostat = []
with open("estat_isoc_sks_itsps_filtered_2.tsv", encoding="utf-8") as soubor:
    for radek in soubor:
        radek = radek.split("\t")
        data_eurostat.append(radek)

```
