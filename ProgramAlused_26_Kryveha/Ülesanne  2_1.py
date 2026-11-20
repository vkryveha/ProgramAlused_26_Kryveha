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
# pinginaabrid=["Anna","Vika"]
# nimi1=input("Siseta esimese inimese nimi: ")
# nimi2=input("Siseta teise inimese nimi: ")
# if nimi1.isalpha() and nimi2.isalpha():
#         if nimi1.capitalize() in pinginaabrid and nimi2.capitalize() in pinginaabrid:
#             print(f"{nimi1} ja {nimi2} on täna pinginaabrid.")
#         else:
#             print(f"{nimi1} ja {nimi2} ei ole täna pinginaabrid.")
# else:
#         print("Viga: nimed peavad koosnema ainult tähtedest.")

#         #otsing nimede algustähtede järgi
# valik=input("Kas soovid  otsida nimede algustähtede järgi? (jah/ei): ").lower()
# if valik=="jah":
#     algustäht=input("Siseta algustäht: ").capitalize()
#     for nimi in pinginaabrid: 
#         if nimi.startswith(algustäht):
#             print(f"{nimi} algab tähega {algustäht}")
#             otsing=True
#     if not otsing:
#         print(f"Ühtegi nime, mis algab tähega {algustäht}, ei leitud.")

# else:
#     print("Otsingut ei tehta.")


    

# #Ülesanne 3
# try:
#     pikkus=float(input("Sisesta toa pikkus meetrites: "))
#     laius=float(input("Sisesta toa laius meetrites: "))
#     pindala=pikkus*laius
#     print(f"Põranda pindala on {round(pindala, 2)} ruutmeetrit.")
# except ValueError:
#     print("Viga: Palun sisesta numbrilised väärtused pikkuse ja laiuse jaoks.")

# valik=input("Kas soovid remonti teha? (jah/ei): ").lower()
# if valik=="jah":
#     hind=float(input("Sisesta ruutmeetri hind: "))
#     poranda_hind=pindala*hind
#     print(f"Põranda vahetamise hind on {round(poranda_hind, 2)} eurot.")

# #lisaküsimus
#     tegija=input("Kas teed remondi ise või kasutad professionaali abi? (ise/professionaal): ").lower()
#     if tegija=="professionaal":
#         too_hind=float(input("Sisesta töö hind ruutmeetri kohta: "))
#         koguhind=poranda_hind+(pindala*too_hind)
#         print(f"Remondi koguhind koos tööga on {round(koguhind, 2)} eurot.")
#     else:
#         print(f"Remondi koguhind on {round(poranda_hind, 2)} eurot.")
# else:
#     print("Remonti ei tehta.")
   
#    #Ülesanne 4
# try:
#     alghind = float(input("Sisesta toote alghind: "))
#     if alghind > 700: 
#         lopp_hind = round(alghind * 0.7, 2)
#     else:
#         lopp_hind = round(alghind, 2)
#     print(f"Toote lõplik hind on {lopp_hind:.2f} eurot.")
# except ValueError: 
#     print("Viga: Palun sisesta numbriline väärtus alhinna jaoks.")  
  
#    #Ülesanne 5
# try:
#     temperatuur = float(input("Sisesta toatemperatuur: "))
#     if temperatuur > 18:
#         print("Toas on piisavalt soe.")
#     else:
#          print("Toas on liiga külm.")
# except ValueError:
#      print("Viga: Palun sisesta temperatuur numbrina.")
   
   #Ülesanne 6
# Lühike: alla 160 cm
# Keskmine: 160–180 cm
# Pikk: üle 180 cm

# try:
#     pikkus = float(input("Sisesta pikkus sentimeetrites: "))

#     if pikkus < 160:
#         print("Sa oled lühike.")
#     elif pikkus <= 180:
#         print("Sa oled keskmise pikkusega.")
#     else:
#         print("Sa oled pikk.")

# except ValueError:
#     print("Viga: Palun sisesta pikkus numbrina.")
  #Ülesanne 7

# try:
#     pikkus = float(input("Sisesta pikkus sentimeetrites: "))
#     sugu = input("Sisesta sugu: ").lower()

#     if sugu == "mees" or sugu == "m":
#         if pikkus < 170:
#             print("Lühike")
#         elif pikkus <= 185:
#             print("Keskmine")
#         else:
#             print("Pikk")

#     elif sugu == "naine" or sugu == "n":
#         if pikkus < 160:
#             print("Lühike")
#         elif pikkus <= 175:
#             print("Keskmine")
#         else:
#             print("Pikk")

#     else:
#         print("Viga: vale sugu!")

# except ValueError:
#     print("Viga: sisesta pikkus numbrina.")
    

#Ülesanne 8
# arve="Toode   Kogus   Hint   Kokku\n"
# valik=input("Kas soovid osta piima? (jah/ei): ")
# if valik.lower()=="jah":
#         kogus=input("Kui palju piima soovid osta (täisarv): ")
#         if kogus.isdigit():
#            kogus=int(kogus)
#            piim_hind=round(uniform(0.5, 3), 2)
#            print(f"Piima hind on {piim_hind} eurot.")
#            summa+=kogus*piim_hind
#            print(f"Piima kogusumma on {kogus*piim_hind} eurot.")
#            arve+=f"piim {kogus} {piim_hind}€  "
# else:
#     print("Selge: Piima ei taha")
# print(f"Kogusumma on:{round(summa,2)} eurot.")



# valik=input("Kas soovid osta sai? (jah/ei): ")
# if valik.lower()=="jah":
#         kogus=input("Kui palju sai soovid osta (täisarv): ")
#         if kogus.isdigit():
#             kogus=int(kogus)
#             sai_hind=round(uniform(0.5, 3), 2)
#             print(f"Sai hind on {sai_hind} eurot.")
#             summa+=kogus*sai_hind
#             print(f"Sai kogusumma on {kogus*sai_hind} eurot.")
#             arve+=f"sai {kogus} {sai_hind}€  "
# else:
#     print("Selge: Sai ei taha")
# print(f"Kogusumma on:{round(summa,2)} eurot.")