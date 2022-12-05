import os
os.system("cls")

def pokemonRogzites():
    nevek = []
    while True:
        nev = input("add meg a pokémon nevét: ")
        if nev != "":
            nevek.append(nev)
        else:
            return nevek

def kiErtekeles(nevek):
    db = len(nevek)
    print(f"Rögzített adatok száma: {db} db")
    bsek = []
    csek = []
    marad = []
    for nev in nevek:
        if nev.startswith("b") or nev.startswith("B"):
            bsek.append(nev)
        elif nev.startswith("c") or nev.startswith("C"):
            csek.append(nev)
        else:
            marad.append(nev)

    separator = ", "
    bStr = separator.join(bsek)
    cStr = separator.join(csek)
    mStr = separator.join(marad)
    print(f"B betűsek: {bStr}")
    print(f"C betűsek: {cStr}")
    print(f"Maradék: {mStr}")

v = pokemonRogzites()
kiErtekeles(v)