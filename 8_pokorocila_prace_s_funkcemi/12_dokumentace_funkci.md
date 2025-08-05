
# Dokumentace funkcí v Pythonu

Dokumentace funkcí je klíčová součást dobré praxe v programování. Umožňuje nám popsat, co funkce dělá, jaké má parametry, co vrací a jaké výjimky může vyhazovat. Python pro tyto účely nabízí tzv. **docstring** – řetězec uzavřený v trojitých uvozovkách, který je umístěn na začátku těla funkce.

---

## Základní docstring

```python
def scitaj_cisla(a, b):
    """Sečte dvě čísla a vrátí výsledek."""
    return a + b

print(scitaj_cisla(10, 15))  # 25
```

Tento text není komentář, ale **součást funkce** a je přístupný pomocí vestavěné funkce `help()` nebo pomocí atributu `.__doc__`.

---

## Formátování docstringu

Je vhodné psát docstring s více informacemi, např. co funkce přijímá, co vrací a proč.

```python
def specialni_akce(jmeno, vek, vstupenka):
    """
    Zkontroluje podmínky pro speciální slevu:
    - Pokud je osoba mladší 18 let, má nárok na dětskou slevu.
    - Pokud je starší než 65 let, má nárok na seniorskou slevu.
    - Jinak platí plnou cenu.

    Parametry:
    jmeno (str) - jméno osoby
    vek (int) - věk osoby
    vstupenka (str) - typ vstupenky ("dětská", "dospělá", "seniorská")

    Návratová hodnota:
    str - informace o tom, zda má osoba nárok na slevu.
    """
    if vek < 18:
        return f"{jmeno} má dětskou slevu."
    elif vek >= 65:
        return f"{jmeno} má seniorskou slevu."
    else:
        return f"{jmeno} nemá nárok na slevu."
```

---

## Přístup k dokumentaci

```python
print(specialni_akce.__doc__)
help(specialni_akce)
```

Pomocí `help()` můžeme interaktivně zobrazit obsah dokumentace.

---

## Dokumentace pro anonymní funkce (`lambda`)

Anonymní funkce (`lambda`) nemají jméno, a tudíž nelze přidat tradiční docstring. Pokud je potřeba, definujeme klasickou funkci s dokumentací.

---

## Generování dokumentace

Ve větších projektech se dokumentace vytváří pomocí nástrojů jako:

- **Sphinx** - generuje HTML dokumentaci z docstringů
- **pdoc**, **pydoc**, nebo **doctest** - jednodušší alternativy
- **type hints** - slouží k doplnění informací o datových typech

---

## Shrnutí

- Používej trojité uvozovky `"""` pro dokumentaci funkcí.
- Popiš účel funkce, parametry a návratovou hodnotu.
- Větší projekty by měly mít automatizovanou dokumentaci.

[12_01_generovani_dokumentace.md](12_01_generovani_dokumentace.md)