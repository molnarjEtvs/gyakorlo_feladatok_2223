import os
os.system("cls")

def bekeres():
    szavak = []
    szo = "teszt"
    while szo!="":
      szo = input("Adj meg egy szót: ")
      if szo!="":
        szavak.append(szo)  
    return szavak

def megallapitas(x):
    db = len(x)
    print(f"Darabszám: {db} db")
    print(f"Az első szó: {x[0]}")
    print(f"Utolsó szó: {x[db-1]}")

a = bekeres()
megallapitas(a)
