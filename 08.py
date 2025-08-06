# sum = 10
# print(sum([1, 2, 3]))  # ❌ TypeError: 'int' object is not callable

# jmeno = "Eva"

# def pozdrav():
#     print(jmeno)

# pozdrav()  # Eva

# jmeno = "Eva"

# def zmen_jmeno():
#     jmeno = "Anna"  # toto vytvoří lokální proměnnou
#     print(jmeno)

# zmen_jmeno()  # Anna
# print(jmeno)  # Eva

jmeno = "Eva"

def zmen_jmeno():
    global jmeno
    jmeno = "Anna"
    print(jmeno)

zmen_jmeno()
print(jmeno)  # Anna