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

print(specialni_akce.__doc__)
help(specialni_akce)