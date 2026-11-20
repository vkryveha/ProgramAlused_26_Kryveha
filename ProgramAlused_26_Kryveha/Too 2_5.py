print("Arvu kontroll")  #ma panesin "
arv=input("Sisesta täisarv => ")
if arv>0:     
    print("Arv on positiivne")
elif arv==0:
    print("Arv on null")
else:
    print("Arv on negatiivne")
if arv%2==0:
    print("Arv on paarisarv")
else:
    print("Arv on paaritu")
print()
print("Kehamassiindeks")
mass=float(input("Sisesta kaal (kg) => "))
pikkus=float(input("Sisesta pikkus (m) => "))
kmi=mass/pikkus**2
print("KMI:", round(kmi,1))
if kmi<18.5:
    print("Alakaal")
elif kmi>=18.5:
    print("Normaalkaal")
elif kmi>=25:
    print("Ülekaal")
elif kmi>=30:
    print("Rasvumine")
print()
print("Ostu allahindlus")
summa=float(input("Sisesta ostusumma => "))
if summa<=0:
    print("Vigane summa")
elif summa>100 or summa<=500:
    print("Allahindlus 5%, maksta:", round(summa*0.95,2))
elif summa>500:
    print("Allahindlus 10%, maksta:", round(summa*0.9,2))
else:
    print("Allahindlust pole, maksta:"), summa



# Arvu kontroll
# Sisesta täisarv => 9
# Arv on positiivne
# Arv on paaritu

# Kehamassiindeks
# Sisesta kaal (kg) => 85
# Sisesta pikkus (m) => 1.75
# KMI: 27.8
# Ülekaal
# Ostu allahindlus
# Sisesta ostusumma => 650
# Allahindlus 10%, maksta: 585.0
try:
    valik=int(input("vali ülesanne: "))
    if valik == 1:
        print("arvu kontroll")
        try:
            arv=input("Sisesta täisarv => ")
            if arv>0:     
                print("Arv on positiivne")
            elif arv==0:
                print("Arv on null")
            else:
                print("Arv on negatiivne")
            if arv%2==0:
                print("Arv on paarisarv")
            else:
                 print("Arv on paaritu")
            if arv%3==0:
                print("arv jagub 3 ga")
            else:
                print("arv jagu 3 ga")
        except ValueError:
            print("viga")
    elif valik == 3:
        print()
        print("Ostu allahindlus")
        summa=float(input("Sisesta ostusumma => "))
        if summa<=0:
            print("Vigane summa")
        elif summa>100 or summa<=500:
            print("Allahindlus 5%, maksta:", round(summa*0.95,2))
        elif summa>500:
            print("Allahindlus 10%, maksta:", round(summa*0.9,2))
        else:
             print("Allahindlust pole, maksta:"), summa
except ValueError:
    print("palun siseta number")
