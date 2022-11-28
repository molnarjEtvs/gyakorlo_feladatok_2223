import os
os.system("cls")

repjegyek = []
f=open("repjegy.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.replace("\n","")
    darabolas = sor.split(";")
    repjegy = {}
    repjegy['datum'] = darabolas[0]
    repjegy['ido'] = darabolas[1]
    repjegy['szek'] = darabolas[2]
    repjegy['gepszam'] = darabolas[3]
    repjegy['honnan'] = darabolas[4]
    repjegy['hova'] = darabolas[5]
    repjegyek.append(repjegy)
f.close()
print(repjegyek)