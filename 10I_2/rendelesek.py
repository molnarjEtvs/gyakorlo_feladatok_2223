import os
os.system("cls")

rendelesek = []
rendelesi_orak = {}
f = open("rendelesek.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.replace("\n","")
    darabolas = sor.split("\t")
    rendeles = {}
    rendeles['pizza'] = darabolas[0]
    rendeles['ar'] = int(darabolas[1])
    rendeles['leadasi_ido'] = darabolas[2]
    oraPerc = darabolas[2].split(":")
    #innen folytatjuk
    rendeles['kisszalitasi_ido'] = darabolas[3]
    rendelesek.append(rendeles)

f.close()
#rendelések száma:
rendelesSzam = len(rendelesek)
print(f"A rendelések száma: {rendelesSzam} db")
