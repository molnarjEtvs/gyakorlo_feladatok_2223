import os
os.system("cls")

nev = input("Add meg a pokemon nevét: ")
ero = int(input("Add meg az erő pontszámot: "))

up = (ero/2)*0.43
rp = (ero/3)*0.9

print(f"A pokemon neve: {nev}")
print(f"Erő: {ero} pont")
print(f"Rugás->{rp}, Ütés->{up}")