# 🧠 Úvod ke vstupům ve funkcích

## 🎯 Cíl lekce
- Pochopit rozdíl mezi **parametrem** a **argumentem**.
- Umět definovat funkce s parametry a volat je s argumenty.
- Vědět, proč záleží na pořadí a typu vstupů.

---

## 🔍 Co jsou **vstupy do funkcí**?

Když chceme, aby funkce pracovala s nějakými daty, předáváme jí tyto **vstupy**. Může jít o čísla, texty, seznamy nebo jiná data.

Funkce vstupy **očekává** – definujeme je jako **parametry**. Při volání jí předáváme konkrétní **argumenty**.

---

## 📚 Parametry vs. Argumenty

| Pojem       | Kde ho najdeš       | Co to je                                |
|-------------|----------------------|-----------------------------------------|
| Parametr    | V definici funkce    | Místo, kde funkce říká „očekávám vstup“ |
| Argument    | Při volání funkce    | Skutečná hodnota, kterou funkci dáš     |

---

## 🧪 Ukázka – Funkce na výpočet ceny

```python
def vypocitej_cenu(kus, cena_za_kus):
    """Vypočítá celkovou cenu."""
    return kus * cena_za_kus

# Volání funkce
cena = vypocitej_cenu(3, 199.9)
print(f"Celkem zaplatíte: {cena} Kč")
```

### 🔍 Co se děje:
- `kus`, `cena_za_kus` → **parametry** ve funkci
- `3`, `199.9` → **argumenty** předané při volání

---

## ⚠️ Časté chyby začátečníků

1. ❌ Předání špatného počtu argumentů:
   ```python
   vypocitej_cenu(5)  # TypeError: chybí 1 argument!
   ```

2. ❌ Předání argumentů v jiném pořadí (poziční zápis je citlivý!):
   Například pokud funkce dělí:
   
   ```python
   def vypocitej_cenu(cena, mnozstvi):
    return cena / mnozstvi

   vypocitej_cenu(199.9, 3)  # správně: 66.63
   vypocitej_cenu(3, 199.9)  # špatně: 0.015

   ```
   Nebo pokud závisí na konkrétní logice:

   ```python
   def vypocitej_cenu(cena, dph):
    return cena + (cena * dph)

   vypocitej_cenu(100, 0.21)  # správně: 121.0
   vypocitej_cenu(0.21, 100)  # špatně: 21.21

   ```

3. ❌ Zapomenutí volání funkce:
   ```python
   vypocitej_cenu  # Odkazuje na funkci, ale nic nespustí
   ```
   výstup:
   
   ```python
   <function scitani at 0x000001BAE6FA1440>
   ```

   Reprezentace funkce jako objektu v paměti
   - scitani je funkce, která v Pythonu existuje jako objekt.
   - 0x000001BAE6FA1440 je paměťová adresa, kde je tento objekt uložen.
---

## 🎓 Proč jsou parametry a argumenty důležité?

- Umožňují psát funkce, které se dají **znovu použít s různými hodnotami**.
- Pomáhají **oddělit logiku od dat** – funkce je univerzální.
- Díky nim může být kód přehlednější a udržitelnější.

---

## 🧩 Mini úkol – Vytvoř funkci

Vytvoř funkci `pozdrav_osobu(jmeno, vek)`, která vypíše:
> Ahoj, Jitko! Je ti 32 let? To je skvělé!

```python
def pozdrav_osobu(jmeno, vek):
    print(f"Ahoj, {jmeno}! Je ti {vek} let? To je skvělé!")

pozdrav_osobu("Jitka", 32)
```

📝 Vyzkoušej funkci i s jinými hodnotami!

---

## ❓Kontrolní otázky (k zamyšlení nebo testu)

1. **V jaké části funkce se používají parametry?**  
   Parametry se uvádějí v závorce při definici funkce (`def`), kde určujeme, jaké vstupy funkce očekává.

2. **Co je to argument a kdy ho píšeme?**  
   Argument je konkrétní hodnota, kterou předáváme funkci při jejím volání. Píšeme ji do závorek při volání funkce.

3. **Co se stane, když předáme špatný počet argumentů?**  
   Python vyhodí chybu `TypeError`, protože počet argumentů neodpovídá počtu parametrů.

4. **Jak zajistíš, že pořadí argumentů nebude vadit?**  
   Místo pozičních argumentů použijeme **klíčové argumenty**, kde ke každé hodnotě uvedeme jméno parametru. Tomu se budeme věnovat později.

---

## 🔧 Extra: Funkce bez parametrů

Někdy funkce nepotřebuje žádné vstupy:

```python
def zobraz_uvod():
    print("Vítejte v našem programu!")

zobraz_uvod()
```

🟢 Tento způsob se používá u jednoduchých zpráv, nastavení, výpisů apod.

---

## 🧠 Shrnutí

- **Parametr** je název proměnné v definici funkce.
- **Argument** je hodnota, kterou do funkce předáváme.
- Funkce s parametry jsou univerzálnější a lépe se testují.
- Na pořadí argumentů záleží (zatím).

---

## 🚀 Pokračujeme do další kapitoly:

👉 [02_pozicni_parametry.md](02_pozicni_parametry.md)
