# ✨ *args – proměnný počet pozičních argumentů

## 🧠 Cíl lekce
- Naučit se psát funkce, které zvládnou přijmout **libovolný počet pozičních argumentů**.
- Pochopit, jak `*args` funguje a kdy se hodí použít.
- Vědět, jak se `*args` chová jako n-tice (tuple).

---

## 📘 Co je `*args`?
### 🧾 Co znamená `args`?

`args` je zkratka pro **arguments** – tedy „argumenty“.

Používá se jako konvenční název pro proměnnou, která zachytí **libovolný počet pozičních argumentů**.

- `*` znamená, že funkce může přijmout více hodnot.
- `args` je jen název proměnné – můžeš ji pojmenovat jinak (např. `*cisla`, `*hodnoty`), ale `args` je běžný standard.

```python
def ukazka(*args):
    print(args)

ukazka(1, 2, 3)  # → (1, 2, 3)
```



Někdy nevíš, kolik argumentů bude funkce potřebovat. Např. funkce, která sčítá libovolný počet čísel, nebo loguje různé zprávy.

Místo pevně daného počtu parametrů můžeš použít **hvězdičku před názvem proměnné**:

```python
def vypis_cisla(*cisla):
    for cislo in cisla:
        print(cislo)

vypis_cisla(1, 2, 3, 4)
```

📌 V tomto příkladu se všechny předané hodnoty uloží do **n-tice (`tuple`) s názvem `cisla`**.

---

## 🧪 Jak `*args` funguje?

```python
def secti(*cisla):
    return sum(cisla)

print(secti(5, 10))               # 15
print(secti(1, 2, 3, 4, 5))       # 15
print(secti())                   # 0
```

🔍 Funkce `secti` může přijmout **žádný, jeden, nebo libovolný počet čísel** – všechna se uloží do proměnné `cisla`.

---

## ⚠️ Pozor na chyby

Pokud bys definoval funkci bez `*args`, Python očekává přesný počet parametrů:

```python
def secti_dve(a, b):
    return a + b

secti_dve(1, 2, 3)
# TypeError: secti_dve() takes 2 positional arguments but 3 were given
```

✅ S `*args` je to bezpečné:

```python
def vypis(*zpravy):
    for z in zpravy:
        print(f"Log: {z}")
```

---

## 💡 Použití v praxi

- Když chceš přijmout **flexibilní počet hodnot**.
- Když vytváříš **rozšířitelné API** – např. logger, zpracování dat apod.
- Pro předávání argumentů do jiné funkce (`*rozbalení argumentů` – pokročilejší technika).

---

## 📌 Tip: `*args` je jen konvence

Název `args` není povinný – důležitá je hvězdička `*`.

```python
def vypis(*polozky):
    print(polozky)  # typ: tuple
```

---

## 🧠 Shrnutí

| Vlastnost                | Popis                                                  |
|--------------------------|---------------------------------------------------------|
| `*args`                  | Zachytí **libovolný počet pozičních argumentů**        |
| Typ                      | `tuple` – můžeš iterovat, používat `len()`, atd.       |
| Počet hodnot             | Může být nulový, jeden nebo více                       |
| Umístění v parametrech   | Typicky na konci funkce (ne nutně poslední – viz `**kwargs`) |

---

## ❓Kontrolní otázky

1. Co znamená `*args` ve funkci?
2. Jaký typ dat Python vytvoří z `*args`?
3. Může `*args` být prázdné?
4. K čemu se hodí `*args` v praxi?

---

## ✅ Odpovědi

1. Označuje, že funkce přijímá libovolný počet pozičních argumentů.
2. Python vytvoří `tuple` – n-tici.
3. Ano – není nutné, aby byla předána jakákoli hodnota.
4. Pro funkce, u kterých neznáš dopředu počet hodnot – např. sčítání, logování, nebo práce s dynamickými vstupy.

---

## 🚀 Další kapitola:

👉 [06_kwargs.md](06_kwargs.md)
