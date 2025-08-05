# 🎯 Positional-only parametry

## 🧠 Cíl lekce
- Naučit se používat **pouze poziční parametry** pomocí speciální syntaxe zavedené v Pythonu 3.8.
- Pochopit, **proč a kdy** je vhodné omezit použití klíčových argumentů.
- Umět číst a psát funkce se symbolem `/`.

---

## 📘 Co jsou positional-only parametry?

V běžné Python funkci lze většinu parametrů při volání předávat **buď pozičně, nebo klíčově**.

Například:

```python
def pozdrav(jmeno, zprava):
    print(f"{zprava}, {jmeno}!")

pozdrav("Alena", "Ahoj")              # pozičně
pozdrav(jmeno="Alena", zprava="Hi")  # klíčově
```

Ale co když chceme **omezit možnost předávání parametrů jen pozičně**?

---

## 🔐 Zavádíme `/` – pouze poziční parametry

Od verze **Python 3.8** můžeme do hlavičky funkce vložit znak `/`, který říká:
> „Všechny parametry vlevo od tohoto znaku musí být předány pozičně.“

### 🧪 Ukázka:

```python
def registrace(jmeno, vek, /):
    print(f"{jmeno} má {vek} let.")

registrace("Petr", 28)              # ✅ funguje
registrace(jmeno="Petr", vek=28)   # ❌ chyba!
```

---

## ⚠️ Co se stane při nesprávném použití?

```python
registrace(jmeno="Eva", vek=25)
# TypeError: registrace() got some positional-only arguments passed as keyword arguments: 'jmeno'
```

Python ti jasně řekne, že daný parametr **nesmí být předán jako klíčový**.

---

## 💡 Kdy se to hodí?

- Když nechceme, aby volající kód přepisoval jména parametrů.
- U jednoduchých API nebo vestavěných funkcí (např. `len()`).
- Pro konzistentní rozhraní → funkce přijímá jen data, ne konfiguraci.

---

## 🧪 Reálnější příklad – Výpis souřadnic

```python
def vykresli_bod(x, y, /, barva="červená", velikost=10):
    print(f"Bod: ({x}, {y}), barva: {barva}, velikost: {velikost}")

vykresli_bod(3, 5)                          # ✅ použije výchozí barvu a velikost
vykresli_bod(1, 2, barva="modrá")          # ✅ barvu určím klíčově
vykresli_bod(x=1, y=2)                     # ❌ TypeError – x a y jsou jen pozičně
```

---

## ✅ Shrnutí

| Parametr        | Může být předán klíčově? | Poznámka                                  |
|------------------|---------------------------|--------------------------------------------|
| Před `/`         | ❌ Ne                     | Jen pozičně                               |
| Za `/`           | ✅ Ano                    | Lze pozičně i klíčově                      |

---

## 📌 Syntaxe v praxi

- Použití `/` je **volitelné** – používá se jen tam, kde to dává smysl.
- Pokud `/` nepoužiješ, Python dovolí volat všechny parametry i klíčově.

---

## ❓Kontrolní otázky

1. Co znamená `/` ve funkční hlavičce?
2. Co se stane, když se pozičně-povinný parametr předá jako klíčový?
3. Proč bys chtěl/a použít pouze poziční parametry?
4. Můžeš kombinovat poziční-only s výchozími parametry?

---

## ✅ Odpovědi

1. `/` říká, že všechny parametry nalevo musí být volány **jen pozičně**.
2. Python vyhodí `TypeError`, protože jsi porušil/a pravidla definice.
3. Kvůli ochraně API před zneužitím, vyšší přehlednosti nebo přehledným signaturám.
4. Ano – poziční-only parametry můžou mít i výchozí hodnoty, např. `def f(x=1, /)`.

---

## 🚀 Další lekce:

👉 [05_args.md](05_args.md)
