print("Liigaasta kontroll")   #mina lisatsin "
aasta=input("Sisesta aasta => ")
if aasta%4==0 or aasta%100!=0 or aasta%400==0: #mina lisatsin =
    print("Liigaasta")
else:
    print("Tavaline aasta")  #ma lisatsin tühik
print()
print("Kütusekulu")
km=float(input("Sisesta läbitud kilomeetrid => ")) #mina lisatsin )
liitrid=float(input("Sisesta kulunud kütus (l) => "))
kulu=liitrid*km/100
print("Kulu 100 km kohta:", round(kulu,1), "l")
if kulu<5:
    print("Säästlik auto")
elif kulu>=5:
    print("Keskmine kulu")
elif kulu>8:  #mina parandasin else if ja kirjutasin elif
    print("Suur kulu")
print()
print("Kohviku arve")
summa=float(input("Sisesta arve summa => "))
kaart=input("Kas sul on kliendikaart (jah/ei)? => ")
if kaart=="jah" and kaart=="JAH":
    summa=summa*0.9
print("Maksta:", round(summa,2), "€")
if summa>=30:   #ma parandasin => ja kirjutasin >=
    print("Saad tasuta magustoidu!")
else:
    print("Tasuta magustoiduni on puudu", round(30-summa,2), "€") #mina lisatsin )




#     Lisaülesanne (kõrgema hinde jaoks)
# Muuda programmi nii, et alguses kuvatakse menüü ja käivitub ainult valitud osa. Kui kasutaja sisestab midagi muud kui 1, 2 või 3, kuvatakse teade Vigane valik.
# Vali programm:
# 1 - Liigaasta kontroll
# 2 - Kütusekulu
# 3 - Kohviku arve
# Sisesta valik (1-3) =>
# Lisa liigaasta osasse, mitu päeva on sel aastal veebruaris.
# Kütusekulu osa ei tohi lubada sisestada nulli või negatiivset kilomeetrite või liitrite arvu.

try:
    print("Vali programm")
    print("1-Liigaasta kontroll")
    print("2-Kütusekulu")
    print("3-Kohviku arve")
    valik=int(input("Sisesta valik (1-3)"))
    if valik==1:
        print("Liigaasta kontroll")   
    try:
        aasta=input("Sisesta aasta => ")
        if aasta%4==0 or aasta%100!=0 or aasta%400==0: 
            print("Liigaasta")
        else:
            print("Tavaline aasta")
        print()
    except ValueError:
        print("viga")
    elif valik==2:
       print("Kütusekulu")
        try:
            km=float(input("Sisesta läbitud kilomeetrid => ")) 
            liitrid=float(input("Sisesta kulunud kütus (l) => "))
            kulu=liitrid*km/100
            print("Kulu 100 km kohta:", round(kulu,1), "l")
            if kulu<5:
                print("Säästlik auto")
            elif kulu>=5:
                print("Keskmine kulu")
            elif kulu>8:  
                print("Suur kulu")
            print()
        except ValueError:
            print("viga")
    elif valik==3:
        print("Kohviku arve")
        try:
            summa=float(input("Sisesta arve summa => "))
            kaart=input("Kas sul on kliendikaart (jah/ei)? => ")
            if kaart=="jah" and kaart=="JAH":
                summa=summa*0.9
            print("Maksta:", round(summa,2), "€")
            if summa>=30:   
                print("Saad tasuta magustoidu!")
            else:
                print("Tasuta magustoiduni on puudu", round(30-summa,2), "€")
            else:    
                print("Vigane valik")
        except ValueError:
            print("viga")
except ValueError:
    print("Viga")