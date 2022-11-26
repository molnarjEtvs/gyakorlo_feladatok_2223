import os
os.system("cls")

telefonHivasok = []
f = open("hivasok.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.replace("\n","")
    if " " in sor:
        darabolas = sor.split(" ")
        szotar = {}
        szotar['ora1'] = int(darabolas[0])
        szotar['perc1'] = int(darabolas[1])
        szotar['mp1'] = int(darabolas[2])
        szotar['ora2'] = int(darabolas[3])
        szotar['perc2'] = int(darabolas[4])
        szotar['mp2'] = int(darabolas[5])
    else:
        szotar['telefonszam'] = sor
        telefonHivasok.append(szotar)

    
    
f.close()
print(telefonHivasok[1]['telefonszam'])