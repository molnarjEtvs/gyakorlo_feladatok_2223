import os
os.system("cls")

nev = input("Add meg a pokemon nevét: ")
ero = int(input("Add meg az erejét: "))
uteseiPontszam = (ero/2)*0.43
rugasiPontszam = (ero/3)*0.9

print(f"A pokemon neve: {nev}")
print(f"Erő: {ero}")
print(f"Rugás->{rugasiPontszam} pont, Ütés->{uteseiPontszam} pont")