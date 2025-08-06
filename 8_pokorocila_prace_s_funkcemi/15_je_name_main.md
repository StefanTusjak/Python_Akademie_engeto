
# `__name__ == "__main__"` – Proč a kdy ho používat?

V Pythonu se často setkáš s konstrukcí:

```python
if __name__ == "__main__":
    main()
```

Tato podmínka má specifický účel – určuje, **zda byl soubor spuštěn přímo**, nebo **importován jako modul**.

---

## 🔍 Co je `__name__`?

Každý Python soubor (modul) má vestavěnou proměnnou `__name__`. Její hodnota závisí na tom, **jak byl soubor spuštěn**:

| Způsob použití | Hodnota `__name__` |
|----------------|---------------------|
| Soubor spuštěn přímo (`python soubor.py`) | `"__main__"` |
| Soubor importován jako modul | název modulu (např. `"muj_modul"`) |

---

## ✅ K čemu to je dobré?

Pomáhá ti **oddělit spuštění skriptu od jeho importu**. Umožňuje napsat modul, který:

- může být spuštěn samostatně (např. pro testování)
- ale také importován do jiného skriptu bez toho, aby se při importu rovnou něco spouštělo

---

## 🔧 Příklad

Soubor `vypocet.py`:

```python
def secti(a, b):
    return a + b

def odecti(a, b):
    return a - b

if __name__ == "__main__":
    print("Testuji funkce:")
    print(secti(5, 3))
    print(odecti(5, 3))
```

### ➕ Spuštění jako skript:

```bash
python vypocet.py
```

📌 Výstup:
```
Testuji funkce:
8
2
```

### ➕ Import jako modul:

Soubor `main.py`:

```python
import vypocet

print(vypocet.secti(10, 4))
```

📌 Výstup:
```
14
```

✅ Funkce se použije, ale kód v `if __name__ == "__main__"` se **nespustí**.

---

## 🧪 Praktické použití

- **Modularita**: můžeš soubor testovat samostatně, ale i používat v jiných skriptech.
- **Testování**: můžeš vložit testovací data nebo testovací funkce dovnitř `__main__`, aniž by zasahovaly do produkčního kódu.
- **Vývoj knihoven**: knihovny běžně obsahují vlastní testy pod tímto blokem.

---

## 💡 Shrnutí

Použij `if __name__ == "__main__"` když:

- chceš, aby se část kódu spustila **jen při přímém spuštění souboru**
- chceš, aby se **při importu funkce nespouštěl zbytečný testovací nebo výstupní kód**

Díky tomu můžeš kombinovat modulární a skriptové použití jednoho Python souboru.

---

## ✅ Doporučený vzor

```python
def main():
    # zde hlavní logika
    pass

if __name__ == "__main__":
    main()
```

---

📚 Tímto způsobem budeš psát čistší, přehlednější a znovupoužitelný kód.
