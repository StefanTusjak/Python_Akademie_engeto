# 🧠 Úvod do rámců (scopes) v Pythonu

## 🎯 Cíl lekce
- Pochopit, co je to **rámec platnosti proměnné** (scope).
- Vysvětlit rozdíl mezi **lokální**, **globální** a dalšími rámci.
- Naučit se, kdy a jak Python hledá proměnné.

---

## 📘 Co je rámec (scope)?

„Rámec“ určuje **místo**, kde je proměnná dostupná.

Např. proměnná vytvořená uvnitř funkce **není viditelná mimo ni** – má tzv. **lokální platnost**.

---

## 🧪 Příklad – Lokální proměnná

```python
def vypis_jmeno():
    jmeno = "Anna"
    print(jmeno)

vypis_jmeno()
print(jmeno)  # ❌ NameError: name 'jmeno' is not defined
```

🔍 Proměnná `jmeno` existuje jen **uvnitř funkce**. Jakmile funkce skončí, `jmeno` „zmizí“.

---

## 🧪 Co se stane při kolizi?

```python
jmeno = "Pavel"

def vypis_jmeno():
    jmeno = "Tereza"
    print(jmeno)

vypis_jmeno()   # Tereza
print(jmeno)    # Pavel
```

📌 V tomto případě existují **dvě různé proměnné `jmeno`** – každá má jiný rámec:
- `jmeno` ve funkci → lokální
- `jmeno` mimo funkci → globální

---

## 🔍 Jak Python hledá proměnnou?

Python při hledání proměnné postupuje podle tzv. **LEGB pravidla**:

1. **L**ocal – uvnitř aktuální funkce
2. **E**nclosing – uvnitř obalujících funkcí (vnořené funkce)
3. **G**lobal – globální proměnné v souboru
4. **B**uilt-in – vestavěné názvy (např. `print`, `len`)

---

## 🔄 Přepis globální proměnné uvnitř funkce

Chceme-li **změnit** globální proměnnou uvnitř funkce, musíme použít `global`:

```python
x = 10

def nastav_x():
    global x
    x = 42

nastav_x()
print(x)  # 42
```

---

## 🧪 Pozor: bez `global` jen vytváříš novou lokální proměnnou

```python
x = 10

def zkouska():
    x = 99  # Toto nevytvoří globální změnu!
    print(x)

zkouska()  # 99
print(x)   # 10
```

---

## 🧠 Přehled rámců (scopes)

| Název         | Platnost                       | Přístupný kde?                       |
|---------------|--------------------------------|--------------------------------------|
| Local         | Uvnitř funkce                  | Jen v dané funkci                    |
| Enclosing     | Vnořené funkce                 | Ve vnitřní funkci                    |
| Global        | Na nejvyšší úrovni souboru     | Všude v souboru, kromě přepisování   |
| Built-in      | Vestavěné jméno (např. `len`)  | Všude                                |

---

## ❓Kontrolní otázky

1. Co se stane, když použiješ proměnnou vytvořenou uvnitř funkce mimo ni?
2. Jak můžeš upravit globální proměnnou uvnitř funkce?
3. Co dělá klíčové slovo `global`?
4. Co znamená LEGB?

---

## ✅ Odpovědi

1. Vznikne `NameError`, protože proměnná má lokální platnost.
2. Musíš použít `global název_proměnné`.
3. Říká Pythonu, že má použít existující globální proměnnou, ne vytvořit novou lokální.
4. Zkratka pro pořadí hledání proměnné: Local → Enclosing → Global → Built-in.

---

## 🧠 Shrnutí

- Proměnná uvnitř funkce existuje jen v rámci té funkce (lokální scope).
- Python hledá proměnné podle LEGB pravidla.
- Pokud chceš upravit globální proměnnou, použij `global`.
- Každý rámec má svá pravidla – znalost těchto rozdílů chrání před nečekanými chybami.

---

👉 Pokračujeme dále na **Globální rámec**

[08_globalni_ramec.md](08_globalni_ramec.md)
