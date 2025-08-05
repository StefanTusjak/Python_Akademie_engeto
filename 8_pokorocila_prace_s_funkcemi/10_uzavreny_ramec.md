
# Uzavřený rámec (Enclosing scope)

Uzavřený rámec vzniká v situaci, kdy funkce je **definovaná uvnitř jiné funkce**.

---

## 📘 Příklad 1 – Funkce v sobě

```python
def vnejsi_funkce():
    x = "vnější hodnota"

    def vnitrni_funkce():
        print("Toto je uvnitř funkce:", x)

    vnitrni_funkce()

vnejsi_funkce()
```

### 🔍 Vysvětlení:
- Proměnná `x` je definována ve funkci `vnejsi_funkce`, ale `vnitrni_funkce` k ní **má přístup**, protože je uvnitř stejného rámce.
- `x` je v uzavřeném (enclosing) rámci.

---

## 📘 Příklad 2 – Přiřazení hodnoty

```python
def vnejsi_funkce():
    x = 5

    def vnitrni_funkce():
        x = 10
        print("Vnitřní x:", x)

    vnitrni_funkce()
    print("Vnější x:", x)

vnejsi_funkce()
```

### 🔍 Vysvětlení:
- Vnitřní funkce má vlastní proměnnou `x`, která přepisuje tu vnější jen **ve svém rámci**.
- Vnější `x` zůstává nezměněno.

---

## 🧠 Uzavřený rámec (Enclosing Scope)

Uzavřený rámec označuje prostředí **nad lokální funkcí**, ale **pod globálním rámcem**.

Tento koncept je důležitý v souvislosti s **uzavíráním proměnných (closures)** nebo s použitím klíčového slova `nonlocal`.

---

## 📘 Příklad 3 – Funkce vracející funkci

```python
def sekvencni_funkce(krok):
    def pridat(x):
        return x + krok
    return pridat

plus_petro = sekvencni_funkce(5)
print(plus_petro(10))  # Výsledek: 15
```

### 🔍 Vysvětlení:
- Funkce `pridat` si pamatuje hodnotu `krok`, která byla dostupná ve vnější funkci – to je **uzavřený rámec**.
- Tato vnější hodnota zůstává zachována, i když `sekvencni_funkce` již dávno skončila.

---

## 🧠 Shrnutí:

- Uzavřený rámec (enclosing scope) vzniká, když je jedna funkce **uvnitř jiné funkce**.
- Vnitřní funkce má přístup k proměnným své vnější funkce (pokud je nepřepíše).
- Tento princip se často používá v kombinaci s `nonlocal`, closures nebo funkcemi vyššího řádu.

---

## 🧪 Bonus – Kdy se nepoužije enclosing?

Pokud vnitřní funkce deklaruje proměnnou se stejným názvem, jako má uzavřený rámec, použije se její **lokální** hodnota:

```python
def a():
    x = "venek"
    def b():
        x = "vnitrek"
        print(x)
    b()
    print(x)

a()
```

🟰 Výstup:
```
vnitrek
venek
```
---

**Pokračujeme na: `nonlocal` a práce s uzavřenými hodnotami.**

[11_souhrn_ramcu.md](11_souhrn_ramcu.md)