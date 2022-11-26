import os
os.system("cls")

focimerkozesek = []
f = open("meccs.txt","r",encoding="utf-8")
for row in f:
    row = row.replace("\n","")
    meccsAdat = row.split(" ")
    szotar = {}
    szotar['fordulo'] = int(meccsAdat[0])
    szotar['hazai_gol_ve'] = int(meccsAdat[1])
    szotar['vendeg_gol_ve'] = int(meccsAdat[2])
    szotar['hazai_gol_fi'] = int(meccsAdat[3])
    szotar['vendeg_gol_fi'] = int(meccsAdat[4])
    szotar['hazai_nev'] = meccsAdat[5]
    szotar['vendeg_nev'] = meccsAdat[6]
    focimerkozesek.append(szotar)

f.close()
#print(focimerkozesek[4]['hazai_nev'])