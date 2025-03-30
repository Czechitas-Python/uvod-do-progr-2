## Obecná výjimka

V obsahu souboru ale může být celá řada dalších záludností. Podívej se na obsah souboru níže. Co tam ma nás číhá?

- Délka směny na prvním řádku (číslujeme od 1) nepůjde převést na číslo.
- Na druhém řádku máme již známý problém s dělení nulou.
- Ve třetím řádku je jedna čárka navíc, což způsobí chybu při "rozbalování" do proměnných.
- Ve čtvrtém řádku je naopak o jednu čárku méně.
- V pátém řádku nepůjde převést tržba na číslo.

```
pondělí,2904,4a
úterý,7390,0
středa,6950,8,pršelo
čtvrtek,3300
pátek,10570x,8
sobota,1310,2
neděle,9806,8
```

Pokud se spokojíme pouze s výpisem o chybě, můžeme namísto chyby `ZeroDivisionError` odchytávat obecnou chybu `Exception`. Tato obecná chyba odchytí další chyby, které se v programu můžou vyskytnout, tedy nejen `ZeroDivisionError`, ale i `ValueError`, `IndexError` a řadu dalších. Dokáže odchytit i chybu s neexistujícím souborem nebo nedostatečnými právy pro jeho čtení.

```py
try:
    avg_sales = []
    for line in lines:
        line = line.split(",")
        day, total_sales, hours = line
        hours = int(hours)
        avg = int(total_sales) / int(hours)
        avg_sales.append(avg)
        print(f"Délka směny pro {day} je 0.")
    print(avg_sales)
except Exception:
    print("Chyba při zpracování souboru")
```
