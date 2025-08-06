def pozdrav(jmeno="neznámý"):
    print(f"Ahoj, {jmeno}!")

pozdrav()              # Ahoj, neznámý!
pozdrav("Štefan")      # Ahoj, Štefan!

def registruj(jmeno, role="uživatel", aktivni=True):
    print(f"{jmeno} byl přidán jako {role}. Aktivní: {aktivni}")

registruj("Tomáš")
registruj("Petra", role="admin")
registruj("Lukáš", aktivni=False)