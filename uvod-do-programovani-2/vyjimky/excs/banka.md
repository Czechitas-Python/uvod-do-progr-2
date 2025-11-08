---
title: Banka
demand: 2
---

Nasimulujme si fungování bankovní aplikace, konkrétně žádost o převod peněz z účtu. Na začátku si vytvoř soubor `balance.txt` a do něj vlož nějaké číslo. Toto číslo reprezentuje aktuální zůstatek na účtu.

Přečti hodnotu v souboru, převeď ji na číslo a ulož ji do proměnné `account_balance`. Čtení souboru i převod na číslo ošetři pomocí výjimek. Následně se zeptej uživatele (uživatelky), kolik peněz chce převést na jiný účet. Ošetři pomocí výjimky, že uživatel (uživatelka) zadal(a) číslo. Dále vyvolej `ValueError` v případě, že zadaná částka je záporná nebo vyšší než zústatek na účtu. Pokud je vše v pořádku, spočítej nový zůstatek a zapiš ho do souboru `balance.txt`.
