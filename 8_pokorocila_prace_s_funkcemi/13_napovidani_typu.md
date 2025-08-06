
# Napovídání datových typů (Type Hinting) v Pythonu

Napovídání datových typů (Type Hinting) slouží k tomu, abychom mohli specifikovat očekávané datové typy parametrů a návratových hodnot funkcí.
Tato funkcionalita je dostupná od verze **Python 3.5** a výrazně zlepšuje čitelnost a srozumitelnost kódu.

---

## Základní syntaxe

```python
def vynasob_hodnoty(x: int, y: int) -> int:
    return x * y
```

- `x: int` a `y: int` – definujeme, že oba parametry by měly být typu `int`.
- `-> int` – funkce vrací hodnotu typu `int`.

---

## Proč používat napovídání typů?

1. ✅ **Zvyšuje čitelnost kódu** – ostatním (i vám) bude hned jasné, jaké typy se očekávají.
2. ✅ **Pomáhá nástrojům jako mypy** odhalovat chyby ještě před spuštěním kódu.
3. ✅ **Zlepšuje automatické doplňování (intellisense)** v editorech jako VS Code.
4. ❌ **Není to validace typů!** Python typy stále nekontroluje při běhu – pouze doporučení.

---

## Typování více typů pomocí Union

Pokud parametr nebo návratová hodnota může být více typů:

```python
from typing import Union

def ziskej_hodnotu(x: Union[int, float]) -> float:
    return float(x)
```

---

## Typování kolekcí (list, tuple, dict...)

```python
from typing import List, Dict, Tuple

def secti_vsechny(cisla: List[int]) -> int:
    return sum(cisla)

def vrat_jmeno_a_vek() -> Tuple[str, int]:
    return ("Anna", 30)

def vytvor_index() -> Dict[str, int]:
    return {"a": 1, "b": 2}
```

---

## Typování proměnných

```python
vek: int = 25
jmeno: str = "Adam"
aktivni: bool = True
```

---

## Použití `type()` pro kontrolu typu za běhu

```python
print(type(jmeno))  # <class 'str'>
```

---

## Kontrola typů pomocí mypy

Pomocí nástroje `mypy` můžeme zkontrolovat celý náš soubor:

```bash
mypy muj_soubor.py
```

Nainstalujeme pomocí:

```bash
pip install mypy
```

---

## Shrnutí

Napovídání typů je skvělý nástroj, který **nezpomaluje běh programu**, ale přináší výhody v podobě lepší čitelnosti, kontroly a ladění.

