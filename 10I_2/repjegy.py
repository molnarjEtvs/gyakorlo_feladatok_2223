import os
os.system("cls")

repjegyek = []

f = open("repjegy.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.replace("\n","")
    egyAdatSor = sor.split(";")
    repjegy = {}
    repjegy['nap'] = egyAdatSor[0]
    repjegy['ido'] = egyAdatSor[1]
    repjegy['szek'] = egyAdatSor[2]
    repjegy['repulo'] = egyAdatSor[3]
    repjegy['indulas'] = egyAdatSor[4]
    repjegy['cel'] = egyAdatSor[5]
    repjegyek.append(repjegy)
f.close()

print(repjegyek)