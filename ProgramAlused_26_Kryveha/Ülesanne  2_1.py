#Ülesanne 1
eesnimi=input("Siseta eesnimi: ")
if eesnimi.upper()=="JUKU":
    print("Lähme Jukuga kinno!")
    if eesnimi.isupper():
        print("Ära karju; Juku!")
    elif eesnimi.islower():
        print("Ära sosita, Juku!")
    try:   
        vanus=int(input("Kui vana sa oled, Juku? "))
        if 0 <=vanus < 6:
            pilet="tasupilet"
        elif 6 <= vanus <= 14:
            pilet="lastepilet"
        elif 15 < vanus < 65:
            pilet="täispilet"
        elif 65 <=vanus <100:
            pilet="sooduspilet"
        else:
            print("Viga andmetes")
        print(f"Juku vanus on  {vanus} aastat, seega on vaja osta {pilet}. ")
    except ValueError:
        print("Palun siseta oma vanusnumbrina.")
else:
    print("Täna kinno ei minna.")

