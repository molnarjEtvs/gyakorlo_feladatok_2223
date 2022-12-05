import os
os.system("cls")

def pokemonRogzites():
    nevek = []
    while True:
        pNev = input("Add meg a pokemon nevét: ")
        if pNev != "":
            nevek.append(pNev)
        else:
            return nevek

def kiErtekeles(szavak):
    db = len(szavak)
    print(f"Rögzített adatok száma: {db} db")
    b = []
    c = []
    m = []
    for egySzo in szavak:
        if egySzo.startswith("b") or egySzo.startswith("B"):
            b.append(egySzo)
        elif egySzo.startswith("c") or egySzo.startswith("C"):
            c.append(egySzo)
        else:
            m.append(egySzo)
    separator = ", "
    b2 = separator.join(b)
    print(f"B betűsek: {b2}")
    c2 = separator.join(c)
    print(f"C betűsek: {c2}")
    m2 = separator.join(m)
    print(f"Maradék: {m2}")

k =pokemonRogzites()
kiErtekeles(k)