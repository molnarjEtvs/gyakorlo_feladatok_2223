import os
os.system("cls")

bruttoFizetes = int(input("Add meg a bruttó fizetésed:"))
szja = bruttoFizetes*0.15
tb= bruttoFizetes*0.185
szocho = bruttoFizetes*0.13
netto = bruttoFizetes-szja-tb
munkaltatoKtsg = bruttoFizetes+szocho

print(f"A nettó fizetésed: {netto} Ft")
print(f"Levonásra kerül: ")
print(f"Szja: {szja} Ft")
print(f"Tb: {tb} Ft")
print(f"Ez a munkáltatónak {munkaltatoKtsg} Ft-ba kerül")