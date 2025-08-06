def objednej_kavu(druh, velikost, mleko):
    print(f"Objednávám {velikost} {druh} kávu s {mleko}.")

objednej_kavu("latte", "velkou", "mandlovým mlékem")

objednej_kavu("velkou", "latte", "mandlovým mlékem")
# Výstup bude nesmyslný – hodnoty se přiřadí špatně

objednej_kavu(druh="espresso", velikost="malou", mleko="bez mléka")
objednej_kavu(mleko="bez mléka", velikost="malou", druh="espresso")

objednej_kavu("flat white", velikost="střední", mleko="sojovým")

# objednej_kavu(druh="flat white", "střední", "sojovým mlékem")  # SyntaxError

def vytvor_uzivatele(jmeno, vek, aktivni=True):
    print(f"Uživatel: {jmeno}, Věk: {vek}, Aktivní: {aktivni}")

# Pozičně
vytvor_uzivatele("Karel", 30)

# Klíčově
vytvor_uzivatele(jmeno="Petra", vek=25, aktivni=False)

# Kombinace
vytvor_uzivatele("Jana", vek=28, aktivni=True)