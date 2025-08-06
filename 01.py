def scitani(a, b):
    return a * b 

soucet = scitani

print(soucet)

def vypocitej_cenu(cena, mnozstvi):
 return cena / mnozstvi

print(vypocitej_cenu(199.9, 3))  # správně: 66.63
print(vypocitej_cenu(3, 199.9))  # špatně: 0.015


def vypocitej_cenu2(cena, dph):
 return cena + (cena * dph)

print(vypocitej_cenu2(100, 0.21))  # správně: 121.0
print(vypocitej_cenu2(0.21, 100))  # špatně: 21.21