def ukazka(*args):
    print(args)

ukazka(1, 2, 3)  # → (1, 2, 3)

def vypis_cisla(*cisla):
    for cislo in cisla:
        print(cislo)

vypis_cisla(1, 2, 3, 4)

def secti(*cisla):
    return sum(cisla)

print(secti(5, 10))               # 15
print(secti(1, 2, 3, 4, 5))       # 15
print(secti())                   # 0