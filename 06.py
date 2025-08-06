def vypis_info(**kwargs):
    for klic, hodnota in kwargs.items():
        print(f"{klic}: {hodnota}")

vypis_info(jmeno="Matěj", prijmeni="Novák", vek=28, email="matej@email.cz")

def demo_funkce(a, b=2, *args, c=3, **kwargs):
    print(f"a={a}, b={b}, args={args}, c={c}, kwargs={kwargs}")

demo_funkce(1, 10, 20, 30, c=40, d=50, e=60)