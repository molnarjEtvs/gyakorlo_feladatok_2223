import os
os.system("cls")

aminosavak = []
f = open("aminosav.txt","r",encoding="utf-8")
i = 0
kulcs = ["nev","rovid","betujel","c","h","o","n","s"]
for sor in f:
    sor = sor.replace("\n","")
    if i == 0:
        szotar = {}
        szotar[kulcs[i]] = sor
    else:
        szotar[kulcs[i]] = sor
    i+=1
    if i == 8:
        aminosavak.append(szotar)
        i = 0
f.close()
print(aminosavak)
