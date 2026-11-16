# #Ülesanne 1
# eesnimi=input("Siseta eesnimi: ")
# if eesnimi.upper()=="JUKU":
#     print("Lähme Jukuga kinno!")
#     if eesnimi.isupper():
#         print("Ära karju; Juku!")
#     elif eesnimi.islower():
#         print("Ära sosita, Juku!")
#     try:   
#         vanus=int(input("Kui vana sa oled, Juku? "))
#         if 0 <=vanus < 6:
#             pilet="tasupilet"
#         elif 6 <= vanus <= 14:
#             pilet="lastepilet"
#         elif 15 < vanus < 65:
#             pilet="täispilet"
#         elif 65 <=vanus <100:
#             pilet="sooduspilet"
#         else:
#             print("Viga andmetes")
#         print(f"Juku vanus on  {vanus} aastat, seega on vaja osta {pilet}. ")
#     except ValueError:
#         print("Palun siseta oma vanusnumbrina.")
# else:
#     print("Täna kinno ei minna.")


    #Ülesanne 2
pinginaabrid=["Anna","Vika"]
nimi1=input("Siseta esimese inimese nimi: ")
nimi2=input("Siseta teise inimese nimi: ")
if nimi1.isalpha() and nimi2.isalpha():
        if nimi1.capitalize() in pinginaabrid and nimi2.capitalize() in pinginaabrid:
            print(f"{nimi1} ja {nimi2} on täna pinginaabrid.")
        else:
            print(f"{nimi1} ja {nimi2} ei ole täna pinginaabrid.")
else:
        print("Viga: nimed peavad koosnema ainult tähtedest.")

        #otsing nimede algustähtede järgi
valik=input("Kas soovid  otsida nimede algustähtede järgi? (jah/ei): ").lower()
if valik=="jah":
    algustäht=input("Siseta algustäht: ").capitalize()
    for nimi in pinginaabrid: 
        if nimi.startswith(algustäht):
            print(f"{nimi} algab tähega {algustäht}")
            otsing=True
    if not otsing:
        print(f"Ühtegi nime, mis algab tähega {algustäht}, ei leitud.")

else:
    print("Otsingut ei tehta.")


    

#Ülesanne 3
try:
    pikkus=float(input("Sisesta toa pikkus meetrites: "))
    laius=float(input("Sisesta toa laius meetrites: "))
    pindala=pikkus*laius
    print(f"Põranda pindala on {round(pindala, 2)} ruutmeetrit.")
except ValueError:
    print("Viga: Palun sisesta numbrilised väärtused pikkuse ja laiuse jaoks.")

valik=input("Kas soovid remonti teha? (jah/ei): ").lower()
if valik=="jah":
    hind=float(input("Sisesta ruutmeetri hind: "))
    poranda_hind=pindala*hind
    print(f"Põranda vahetamise hind on {round(poranda_hind, 2)} eurot.")

#lisaküsimus
    tegija=input("Kas teed remondi ise või kasutad professionaali abi? (ise/professionaal): ").lower()
    if tegija=="professionaal":
        too_hind=float(input("Sisesta töö hind ruutmeetri kohta: "))
        koguhind=poranda_hind+(pindala*too_hind)
        print(f"Remondi koguhind koos tööga on {round(koguhind, 2)} eurot.")
    else:
        print(f"Remondi koguhind on {round(poranda_hind, 2)} eurot.")
else:
    print("Remonti ei tehta.")
