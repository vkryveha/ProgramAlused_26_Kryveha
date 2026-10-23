from random import * #randit
from math import *
#Ülesanne 1
print ("Tere, maailm")
nimi = input("Siseta ona nimi: ")
print(f"Tere, maailm! Tervitan sind {nimi}!")
try:
    vanus=int(input("Siseta oma vanus: "))
    print(f"Tere, maailm! Tervitan sind {nimi}! Sa oled {vanus} aastat vana.")
except ValueError:
    print("Palun siseta kehtiv number vanuse jaoks. ")


#Ülesanne 2
vanus=18
eesnimi="Vika"
pikkus=16.5
kas_käib_koolis=True 
print(f"Vanus:{vanus}, tüüp: {type(vanus)}")
print(f"Eesnimi:{eesnimi}, tüüp: {type(eesnimi)}")
print(f"Pikkus:{pikkus}, tüüp: {type(pikkus)}")
print(f"Käib koolis:{kas_käib_koolis}, tüüp: {type(kas_käib_koolis)}")


#Ülesanne 3
kommide_arv=randint(1,100)        #int(input("Kommide arv: "))
print(f"Laud on {kommide_arv} kommi.")
try:
    kommid=int(input("Mitu kommi soovid ära võtta? "))
    kommide_arv -= kommid
    print(f"Laud on nüüd {kommide_arv} kommi.")
except ValueError: 
    print("Palun siseta number.")


#Ülesanne 4
try:
    ümbermõõt=float(input("Siseta puu ümbermõõt: "))
    läbimõõt=round(ümbermõõt/pi,1)
    print(f"Puu läbimõõt on {läbimõõt}.")
except ValueError:
    print("Palun siseta number.")


#Ülesanne 5 
try:
    N=float(input("Siseta ristküliku esimene külg (N): "))
    M=float(input("Siseta ristküliku esimene külg (M): "))

    diagonaal=round(sqrt(N**2 + M**2), 1)
    print (f"Ristküliku diagonaal on {diagonaal}.")
except ValueError:
    print("Palun siseta kehtiv number.")

#Ülesanne 6 
arv1=randint(1, 100)
arv2=randint(1, 100)
arv3=randint(1, 100)
arv4=randint(1, 100)
arv5=randint(1, 100)
summa=arv1+arv2+arv3+arv4+arv5
try:
    jagaja= int(input("Siseta arv, millega jagada: "))
    tulemus=summa/jagaja
    print("Tulemus:", tulemus)
    print("Täisarvuline osa:", int(tulemus))

    print("Jääk:", summa % jagaja)
except ValueError:
    print("Palun siseta kehtiv number.")