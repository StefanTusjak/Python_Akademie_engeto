# 🧰 **kwargs – proměnný počet pojmenovaných argumentů

## 🧠 Cíl lekce
- Naučit se psát funkce, které přijímají **libovolný počet klíčových (pojmenovaných) argumentů**.
- Pochopit, jak `**kwargs` funguje a jak jej využít v praxi.
- Umět rozlišit `*args` a `**kwargs` a správně je kombinovat.

---

## 📘 Co je `**kwargs`?

`**kwargs` je zkratka pro **keyword arguments** – tedy pojmenované argumenty.

Pomocí `**` říkáme Pythonu:
> „Chci zachytit libovolný počet argumentů, které jsou ve formátu `klíč=hodnota`. Ulož je do jednoho slovníku.“

---

## 🧪 Příklad – Výpis informací o osobě

```python
def vypis_info(**kwargs):
    for klic, hodnota v kwargs.items():
        print(f"{klic}: {hodnota}")

vypis_info(jmeno="Matěj", prijmeni="Novák", vek=28, email="matej@email.cz")
```

✅ Výstup:
```
jmeno: Matěj
prijmeni: Novák
vek: 28
email: matej@email.cz
```

📌 Python vytvoří **slovník (`dict`)**, ve kterém jsou klíče názvy argumentů a hodnoty jsou jejich obsah.

---

## 💡 Kdy použít `**kwargs`?

- Když **nevíš předem, kolik a jaké parametry** ti uživatel funkce může poslat.
- U funkčních wrapperů (např. dekorátory).
- Při přeposílání dat do jiných funkcí (např. `render_template(**context)` ve Flasku).
- Pro konfigurace, přepínače, logování apod.

---

## 🧪 Kombinace s pevnými parametry

```python
def registruj(jmeno, prijmeni, **dalsi_udaje):
    print(f"{jmeno} {prijmeni}")
    for k, v in dalsi_udaje.items():
        print(f"{k}: {v}")

registruj("Lenka", "Malá", vek=29, aktivni=True, email="lenka@mail.cz")
```

✅ Výstup:
```
Lenka Malá
vek: 29
aktivni: True
email: lenka@mail.cz
```

---

## 🧠 Tipy a poznámky

- Název `kwargs` je konvence – můžeš použít i `**data`, `**params`, atd.
- Vždy musí být **na konci** parametrů.
- Výsledkem je `dict`, který můžeš procházet přes `.items()`, `.keys()` atd.

---

## ⚠️ Pozor na konflikt se jmény

```python
def funkce(jmeno, **kwargs):
    print(jmeno)
    print(kwargs)

funkce("Eva", jmeno="Tereza")
# TypeError: funkce() got multiple values for argument 'jmeno'
```

🛑 Pokud název v `kwargs` koliduje s pevným parametrem, vznikne chyba!

---

## 📌 Shrnutí `*args` vs `**kwargs`

| Zápis       | Co dělá                               | Typ datové struktury |
|-------------|----------------------------------------|-----------------------|
| `*args`     | Zachytí všechny **poziční** argumenty  | `tuple`               |
| `**kwargs`  | Zachytí všechny **pojmenované** argumenty | `dict`             |

---

## ❓Kontrolní otázky

1. Co znamená `**kwargs` a jaký typ dat vrací?
2. Může být `**kwargs` prázdný?
3. Jaký je rozdíl mezi `*args` a `**kwargs`?
4. Co se stane, když `**kwargs` obsahuje klíč, který je již použit jako pevný parametr?

---

## ✅ Odpovědi

1. `**kwargs` je slovník pojmenovaných argumentů – tedy těch, které jsou zadány jako `klíč=hodnota`.
2. Ano – pokud žádný klíčový argument nepředáš, bude to prázdný slovník `{}`.
3. `*args` sbírá poziční argumenty jako `tuple`, `**kwargs` sbírá klíčové argumenty jako `dict`.
4. Python vyhodí chybu `TypeError`, protože dostane stejný parametr dvakrát.

---

## 🚀 Bonus: Kombinace všech možností

```python
def demo_funkce(a, b=2, *args, c=3, **kwargs):
    print(f"a={a}, b={b}, args={args}, c={c}, kwargs={kwargs}")

demo_funkce(1, 10, 20, 30, c=40, d=50, e=60)
```

✅ Výstup:
```
a=1
b=10
args=(20, 30)
c=40
kwargs={'d': 50, 'e': 60}
```

---

## 🧠 Shrnutí vstupů do funkcí

| Typ             | Ukázka                  | Vlastnost                                        |
|------------------|--------------------------|--------------------------------------------------|
| Poziční parametry| `def f(x, y)`            | Parametry bez výchozí hodnoty                   |
| Defaultní parametry | `def f(x=10)`         | Parametry s výchozí hodnotou                    |
| Positional-only  | `def f(x, /)`            | Parametr lze zadat jen pozičně                  |
| `*args`          | `def f(*args)`           | Libovolný počet pozičních argumentů (n-tice)    |
| Klíčové parametry| `def f(*, x)`            | Parametry musí být zadány klíčově               |
| `**kwargs`       | `def f(**kwargs)`        | Libovolný počet klíčových argumentů (slovník)   |

---

## 🚀 Tímto končí sekce o vstupních parametrech 🎉

Další kapitola může být např. o rozsazích proměnných nebo dokumentaci funkcí.
