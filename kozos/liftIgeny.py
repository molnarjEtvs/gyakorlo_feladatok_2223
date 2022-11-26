import os
os.system("cls")

liftHasznalat=[]
f = open("igeny.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.replace("\n","") #9 3 14 3 10 17
    egySorAdat = sor.split(" ")
    szotar = {}
    szotar['ora'] = int(egySorAdat[0])
    szotar['perc'] = int(egySorAdat[1])
    szotar['mp'] = int(egySorAdat[2])
    szotar['csapat_ssz'] = int(egySorAdat[3])
    szotar['indulo_szint'] = int(egySorAdat[4])
    szotar['cel_szint'] = int(egySorAdat[5])
    liftHasznalat.append(szotar)
f.close()

#print(liftHasznalat)
#print(liftHasznalat[2]['mp'])