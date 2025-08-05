# 🌐 Zabudovaný a globální rámec (built-in & global scope)

## 🎯 Cíl lekce
- Vysvětlit rozdíl mezi **globálním** a **zabudovaným (built-in)** rámcem.
- Naučit se používat a rozlišit různé vrstvy rámců v Pythonu.
- Uvědomit si, jak Python přistupuje k proměnným mimo lokální a vnořené prostředí.

---

## 🧠 Co je zabudovaný (built-in) rámec?

Built-in scope obsahuje všechny **vestavěné funkce a objekty** v Pythonu:
- `len()`, `print()`, `int()`, `str()`, `list()`, `dict()`, `sum()` atd.

Tyto funkce jsou dostupné **kdekoli v kódu** – není třeba je importovat ani definovat. Jsou automaticky načtené při startu Pythonu.

---

## 🧪 Ukázka použití vestavěných funkcí

```python
print(len("Python"))
print(sum([1, 2, 3]))
```

✅ Nemusíme `len` ani `sum` nijak definovat – pochází z **built-in scope**.

---

## 🔍 Co když přepíšeme vestavěné jméno?

```python
sum = 10
print(sum([1, 2, 3]))  # ❌ TypeError: 'int' object is not callable
```

📌 Přepsali jsme `sum`, které bylo dříve funkcí, na proměnnou `int`. Python už pak funkci nepozná!

🧽 Doporučení: **Nikdy nepoužívej názvy jako `list`, `sum`, `dict` atd. pro své proměnné!**

---

## 🌍 Globální rámec

Globální rámec je vše, co se nachází:
- na nejvyšší úrovni Python skriptu (mimo funkce),
- nebo je označeno uvnitř funkce pomocí `global`.

---

## 🧪 Ukázka globální proměnné

```python
jmeno = "Eva"

def pozdrav():
    print(jmeno)

pozdrav()  # Eva
```

Proměnná `jmeno` je dostupná z funkce, protože je v **globálním rámci**.

---

## 🧪 Přepis globální proměnné bez `global`

```python
jmeno = "Eva"

def zmen_jmeno():
    jmeno = "Anna"  # toto vytvoří lokální proměnnou
    print(jmeno)

zmen_jmeno()  # Anna
print(jmeno)  # Eva
```

🛑 V tomto případě `jmeno` **nevytvoří změnu globálně**, protože nemáme `global`.

---

## 🧪 Přepis s použitím `global`

```python
jmeno = "Eva"

def zmen_jmeno():
    global jmeno
    jmeno = "Anna"

zmen_jmeno()
print(jmeno)  # Anna
```

✅ Nyní se skutečně změnila hodnota globální proměnné.

---

## 🧠 Shrnutí rámců

| Typ rámce     | Přístupný kde?          | Typické použití                     |
|---------------|--------------------------|--------------------------------------|
| Built-in      | Kdekoli v kódu           | Vestavěné funkce a typy              |
| Globální      | V celém souboru          | Sdílené konstanty, proměnné, importy |
| Lokální       | Uvnitř funkce            | Dočasné výpočty, funkční proměnné    |

---

## ❓Kontrolní otázky

1. Co obsahuje built-in rámec?
2. Můžeš použít `len()` bez importu? Proč?
3. Co se stane, když přepíšeš `sum = 5`?
4. Jak změnit globální proměnnou uvnitř funkce?

---

## ✅ Odpovědi

1. Obsahuje všechny předdefinované funkce a typy v Pythonu.
2. Ano, protože `len` je dostupné automaticky jako součást vestavěných funkcí.
3. Přepíšeš tím funkci `sum` a znemožníš její použití (nastane chyba při volání).
4. Použiješ klíčové slovo `global` před názvem proměnné.

---

👉 Pokračujeme na: **Lokální rámec**
[09_lokalni_ramec.md](09_lokalni_ramec.md)