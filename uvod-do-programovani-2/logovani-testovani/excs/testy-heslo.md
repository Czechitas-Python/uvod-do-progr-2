---
title: Validátor hesla
demand: 3
---

V lekci jsme testovali metody tříd, ale pomocí `TestCase` můžeme testovat i samostatné funkce. Máme funkci `validate_password(password)`, která ověřuje sílu hesla. Funkce vrátí `True`, pokud heslo splňuje všechna pravidla, a `False`, pokud ne.

Pravidla pro platné heslo:

- Heslo má alespoň 8 znaků.
- Heslo obsahuje alespoň jedno velké písmeno.
- Heslo obsahuje alespoň jedno malé písmeno.
- Heslo obsahuje alespoň jednu číslici.

```py
def validate_password(password):
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    return True
```

Napiš unit testy pro tuto funkci. Vytvoř testovací třídu `TestValidatePassword` s následujícími testy:

- `test_valid_password` - ověří, že heslo `"Heslo123"` je platné.
- `test_too_short` - ověří, že heslo `"Abc1"` je neplatné (příliš krátké).
- `test_missing_uppercase` - ověří, že heslo `"heslo123"` je neplatné (chybí velké písmeno).
- `test_missing_lowercase` - ověří, že heslo `"HESLO123"` je neplatné (chybí malé písmeno).
- `test_missing_digit` - ověří, že heslo `"HesloAbc"` je neplatné (chybí číslice).

Testování by však mělo odhalit, že v implementaci funkce je chyba. Oprav chybu ve funkci a spusť testy znovu, aby ses ujistil, že jsou všechny v pořádku.

:::solution
```py
from unittest import TestCase
from password_validator import validate_password


class TestValidatePassword(TestCase):
    def test_valid_password(self):
        self.assertEqual(validate_password("Heslo123"), True)

    def test_too_short(self):
        self.assertEqual(validate_password("Abc1"), False)

    def test_missing_uppercase(self):
        self.assertEqual(validate_password("heslo123"), False)

    def test_missing_lowercase(self):
        self.assertEqual(validate_password("HESLO123"), False)

    def test_missing_digit(self):
        self.assertEqual(validate_password("HesloAbc"), False)
```

Test `test_missing_digit` odhalí chybu - funkce neověřuje přítomnost číslice. Opravená funkce:

```py
def validate_password(password):
    if len(password) < 8:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    return True
```
:::
