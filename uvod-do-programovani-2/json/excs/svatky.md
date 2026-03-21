---
title: Svátky
demand: 3
---

Na adrese `https://svatkyapi.cz/api/day` najdete API, které vám odpoví, kdo má dneska svátek.

1. Využijte toto API k tomu, abyste napsali program, který po spuštění vypíše na obrazovku kdo má dneska svátek.
1. Pokud použijete adresu `https://svatkyapi.cz/api/day/YYYY-MM-DD`, kde místo YYYY-MM-DD doplníte konkrétní datum, dostanete jméno, které má svátek v zadaný den. Formát YYYY-MM-DD znamená že 6. ledna bude zapsáno jako 2026-01-06, 12. září jako 2026-09-12 apod. Napište program, který dostane na příkazové řádce číslo dne a číslo měsíce a vypíše na výstup kdo má v daný den svátek. Použijte váš program abyste zjistili, kdo má svátek 29. února. Rok můžeš použít jakýkoli (např. 2026), pro svátek není důležitý, ale aplikace ho používá pro některé další hodnoty, např. den v týdnu.

:::solution
```py
import requests

# 1. Kdo má dneska svátek
response = requests.get("https://svatkyapi.cz/api/day")
data = response.json()
print(data["name"])

# 2. Svátek v zadaný den
den = int(input("Zadejte den: "))
mesic = int(input("Zadejte měsíc: "))
datum = f"2026-{mesic}-{den}"
response = requests.get(f"https://svatkyapi.cz/api/day/{datum}")
data = response.json()
print(data["name"])
```
:::
