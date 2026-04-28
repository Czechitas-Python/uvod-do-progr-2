# INSTRUKCE PRO GENEROVÁNÍ TEXTU VE STEJNÉM STYLU

## 1. Charakter stylu

- Styl je **přátelský a konverzační**, ale věcný — text mluví se čtenářem přímo, jako zkušený kolega u počítače.
- Každý nový koncept je **nejprve motivován konkrétním životním příkladem** (výlet, bankovní účet, vysvědčení, kosmická mise), teprve poté přichází abstrakce.
- Abstraktní definice se **nikdy nepíší před konkrétním příkladem** — pořadí je vždy: situace → kód → vysvětlení.
- Text je **iterativní**: ukázka nejprve pracuje, pak se rozšiřuje, pak zobecňuje.
- Kód a text jsou **rovnocenné poloviny** — žádná část není jen ozdobou druhé.
- Varování a záludnosti se uvádějí explicitně, tučným textem (`**POZOR!**`) nebo jako pojmenovaná `**Poznámka:**`.
- Klíčové je **propojení s tím, co čtenář již zná** — nový pojem se téměř vždy uvede větou, která odkazuje na dříve naučené.
- Terminologie se zavádí v *kurzívě* s českým i anglickým názvem, nebo alespoň s anglickým výrazem v závorce.
- Text nikdy nepůsobí akademicky ani jako dokumentace — cílem je, aby čtenář **pochopil „proč"**, ne jen „co".
- Délka výukové stránky je typicky **300–600 slov + kód**.

---

## 2. Logická struktura a práce s kontextem

**Propojování nových pojmů s dříve vysvětlenými:**
- Každý nový oddíl začíná větou, která explicitně navazuje: „Už jsme viděli...", „Zatím jsme poznali...", „Vzpomeňme si, že...".
- Nový pojem se zavádí jako přirozené rozšíření existujícího.

**Návaznosti mezi sekcemi:**
- Sekce v rámci lekce na sebe navazují sdílenou datovou strukturou nebo společným příkladem.
- Přechod mezi sekcemi bývá věta, která shrnuje, co čtenář právě získal, a naznačuje, co bude dál potřebovat.

**Budování mentálních modelů:**
- Složité struktury se vizualizují metaforou před kódem.
- Poté metaforu opustíme a ukážeme přesný mechanismus kódem.

**Struktura vysvětlení:**
`motivující situace → intuice / analogie → kód → popis výstupu → rozšíření → varování / poznámka`

**Vysvětlování „proč", ne jen „co":**
- Vždy vysvětlit důvod pravidla nebo chování.
- Komparativní perspektiva (Python vs. JavaScript) se používá ke zdůraznění specifického chování.

**Opakování a připomínání kontextu:**
- Pokud se pojem vrací po delší odmlce, text ho stručně připomene větou, nikoliv celým výkladem.

---

## 3. Pravidla vysvětlování

**Jak zavádět nové pojmy:**
1. Uveď problém nebo potřebu, která pojem volá.
2. Ukaž hypotetický příklad, který by bez pojmu nefungoval.
3. Pojmenuj pojem a uveď ho do vztahu s tím, co čtenář zná.
4. Ukaž minimální funkční kód s pojmem.
5. Rozšiř kód o variantu nebo hraniční případ.

**Kdy a jak používat příklady:**
- Příklady přicházejí **ihned po uvedení konceptu**, nikdy ve větším odstupu.
- Každý příklad má jasný, uzavřený účel — čtenář vidí celý kód, nikoliv fragmenty.
- Příklady jsou ze **skutečného života** (bankovní pohyby, jízdní řády, školní výsledky, sportovní závody, kosmonautika), ne abstraktní (`foo`, `bar`, `x`, `y`).

**Škálování komplexity:**
- Vždy od nejjednoduššího případu (bez podmínek, bez cyklů, bez výjimek).
- Každá nová vrstva složitosti je explicitně pojmenována: „Upravme naši funkci tak, aby...".
- Pokročilejší variace se odkládají do sekcí „Čtení na doma".

---

## 4. Struktura obsahu

### Šablona výukové stránky (lekce)

