---
title: Zátopek
demand: 2
---

Níže jsou data běžců maratonu, který se beží na počest Emila Zátopka. Závod se běží ve Stromovce a úspěšnému dokončení závodu je třeba absolvovat 8 kol po cca 5.27 kilometrech (celkem 42.195 km). Na začátku vnořeného seznamu je startovní číslo běžce nebo běžkyně, ostatní položky označují časy v jednotlivých kolech.

Tvým úkolem je data zpracovat a pro každého z běžců a běžkyň vypsat níže uvedené informace. Pro zpracování je vhodné data převést na číslo, např. na minuty. Pokud výpis není celé číslo, proveď zaokrouhlení na dvě desetinná místa.

- Občas se stane, že někdo ze závodníků "přepálí start", tj. běží na začátku příliš rychle a poté jim docházejí síly. Spočítej rozdíl mezi časem prvního a posledního kola.
- Profesionálové někdy doporučují běžet prvních cca 30 km stálým tempem. Uvažuj tedy prvních pět kol závodu a urči čas nejrychleji a nejpomaleji zaběhnutého kola. Nakonec vypiš rozdíl mezi těmito dvěma časy.
- Nyní uvažuj všechna kola závodu. Pro každého běžce vypiš číslo jeho nejrychlejšího a číslo jeho nejpomalejšího kola. Při výpisu uvažuj počítání od jedničky.
- Spočítej průměrnou rychlost v kilometrech za hodinu. K tomu využij vzorec "42.195 / čas v hodinách".

Dále spočítej následující statistiky pro všechny běžce.

- Kolik běžců a běžkyň zaběhlo nejrychleji první kolo a nejpomaleji poslední kolo? Výsledek vypiš v počtech i procentech.

### Nápověda

V tomto cvičení budeš pravděpodobně potřebovat najít prvek v seznamu. K tomu slouží metoda, která na kodim.cz není, ale v Pythonu existuje. Zkus to Google zadat "find element in list python", případně zadej dotaz "How can I get an index of an element in Python list?" do ChatGPT.

