import os
import collections
os.system("cls")

def legtobb(lista):
    c = collections.Counter(lista)
    print(c)

rendelesek = []
orak = []
fajl=open("rendelesek.txt","r",encoding="utf-8")
for row in fajl:
    row = row.replace("\n","")
    darabolas = row.split("\t")
    pizza = {}
    pizza['nev'] = darabolas[0]
    pizza['ar'] = int(darabolas[1])
    pizza['rendeles'] = darabolas[2]
    oraperc = darabolas[2].split(":")
    orak.append(oraperc[0])
    pizza['kiszallitas'] = darabolas[3]
    rendelesek.append(pizza)
fajl.close()
db = len(rendelesek)
print(f"A rendelések száma: {db} db")
legtobb(orak)

