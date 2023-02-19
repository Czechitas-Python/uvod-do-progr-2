with open("battles.tsv", encoding="utf-8") as soubor:
    radky = soubor.readlines()

SL_UTOCNIK_PRVNI = 5
SL_UTOCNIK_POSLEDNI = 8

utocnici = {}
for radek in radky[1:]:
    radek = radek.split("\t")
    for utocnik in radek[SL_UTOCNIK_PRVNI:SL_UTOCNIK_POSLEDNI + 1]:
        if utocnik != "":
            utocnici[utocnik] = utocnici.get(utocnik, 0) + 1
print(utocnici)

import pandas
data = pandas.read_csv("battles.tsv", sep="\t")

data = pandas.concat([data["attacker_1"], data["attacker_2"], data["attacker_3"], data["attacker_4"]])
data = data.value_counts()
print(data)
