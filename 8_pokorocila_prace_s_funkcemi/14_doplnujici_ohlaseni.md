
# Doplňující ohlašování výjimek v Pythonu

Při psaní složitějších programů v Pythonu může být potřeba reagovat na různé chyby pomocí **výjimek** (exceptions). Existují však situace, kdy potřebujeme výjimky nejen zachytit, ale také je **dále předat** nebo **upravit a znovu vyvolat** – tomu říkáme **doplňující ohlašování výjimek**.

## Ohlášení originální výjimky

Použitím `raise` bez argumentu ve vnitřním `except` bloku předáme výjimku dále:

```python
def vypocet():
    try:
        1 / 0
    except ZeroDivisionError:
        print("Nulou dělit nelze!")
        raise  # znovuvyvolání původní výjimky

vypocet()
```

## Zachycení a přidání nové informace

Pokud chceme přidat kontext k původní výjimce (například jméno proměnné), můžeme využít `raise ... from ...`, čímž vznikne tzv. **řetězení výjimek**:

```python
def vypocet(denominator):
    try:
        return 10 / denominator
    except ZeroDivisionError as e:
        raise ValueError(f"Chyba při dělení číslem: {denominator}") from e

vypocet(0)
```

## Příklad s vlastním typem výjimky

Pokud vytváříme vlastní výjimky, můžeme je kombinovat s původními pomocí `raise ... from ...`:

```python
class MojeChyba(Exception):
    pass

try:
    raise ValueError("Původní chyba")
except ValueError as e:
    raise MojeChyba("Zachycena a transformována") from e
```

## Příklad s `traceback` – sledování původu výjimky

Pomocí modulu `traceback` lze analyzovat detaily o výjimce, např. včetně místa vzniku:

```python
import traceback

try:
    1 / 0
except Exception as e:
    print("Výjimka zachycena:")
    traceback.print_exc()
```

## Pokročilé použití – funkce s více výjimkami

Příklad funkce, která může vyvolat různé výjimky podle vstupu:

```python
import random

def nahodny_vypocet(x):
    if x < 0:
        raise ValueError("Záporné číslo!")
    if random.choice([True, False]):
        raise ZeroDivisionError("Náhodné dělení nulou")
    return 10 / (x + 1)

try:
    vysledek = nahodny_vypocet(-1)
except Exception as e:
    print("Chyba:", e)
```

## Shrnutí

Doplňující ohlašování výjimek je užitečná technika, když chceme:
- přidat kontext původní výjimce,
- transformovat výjimku na jiný typ (např. z `ZeroDivisionError` na `ValueError`),
- sledovat původ chyby pomocí tracebacku,
- nebo výjimku pouze zachytit, zalogovat a opětovně vyvolat.

Je to silný nástroj pro robustní a dobře srozumitelný kód.

