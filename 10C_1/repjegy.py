import os
os.system("cls")

repjegyek = []
f = open("repjegy.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.replace("\n","")
    darabolt = sor.split(";")
    repjegy = {}
    repjegy['nap'] = darabolt[0]
    repjegy['ido'] = darabolt[1]
    repjegy['szek'] = darabolt[2]
    repjegy['gepszam'] = darabolt[3]
    repjegy['honnan'] = darabolt[4]
    repjegy['hova'] = darabolt[5]
    repjegyek.append(repjegy)
f.close()

print(repjegyek)