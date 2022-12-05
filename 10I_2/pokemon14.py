import os
os.system("cls")

def pokemonRogzites():
    nevek = []
    nev = "t"
    while nev != "":
        nev = input("add meg a pokemon nevét: ")
        if nev != "":
            nevek.append(nev)
    return nevek

def kiErtekeles(p):
    bBetusek = []
    cBetusek = []
    maradek = []
    for egyNev in p:
        egyNev2 = egyNev.lower()
        if egyNev2.startswith("b"):
            bBetusek.append(egyNev)
        elif egyNev2.startswith("c"):
            cBetusek.append(egyNev)
        else:
            maradek.append(egyNev)
    db = len(p)
    print(f"Rögzített adatok száma: {db} db")
    separator = ", "
    b = separator.join(bBetusek)
    c = separator.join(cBetusek)
    m = separator.join(maradek)
    print(f"B betűsek: {b}")
    print(f"C betűsek: {c}")
    print(f"maradék: {m}")
    
s = pokemonRogzites()
kiErtekeles(s)