```
## [Název tématu]                          ← H2, jedno nebo dvě slova

[Úvodní věta propojující s předchozím]    ← 1–2 věty, vždy referuje na dříve naučené

[Motivující příklad situace]               ← 1–4 věty popisující reálný scénář

```py
[minimální ukázkový kód]                  ← 5–15 řádků
```

[Vysvětlení kódu nebo výstupu]            ← 1–3 věty

### [Podtéma / variace]                    ← H3

[Rozšíření nebo nová varianta pojmu]      ← 1–3 věty + kód

[**POZOR!** nebo **Poznámka:**]            ← pouze pokud existuje záludnost

### Užitečné [funkce/metody] na [typ]      ← H3, přehledový seznam

`název()`
: Jednořádkový popis

```py
[příklad volání]
```
```

**Délka:** hlavní výklad 300–600 slov, kódové ukázky 5–20 řádků každá, přehledový seznam funkcí 3–8 položek.

---

## 5. Jazyk a tonalita

**Oslovení:** druhá osoba singuláru (tykání): "Všimni si", "Vyzkoušej si", "stáhni soubor".

**Uvozovky:** používej pouze základní uvozovky `"` - nikdy české „ a ".

**Emotikony:** nepoužívej emotikony ani emoji v žádném textu.

**Pomlčka:** používej pouze `-`, nikdy `—` (em dash).

**Formálnost:** nízká až střední. Hovorové výrazy jsou přípustné.

**Délka vět:** střední (15–30 slov). Technické věty kratší.

**Typické formulace:**
- Zavádění konceptu: „Představme si, že...", „Uvažujme například...", „Začněme s..."
- Odkaz dozadu: „Jako jsme již viděli...", „Zatím jsme poznali...", „Vzpomeňme si..."
- Rozšíření: „Upravme naši funkci tak, aby...", „Podobně můžeme také..."
- Varování: `**POZOR!**`, `**Poznámka:**`
- Pobídka k akci: „Vyzkoušejte si ji.", „Zkusme si...", „Pojďme se podívat..."

**Technické termíny:** první výskyt v *kurzívě*, poté normální text.

---

## 6. Pravidla pro práci s kódem

- Kód je vždy v ohraničeném bloku (` ```py `, ` ```shell `, ` ```json `).
- Každý kód musí být spustitelný a kompletní — žádné `...` ani `# zbytek kódu`.
- Výstup kódu se ukazuje jako komentář nebo jako blok `shell` pod kódem.
- Kód se nepřepisuje do textu — text přidává to, co kód neřekne sám: proč, co je překvapivé.
- Klíčová slova a názvy funkcí se vždy uvádějí v `backtick` inline formátu.
- Inline komentáře v kódu jsou v češtině, stručné.

---

## 7. Pedagogický přístup

**Typy příkladů (v pořadí preferencí):**
1. Scénář ze školního prostředí (vysvědčení, přijímačky, maturita)
2. Scénář z každodenního života (bankovní pohyby, nakupování, cestování)
3. Historické nebo vědecké reálie (Apollo, atleti)
4. Abstraktní, ale pojmenované hodnoty (seznam jmen, seznam knih) — nikdy holé `x`, `y`, `a`, `b`

---

## 8. Omezení a zakázané vzory

- **Nezačínat** sekcí s definicí — vždy nejprve motivace nebo příklad.
- **Nepoužívat** abstraktní proměnné bez sémantického obsahu (`a`, `b`, `x`, `foo`, `bar`).
- **Nepsat** kód, který není kompletní a spustitelný.
- **Nevysvětlovat** pojem bez kódu déle než 3 věty za sebou.
- **Nepoužívat** akademický nebo dokumentační jazyk.
- **Neopakovat** celý výklad dříve vysvětleného pojmu — stačí odkaz nebo stručná věta.
- **Nevkládat** více než jeden úplně nový pojem do jednoho odstavce.
- **Neskrývat** výstupy kódu.

---

## 9. Časové odhady lekce

Každá lekce musí obsahovat tabulku odhadovaných časů na začátku souboru (hned za nadpisem H1). Tabulka má jeden řádek pro každou sekci H2.

Časový odhad se skládá z:
- **Výklad** - čas potřebný k vysvětlení tématu
- **Otázky** - čas vyhrazený na dotazy účastníků
- **Praktická ukázka** - pouze u sekcí s praktickou částí

Tabulka se aktualizuje **pouze na výslovnou žádost uživatele**, ne automaticky při každé změně obsahu.

Breakdown (výklad / otázky / praktická ukázka) slouží pouze jako interní podklad pro odhad - v tabulce se nezobrazuje. Tabulka ukazuje pouze celkový čas na sekci.

Formát tabulky:
```
| Sekce | Čas |
|---|---|
| Název sekce | X min |
| **Celkem** | **X min** |
```
