import os
os.system("cls")

def bekeres():
    szavak = []
    while True:
        szo = input("Adj meg egy szót: ")
        if szo != "":
            szavak.append(szo)
        else:
            return szavak

def megallapitas(s):
    db = len(s)
    print(f"Darabszám: {db} db")
    print(f"Első szó: {s[0]}")
    print(f"Az utolsó szó: {s[db-1]}")

g = bekeres()
megallapitas(g)
