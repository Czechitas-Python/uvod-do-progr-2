## Čtení na doma: Slicing graficky

Zápis slicingu je následující:

![](assets/Slicing-1.drawio.svg)

Máme seznam `tym`:

```python
tym = ["Kuba", "Terez", "Soustruh", "Jirka", "Míša", "Pavel", "Petra"]
```

Pokud chceme první čtyři prvky, použijeme:

```python
prvni_ctyri = tym[0:4]
```

Níže je obsah proměnné `prvni_ctyri`.

```
['Kuba', 'Terez', 'Soustruh', 'Jirka']
```

Slicing začíná na indexu 0 (první prvek) a končí **před** indexem 4, takže dostaneme prvky s indexy 0, 1, 2 a 3.

![](assets/Slicing-3.drawio.svg)

Pokud chceme prvky od prostředka seznamu:

```python
cast_tymu = tym[2:5]
```

Níže je obsah proměnné `cast_tymu`.

```
['Soustruh', 'Jirka', 'Míša']
```

Slicing začíná na indexu 2 a končí před indexem 5, takže dostaneme prvky s indexy 2, 3 a 4.

![](assets/Slicing-4.drawio.svg)
