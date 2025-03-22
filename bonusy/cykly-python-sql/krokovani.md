## Použití krokování

Podobné schéma si můžeme zobrazit ve Visual Studio Code v postupu označeném jako krokování (debuggování). Krokování je podobné například prohlížení si zpomalených záběrů při hokeji. Na zpomaleném záběru je lépe vidět, jak se jednotliví hráči a puk pohybovali. U krokování program zastavíme a poté spuštíme dál po jednotlivých krocích (snímcích). Můžeme se též podívat na aktuálně existující proměnné a jejich hodnoty.

Nejprve je nutné umístit break-point, tj. bod, ve kterém se program (video) zastaví.

::fig[]{src=assets/debugging_01.png}

Poté klikneme na ikonku Run and Debug v levém menu a poté na tlačítko Run and Debug, které se nám zobrazí.

::fig[]{src=assets/debugging_02.png}

Pokud program krokujeme poprvé, musíme vybrat jeho typ. V našem případě volíme Python File.

::fig[]{src=assets/debugging_03.png}

Program se zastaví na začátku cyklu, tj. v break-pointu. Zatím máme pouze proměnnou `prodej_knih`. Posuneme se tedy o jeden krok (snímek) dopředu.

::fig[]{src=assets/debugging_04.png}

Posunutí vpřed provedeme pomocí ikonky šipky s tečkoku (druhá zleva). Pozor na použití správné ikonky! První ikonka pustí program dál až do dalšího break-pointu, případně program doběhne až do konce!

::fig[]{src=assets/debugging_05.png}

Nyní jsme o krok (snímek) dál a vidíme, že vznikla proměnná `radek`. Protože proměnná je seznam, můžeme ji rozkliknout a vidíme hodnoty ja jednotlivých pozicích.

Aktuální pozici nám vyznačuje podbarvení řádku a šipka vlevo u čísla řádku.

::fig[]{src=assets/debugging_06.png size=50}

Visual Studio Code nám tedy zobrazuje stejné informace, které byly na schématu, pouze v graficky jiné podobě.

::fig[]{src=assets/cyklus-prubeh_1_2.drawio.svg}

Podíváme se o dva kroky dále (všimni si, že řádek uvnitř podmínky se nepodtrhne - protože je podmínka nesplněná, Python se řádku uvnitř podmínky vyhne). O dva kroky dále již vidíme čísla pro Brno. Visual Studio v levém panelu zvýrazní, které hodnoty se mezi kroky změnily, což pomáhá v případě, kdy je proměnných hodně.

::fig[]{src=assets/debugging_07.png}

V případě Brna už se podíváme i do vnitřku podmínky, protože výraz v podmínce je vyhodnocen jako pravda.

::fig[]{src=assets/debugging_08.png}
