print("Liigaasta kontroll")   #mina lisatsin "
aasta=input("Sisesta aasta => ")
if aasta%4==0 or aasta%100!=0 or aasta%400==0: #mina lisatsin =
    print("Liigaasta")
else:
    print("Tavaline aasta")  #ma lisatsin t¸hik
print()
print("K¸tusekulu")
km=float(input("Sisesta l‰bitud kilomeetrid => ")) #mina lisatsin )
liitrid=float(input("Sisesta kulunud k¸tus (l) => "))
kulu=liitrid*km/100
print("Kulu 100 km kohta:", round(kulu,1), "l")
if kulu<5:
    print("S‰‰stlik auto")
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
print("Maksta:", round(summa,2), "Ä")
if summa>=30:   #ma parandasin => ja kirjutasin >=
    print("Saad tasuta magustoidu!")
else:
    print("Tasuta magustoiduni on puudu", round(30-summa,2), "Ä") #mina lisatsin )




#     Lisa¸lesanne (kırgema hinde jaoks)
# Muuda programmi nii, et alguses kuvatakse men¸¸ ja k‰ivitub ainult valitud osa. Kui kasutaja sisestab midagi muud kui 1, 2 vıi 3, kuvatakse teade Vigane valik.
# Vali programm:
# 1 - Liigaasta kontroll
# 2 - K¸tusekulu
# 3 - Kohviku arve
# Sisesta valik (1-3) =>
# Lisa liigaasta osasse, mitu p‰eva on sel aastal veebruaris.
# K¸tusekulu osa ei tohi lubada sisestada nulli vıi negatiivset kilomeetrite vıi liitrite arvu.

try:
    print("Vali programm")
    print("1-Liigaasta kontroll")
    print("2-K¸tusekulu")
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
       print("K¸tusekulu")
        try:
            km=float(input("Sisesta l‰bitud kilomeetrid => ")) 
            liitrid=float(input("Sisesta kulunud k¸tus (l) => "))
            kulu=liitrid*km/100
            print("Kulu 100 km kohta:", round(kulu,1), "l")
            if kulu<5:
                print("S‰‰stlik auto")
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
            print("Maksta:", round(summa,2), "Ä")
            if summa>=30:   
                print("Saad tasuta magustoidu!")
            else:
                print("Tasuta magustoiduni on puudu", round(30-summa,2), "Ä")
            else:    
                print("Vigane valik")
        except ValueError:
            print("viga")
except ValueError:
    print("Viga")



    22.
summa = 0

for i in range(100, 201):
    if i % 17 == 0:
        summa = summa + i

print(summa)



31.
K = int(input("Mitu kotletti? "))
M = int(input("Mitu kotletti mahub pannile? "))

tais = K // M
jaak = K % M

print("T‰is pannit‰isi:", tais)
print("Viimasele pannile j‰‰b:", jaak)