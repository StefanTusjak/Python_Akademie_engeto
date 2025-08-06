
# 📘 Generování dokumentace v Pythonu

## 🧰 Přehled nástrojů

Python nabízí několik nástrojů pro generování dokumentace přímo z dokumentačních řetězců (docstringů):

- **Sphinx** – robustní nástroj, vhodný pro rozsáhlejší projekty, umožňuje výstup do HTML, PDF, atd.
- **pdoc** – jednoduchý nástroj pro generování HTML dokumentace z komentářů v kódu.
- **pydoc** – základní nástroj dostupný v Pythonu bez nutnosti instalace.
- **doctest** – umožňuje spouštět testy uvedené přímo v docstringu.

---

## ⚙️ Instalace nástrojů

```bash
pip install sphinx
pip install pdoc3
```

> `pydoc` a `doctest` jsou součástí Pythonu – není nutná instalace.

---

## 🛠️ Použití nástrojů

### ✅ Sphinx

1. Spuštění průvodce:
```bash
sphinx-quickstart
```

2. Vytvoří se základní adresářová struktura včetně souboru `conf.py` a `index.rst`.

3. Uprav `conf.py`, aby obsahoval cestu k tvému modulu:
```python
import os
import sys
sys.path.insert(0, os.path.abspath('../tvůj_modul'))
```

4. Vytvoř reST soubor např. `modules.rst` a přidej autodoc:
```rst
.. automodule:: tvůj_modul
   :members:
```

5. Generování HTML dokumentace:
```bash
make html
```

---

### ✅ pdoc

Generování HTML dokumentace:
```bash
pdoc --html tvůj_soubor.py --output-dir docs
```

---

### ✅ pydoc

Zobrazení dokumentace v terminálu:
```bash
pydoc tvůj_soubor
```

Export do HTML souboru:
```bash
pydoc -w tvůj_soubor
```

---

### ✅ doctest

Ukázka funkce s doctest dokumentací:

```python
def secti(a, b):
    """
    Sečte dvě čísla.

    >>> secti(2, 3)
    5
    """
    return a + b
```

Spuštění testů v docstringu:
```bash
python -m doctest tvůj_soubor.py
```

---

## ✅ Shrnutí

| Nástroj   | Účel                           | Výhody                          | Použití                    |
|-----------|--------------------------------|----------------------------------|-----------------------------|
| Sphinx    | HTML/PDF dokumentace z projektu | Ideální pro větší projekty       | `sphinx-quickstart`, `make` |
| pdoc      | HTML z docstringů              | Jednoduché a přehledné           | `pdoc --html`              |
| pydoc     | Rychlá dokumentace z CLI       | Bez nutnosti instalace           | `pydoc`, `pydoc -w`        |
| doctest   | Testy v docstringu             | Kombinuje testy a dokumentaci    | `python -m doctest`        |

[13_napovidani_typu.md](13_napovidani_typu.md)