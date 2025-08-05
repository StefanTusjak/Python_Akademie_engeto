
# Souhrn rámců

V této lekci si ukážeme, jak Python postupuje při hledání hodnot proměnných a jak funguje tzv. **souhrn rámců** (*scope resolution*).

---

## 🔍 Příklad základního chování

```python
x = "globalní"

def outer():
    x = "vnější"

    def inner():
        x = "vnitřní"
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
print("global:", x)
```

Tento příklad ilustruje, že Python vždy začne hledat proměnnou **v rámci funkce** a pokud ji nenajde, pokračuje směrem ven.

---

## 🧠 LEGB pravidlo

Python používá tzv. **LEGB** pravidlo pro vyhledávání jmen proměnných:

- **L** – *Local* – Lokální rámec (např. uvnitř aktuálně běžící funkce)
- **E** – *Enclosing* – Uzavřený rámec (např. vnější funkce obsahující vnitřní funkci)
- **G** – *Global* – Globální rámec (modul nebo skript)
- **B** – *Built-in* – Vestavěný rámec (např. `print`, `len`, `str` atd.)

Python tedy hledá proměnnou v tomto pořadí a použije první odpovídající výskyt.

---

## 🧪 Příklad s uzavřeným rámcem

```python
x = "globalní"

def outer():
    x = "vnější"

    def inner():
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
print("global:", x)
```

Výstup:
```
inner: vnější
outer: vnější
global: globalní
```

---

## 🧨 shadowing vs. přístup k proměnným

Někdy může dojít k tzv. **shadowingu**, tj. když proměnná ve vnitřním rámci přepíše proměnnou s týmž jménem z rámce vnějšího.

```python
x = "globalní"

def outer():
    x = "vnější"

    def inner():
        x = "vnitřní"
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
print("global:", x)
```

---

## 📛 Použití `nonlocal`

Chceme-li přistupovat ke **změně** proměnné z uzavřeného rámce (enclosing), použijeme klíčové slovo `nonlocal`:

```python
def outer():
    x = "vnější"

    def inner():
        nonlocal x
        x = "upraveno"
        print("inner:", x)

    inner()
    print("outer:", x)

outer()
```

---

## 🌍 Použití `global`

Pokud chceme upravit proměnnou na **globální úrovni**, použijeme `global`:

```python
x = "globalní"

def change_global():
    global x
    x = "změněno"

change_global()
print(x)
```

---

## 🧾 Shrnutí

| Klíčové slovo | Účel |
|---------------|------|
| `local`       | Proměnná definovaná uvnitř funkce. |
| `enclosing`   | Proměnná ve funkci, která obaluje jinou funkci. |
| `global`      | Proměnná na nejvyšší úrovni (modul, skript). |
| `built-in`    | Vestavěné jméno z Pythonu (`len`, `str`, …). |
| `nonlocal`    | Umožňuje měnit proměnnou v uzavřeném rámci. |
| `global`      | Umožňuje měnit proměnnou v globálním rámci. |

Tímto je ukončen přehled rámců a jejich souhrnu. Python je velmi konzistentní a striktní v tom, jak se chová při vyhledávání jmen.
