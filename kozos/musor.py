import os
os.system("cls")

musorSzamok = []
f = open("musor.txt","r",encoding="utf-8")
for sor in f:
    #eltávolítjuk a sor végéről az entereket
    sor = sor.replace("\n","")
    #feldaraboljuk az adott sort
    adatok = sor.split(" ")
    #elemntjük a szotárba egyesével az adatokat
    szotar = {}
    szotar['sorszam'] = int(adatok[0])  #1
    szotar['perc'] = int(adatok[1]) #5
    szotar['mp'] = int(adatok[2]) #3
    #mivel nem tudjuk hány db az utolsó adat ezért ciklusba rakjuk
    utolsoAdat = ""
    for x in range(3,len(adatok)):
        utolsoAdat += adatok[x]+" "
    szotar['azonosito'] = utolsoAdat
    musorSzamok.append(szotar)
f.close()
#print(musorSzamok)
print(musorSzamok[8]['azonosito'])