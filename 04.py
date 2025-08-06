def pozdrav(jmeno, zprava):
    print(f"{zprava}, {jmeno}!")

pozdrav("Alena", "Ahoj")              # pozičně
pozdrav(jmeno="Alena", zprava="Hi")  # klíčově

def registrace(jmeno, vek, /):
    print(f"{jmeno} má {vek} let.")

registrace("Petr", 28)              # ✅ funguje
# registrace(jmeno="Petr", vek=28)   # ❌ chyba!

def vykresli_bod(x, y, /, barva="červená", velikost=10):
    print(f"Bod: ({x}, {y}), barva: {barva}, velikost: {velikost}")

vykresli_bod(3, 5)                          # ✅ použije výchozí barvu a velikost
vykresli_bod(1, 2, barva="modrá")          # ✅ barvu určím klíčově
vykresli_bod(x=1, y=2)                     # ❌ TypeError – x a y jsou jen pozičně