
# Lokální rámec

## 🧠 Co je to lokální rámec?

Lokální rámec (angl. *local scope*) je oblast platnosti proměnných definovaných **uvnitř funkce**.  
Proměnná vytvořená uvnitř funkce je **lokální** a **není viditelná mimo ni**, pokud ji výslovně nevrátíme.

---

## ✅ Základní příklad

```python
jmeno = "Adam"

def vrat_jmeno():
    jmeno = "David"  # Lokální proměnná
    return jmeno

print(vrat_jmeno())     # Výstup: David
print(jmeno)            # Výstup: Adam
```

> Lokální proměnná `jmeno` uvnitř funkce nepřepíše globální proměnnou `jmeno`.

---

## ⚠️ Konflikt proměnných – nechtěné chování

Může se stát, že se proměnná ve funkci **shoduje jménem** s proměnnou mimo funkci.

```python
jmeno = "Marie"

def vrat_jmeno(ucitel, student):
    jmeno = ucitel
    def vrat_studenta():
        jmeno = student
        return jmeno
    return vrat_studenta()

print(vrat_jmeno("Eva", "Anna"))  # Výstup: Anna
```

> Vnořená funkce používá **svůj vlastní lokální rámec**, přestože `jmeno` už existuje ve vnějším rámci.

---

## 🕵️‍♂️ Funkce `locals()` – co je v lokálním rámci?

Pomocí funkce `locals()` můžeme zjistit všechny proměnné v aktuálním **lokálním rámci**:

```python
def test():
    jmeno = "Alena"
    prijmeni = "Nováková"
    print(locals())

test()
```

Výstup:

```python
{'jmeno': 'Alena', 'prijmeni': 'Nováková'}
```

---

## 🔄 Přepsání globální proměnné z funkce

Chceme-li **změnit globální proměnnou** uvnitř funkce, musíme použít **klíčové slovo `global`**:

```python
vek = 40

def zmen_vek():
    global vek
    vek = 50

zmen_vek()
print(vek)  # Výstup: 50
```

---

## 🧩 Shrnutí rozdílů mezi globální a lokální proměnnou

| Vlastnost                  | Lokální proměnná              | Globální proměnná             |
|---------------------------|-------------------------------|-------------------------------|
| Kde se definuje           | Uvnitř funkce                 | Mimo funkci                   |
| Kde je dostupná           | Pouze ve své funkci           | V celém programu              |
| Změna ve funkci           | Nemění globální proměnnou     | Lze měnit pomocí `global`     |

---

## 🧪 Kontrolní otázky

1. Co je to lokální proměnná?
2. Jak zjistím, které proměnné jsou v aktuálním lokálním rámci?
3. Jak mohu změnit globální proměnnou z funkce?
4. Co vypíše následující kód:

```python
jmeno = "Tomáš"

def test():
    jmeno = "Karel"
    return jmeno

print(test())
print(jmeno)
```

**Správné odpovědi:**
1. Proměnná definovaná uvnitř funkce.
2. Pomocí funkce `locals()`.
3. Použitím klíčového slova `global`.
4. Výstup: `Karel`, `Tomáš`.

---

Chceš pokračovat kapitolou **nonlocal proměnné**?

[10_uzavreny_ramec.md](10_uzavreny_ramec.md)