import os
os.system("cls")
def legtobbszorElofordulo(lista):
    return max(set(lista), key = lista.count)
rendelesek = []
orak = []
f = open("rendelesek.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.replace("\n","")#Finom	1390	08:12	08:22
    darabolas = sor.split("\t")#[0]->Finom [1]->1390 [2]->08:12 [3]->08:22
    pizza = {}
    pizza['nev'] = darabolas[0]
    pizza['ara'] = int(darabolas[1])
    pizza['rendelesido'] = darabolas[2]
    rendelesiIdo = darabolas[2].split(":")
    ora=rendelesiIdo[0]
    orak.append(ora)
    pizza['szallitasido'] = darabolas[3]
    rendelesek.append(pizza)
f.close()
rendelesSzam = len(rendelesek)
print(f"A rendelések száma {rendelesSzam}db")
print(str(legtobbszorElofordulo(orak)))


