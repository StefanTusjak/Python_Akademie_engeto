# 🧰 Defaultní parametry

## 🎯 Cíl lekce
- Naučit se používat výchozí (defaultní) hodnoty u parametrů ve funkcích.
- Pochopit, jak funguje chování funkce s/bez předaného argumentu.
- Umět kombinovat defaultní parametry s ostatními typy vstupů.

---

## 📘 Co jsou defaultní parametry?

V Pythonu můžeme některým parametrům přiřadit **výchozí hodnotu**. To znamená, že funkce funguje i bez explicitního předání těchto hodnot.

Pokud argument při volání funkce **nepředáme**, použije se právě ta výchozí hodnota.

---

## 🧪 Ukázka – Pozdrav s výchozím jménem

```python
def pozdrav(jmeno="neznámý"):
    print(f"Ahoj, {jmeno}!")

pozdrav()              # Ahoj, neznámý!
pozdrav("Štefan")      # Ahoj, Štefan!
```

🔍 Pokud `jmeno` nepředáme → použije se `"neznámý"`. Jinak se použije hodnota, kterou zadáme.

---

## 💡 Proč je to užitečné?

- Můžeme **zjednodušit volání funkcí**, když některé hodnoty chceme často opakovat.
- Funkce jsou **flexibilnější** – zvládnou různé situace bez přetížení.
- Pomáhá při **testování a ladění**, když nepotřebujeme složité vstupy.

---

## 🧪 Složitější příklad – Registrace uživatele

```python
def registruj(jmeno, role="uživatel", aktivni=True):
    print(f"{jmeno} byl přidán jako {role}. Aktivní: {aktivni}")

registruj("Tomáš")
registruj("Petra", role="admin")
registruj("Lukáš", aktivni=False)
```

✅ Výstup:
```
Tomáš byl přidán jako uživatel. Aktivní: True
Petra byl přidán jako admin. Aktivní: True
Lukáš byl přidán jako uživatel. Aktivní: False
```

---

## ⚠️ Pozor na pořadí parametrů!

Defaultní parametry **musí být vpravo** – až za těmi, které výchozí hodnotu nemají.

❌ Toto nebude fungovat:

```python
def chyba(jmeno="Pepa", vek):
    pass  # SyntaxError
```

✅ Správně:

```python
def spravne(jmeno, vek=30):
    pass
```

---

## 🧠 Tipy pro použití

- Funkce může mít více defaultních parametrů – ale vždy až **na konci**.
- Můžeš je přepsat pozičně nebo klíčově:
  ```python
  registruj("Eva", "moderátor")
  registruj("Eva", aktivni=False)
  ```
- Pokud některý parametr často měníš – zvaž, jestli si **zaslouží výchozí hodnotu**.

---

## ✅ Shrnutí

| Typ chování                  | Výsledek                                      |
|-----------------------------|-----------------------------------------------|
| Parametr bez argumentu      | Použije se výchozí hodnota                    |
| Parametr s argumentem       | Nahradí výchozí hodnotu                       |
| Kombinace s pozičními       | Možná – musí se dodržet pořadí                |
| Kombinace s klíčovými       | Možná – lze přepsat konkrétní výchozí hodnotu |

---

## ❓Kontrolní otázky

1. Co je defaultní parametr?
2. Kdy se defaultní hodnota použije?
3. Můžu mít defaultní parametr před běžným parametrem?
4. Jak přepíšu výchozí hodnotu klíčově?

---

## 🧠 Odpovědi

1. Parametr s výchozí hodnotou uvedenou při definici funkce.
2. Když při volání funkce není argument explicitně uveden.
3. Ne – defaultní parametry musí být až za běžnými.
4. Použiju klíčový argument např. `funkce(jmeno="Eliška")`.

---

## 🚀 Pokračujeme dál:

👉 [04_positional_only_parametry.md](04_positional_only_parametry.md)