```py
data = [
    ['1', '19:08.4;19:00.8;19:01.4;18:43.8;19:31.8;20:06.6;21:35.9;22:37.2'],
    ['84', '19:45.0;19:56.4;20:15.3;20:42.4;21:24.5;22:42.4;23:14.4;23:33.0'],
    ['2', '19:59.2;20:28.7;20:48.5;21:30.1;22:12.6;22:29.7;23:15.1;23:01.5'],
    ['20', '22:14.6;22:06.0;22:10.1;22:01.1;22:11.2;22:04.2;21:48.7;21:24.6'],
    ['73', '22:01.2;22:02.1;22:08.4;22:29.2;22:32.5;22:53.7;23:11.0;22:50.3'],
    ['13', '20:49.0;20:44.1;20:46.6;21:52.0;22:41.5;23:55.8;26:22.4;27:41.0'],
    ['5', '21:51.9;21:54.4;22:00.5;22:00.1;23:22.0;24:05.6;23:54.4;26:42.6'],
    ['115', '23:18.6;23:38.5;24:08.9;24:29.5;25:09.8;26:42.8;28:04.0;26:03.7'],
    ['120', '24:32.9;24:49.5;25:07.4;25:27.4;25:46.7;25:51.7;26:46.5;26:15.4'],
    ['72', '24:46.3;25:27.6;25:15.2;25:09.8;26:23.0;26:01.3;26:22.8;25:27.3'],
    ['99', '24:16.2;24:59.1;24:14.8;25:47.2;26:29.3;26:43.1;26:57.9;26:24.6'],
    ['83', '24:04.5;24:15.7;24:14.5;24:16.6;25:00.2;26:56.3;29:28.2;28:26.8'],
    ['414', '26:05.6;26:10.5;25:19.3;25:43.5;26:14.2;26:34.5;27:08.3;26:37.9'],
    ['38', '22:45.8;22:57.8;23:56.5;24:52.3;26:06.5;28:14.3;34:14.7;29:31.2'],
    ['49', '26:33.3;27:03.1;26:47.4;27:24.9;26:58.9;27:05.7;27:37.6;26:58.3'],
    ['76', '25:02.7;25:34.8;25:39.4;26:28.9;28:08.1;28:36.4;28:42.1;29:02.8'],
    ['4', '24:43.6;24:55.7;25:12.9;26:09.1;27:45.2;30:12.2;30:48.0;28:47.4'],
    ['62', '28:07.6;27:49.4;27:15.9;27:53.9;28:55.2;27:40.4;27:47.1;27:52.1'],
    ['78', '24:43.4;26:02.6;28:16.7;26:58.6;28:18.2;29:33.0;30:19.5;30:11.5'],
    ['18', '25:56.3;26:34.4;26:32.2;26:01.9;28:06.0;28:35.2;33:21.5;30:46.8'],
    ['106', '27:41.0;27:28.4;27:20.7;27:59.7;28:53.5;28:53.2;30:01.1;29:03.1'],
    ['48', '27:57.1;29:10.9;28:14.2;29:25.2;29:51.8;30:22.2;32:10.9;31:03.1'],
    ['55', '27:49.8;28:00.6;28:24.8;29:11.3;29:41.4;31:06.4;32:11.9;32:21.9'],
    ['123', '26:54.6;27:57.3;28:45.4;29:06.1;29:53.0;31:33.4;31:59.9;32:42.6'],
    ['103', '26:53.9;28:06.2;28:40.2;29:07.1;30:38.1;31:58.5;32:49.9;32:25.1'],
    ['85', '28:07.4;27:46.4;27:22.4;28:51.8;30:07.1;33:07.2;34:09.0;33:56.2'],
    ['56', '30:06.7;30:25.6;29:50.4;30:01.5;30:22.8;31:42.5;31:25.6;32:34.9'],
    ['53', '30:07.6;30:25.3;29:50.5;30:00.9;30:23.0;31:42.6;31:26.2;33:27.4'],
    ['129', '27:05.0;26:48.7;28:00.6;32:05.8;32:24.4;32:22.0;35:05.8;35:05.2'],
    ['50', '27:47.0;27:19.9;27:22.6;28:17.0;29:16.1;31:04.6;39:51.3;41:11.3'],
    ['81', '30:17.2;31:05.2;30:27.0;30:57.3;31:41.3;31:54.9;34:11.8;32:24.6'],
    ['63', '30:02.3;30:06.2;30:10.8;30:21.2;32:21.2;32:07.9;32:52.1;35:47.3'],
    ['59', '30:11.2;28:53.4;28:55.2;29:59.9;30:35.2;33:59.0;37:29.5;35:44.5'],
    ['54', '26:44.3;26:26.4;26:11.2;26:57.2;37:43.8;29:09.9;41:49.5;41:39.9'],
    ['80', '29:36.1;29:34.9;29:28.8;30:03.6;31:11.3;35:34.6;35:27.0;36:36.3'],
    ['121', '26:47.5;27:24.2;28:20.0;29:53.9;32:48.5;35:46.9;39:05.3;40:17.2'],
    ['64', '32:25.2;30:36.3;31:13.5;36:33.1;33:33.8;37:12.9;32:21.5;32:25.1'],
    ['27', '27:58.1;28:46.5;28:55.6;30:26.3;34:42.7;38:06.7;37:01.6;41:43.4'],
    ['105', '29:31.0;31:00.3;31:16.8;33:57.1;33:15.4;37:37.2;36:47.6;35:05.2'],
    ['31', '29:34.6;29:20.9;29:19.7;29:26.2;30:35.6;35:39.4;41:56.8;43:20.1'],
    ['112', '28:38.4;29:23.7;29:57.2;31:01.4;33:39.8;36:55.1;40:18.9;42:40.7'],
    ['28', '31:27.6;30:53.0;32:04.3;35:34.1;37:09.1;38:02.2;37:12.8;37:58.1'],
    ['69', '33:05.1;33:54.1;33:08.6;33:19.1;34:13.5;34:22.7;37:39.0;40:39.6'],
    ['77', '29:44.5;30:35.5;30:06.5;34:19.8;36:03.5;39:15.2;39:36.2;42:07.7'],
    ['45', '29:44.7;30:36.0;30:04.5;34:20.5;36:03.9;39:13.4;39:38.4;42:07.7'],
    ['29', '28:38.2;29:21.1;30:01.5;32:11.2;35:39.7;40:08.9;42:48.4;44:26.8'],
    ['46', '30:28.8;31:07.4;31:17.1;32:13.8;38:15.5;40:31.9;41:19.8;39:28.1'],
    ['30', '31:47.7;33:52.0;34:45.6;35:29.7;36:56.2;37:46.7;39:12.1;37:13.7'],
    ['82', '34:21.7;34:21.4;34:49.4;35:01.8;36:23.9;37:03.2;38:00.5;37:54.5'],
    ['57', '34:19.8;34:08.8;37:13.3;37:05.2;39:28.6;40:05.6;39:33.5;36:25.4'],
    ['74', '37:20.3;38:44.7;40:13.9;42:23.3;43:55.3;43:20.5;44:46.2;46:21.3'],
    ['104', '43:15.8;45:06.6;42:16.0;42:42.6;39:45.9;42:31.9;43:29.7;41:30.3'],
    ['19', '32:52.3;36:50.5;38:45.6;43:28.7;45:28.5;51:52.3;51:27.5;45:26.6'],
    ['118', '36:49.1;39:38.4;42:54.4;45:49.6;44:53.7;45:43.9;43:42.7;48:00.2'],
    ['32', '34:23.0;35:18.2;37:59.3;41:41.4;50:35.1;52:20.6;47:16.1;47:58.5'],
    ['66', '38:36.1;36:10.7;41:44.2;46:46.7;49:00.2;47:35.1;48:12.8;46:00.4'],
    ['65', '33:39.7;36:11.9;38:25.3;43:08.2;52:43.1;50:31.6;56:04.1;1:05:05.8'],
    ['26', '37:07.4;38:39.1;42:54.6;49:14.2;51:50.7;55:28.6;52:08.6;49:07.3'],
    ['67', '43:55.5;46:31.3;48:59.8;52:29.1;53:58.1;52:46.4;52:31.6;52:00.4'],
    ['60', '44:20.6;45:52.2;47:45.0;49:26.3;53:05.4;56:25.9;54:49.1;53:09.7'],
    ['61', '44:20.0;45:50.2;47:47.4;49:24.5;53:06.6;56:25.1;54:49.7;53:10.9'],
    ['52', '43:33.1;45:59.0;50:37.4;53:55.4;54:33.8;55:03.2;53:30.4;51:35.4'],
]
```

Níže jsou příklady výstupu. Pro běžce s číslem 1 může výstup vypadat takto:

```
1
Rozdíl mezi prvním a posledním kolem je 3.48 min.
Rozdíl mezi nejrychlejším a nejpomalejším časem v rámci prvních pěti kol je 0.8 min.
Nejrychleji zaběhl(a) 4. a nejpomaleji 8. kolo.
Průměrná rychlost je 15.85 km/h.
```

Pro běžce s číslem 84 může výstup vypadat takto:

```
84
Rozdíl mezi prvním a posledním kolem je 3.8 min.
Rozdíl mezi nejrychlejším a nejpomalejším časem v rámci prvních pěti kol je 1.66 min.
Nejrychleji zaběhl(a) 1. a nejpomaleji 8. kolo.
Průměrná rychlost je 14.76 km/h.
```

Odpověď na poslední bod může vypadat třeba takto:

```
První kolo zaběhlo nejrychleji 39 (63 %) běžců a běžkyň a poslední nejpomaleji 22 (35 %) běžců a běžkyň.
```
