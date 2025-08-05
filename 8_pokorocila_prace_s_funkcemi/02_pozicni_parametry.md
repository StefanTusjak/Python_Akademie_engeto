# 🎯 Poziční a klíčové parametry

## 🧠 Cíl lekce
- Porozumět rozdílu mezi **pozičními** a **klíčovými** parametry.
- Naučit se je kombinovat a správně používat ve vlastních funkcích.
- Vyhnout se běžným chybám při jejich používání.

---

## 📘 Co jsou poziční a klíčové parametry?

Funkce může mít více parametrů. Když ji voláme, můžeme jim předávat hodnoty **podle pořadí (pozičně)** nebo **podle názvu (klíčově)**.

---

## 📌 Poziční parametry

Poziční parametry jsou ty, kterým hodnoty přiřadíme **na základě pořadí**, v jakém je uvádíme.

### 🧪 Příklad:

```python
def objednej_kavu(druh, velikost, mleko):
    print(f"Objednávám {velikost} {druh} kávu s {mleko}.")

objednej_kavu("latte", "velkou", "mandlovým mlékem")
```

🔍 Hodnoty se přiřadí takto:
- `druh = "latte"`
- `velikost = "velkou"`
- `mleko = "mandlovým mlékem"`

✅ Funguje, protože pořadí argumentů odpovídá pořadí parametrů.

---

## ⚠️ Na pořadí záleží!

```python
objednej_kavu("velkou", "latte", "mandlovým mlékem")
# Výstup bude nesmyslný – hodnoty se přiřadí špatně
```

---

## 🏷️ Klíčové (pojmenované) parametry

Místo toho, abychom se spoléhali na pořadí, můžeme při volání **výslovně říct, který argument patří ke kterému parametru**:

```python
objednej_kavu(druh="espresso", velikost="malou", mleko="bez mléka")
```

✅ Výhoda: **nezáleží na pořadí**, protože vše je jasně pojmenováno.

---

## 🧪 Kombinace obou způsobů

Můžeme kombinovat poziční i klíčové argumenty – ale **nejprve musí být všechny poziční**, až potom klíčové.

```python
objednej_kavu("flat white", velikost="střední", mleko="sojovým")
```

❌ Toto by nefungovalo:
```python
objednej_kavu(druh="flat white", "střední", "sojovým")  # SyntaxError
```

---

## 💡 Reálný příklad z praxe

```python
def vytvor_uzivatele(jmeno, vek, aktivni=True):
    print(f"Uživatel: {jmeno}, Věk: {vek}, Aktivní: {aktivni}")

# Pozičně
vytvor_uzivatele("Karel", 30)

# Klíčově
vytvor_uzivatele(jmeno="Petra", vek=25, aktivni=False)

# Kombinace
vytvor_uzivatele("Jana", vek=28, aktivni=True)
```

---

## 🧠 Shrnutí

| Styl        | Vhodný když...                        | Výhoda                              |
|-------------|----------------------------------------|-------------------------------------|
| Poziční     | Máš krátkou funkci, pořadí je jasné    | Rychlé, stručné                     |
| Klíčový     | Chceš čitelnost, vynechat parametry    | Nepotřebuješ znát pořadí           |
| Kombinace   | Chceš stručnost + přehlednost          | Flexibilita                         |

---

## ❓Kontrolní otázky

1. Co je poziční parametr? Kdy se hodí použít?
2. Co je klíčový argument? Jaká je jeho výhoda?
3. Můžu použít klíčové argumenty bez znalosti pořadí parametrů?
4. Můžu kombinovat poziční a klíčové argumenty? Pokud ano, jak?

---

## ✅ Odpovědi

1. **Poziční parametr** je přiřazen podle pořadí – je vhodný pro jednoduché funkce, kde pořadí je jasné.
2. **Klíčový argument** se přiřazuje pomocí názvu – výhodou je čitelnost a nezávislost na pořadí.
3. Ano – pokud použiješ výhradně klíčové argumenty, pořadí nehraje roli.
4. Ano – ale poziční musí být **vždy první**, klíčové až **potom**.

---

## 🚀 Pokračujeme dále:

👉 [03_defaultni_parametry.md](03_defaultni_parametry.md)
