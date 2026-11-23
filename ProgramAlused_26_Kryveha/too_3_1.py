while True:
    print("Vali ülesanne:")
    print("1")
    print("2")
    print("3")
    print("4")
    print("5")
    valik=input("Sisesta ülesande number (1-5) või 'q' väljumiseks: ")

if valik=='1':
    i=0
    kogus=0
    while i < 15:
        arv= float(input(f"{i+1}. arv: "))
        if arv.is_integer():
            kogus+= 1
        i += 1
    print("Täisarve:", kogus)


elif valik=='2':
    try:
        while True:
            A=int(input("Sisesta arv A: "))
            if A > 0:
                summa=0
                for i in range(1, A + 1):
                    summa +=i
                print("Summa:", summa)
                break
            else:
                print("palun sisetsa positiivne täisarv")
    except ValueError:
        print("Palun sisesta kehtiv täisarv.")
elif valik=='3':
    try:
    korrutis = 1   
    for i in range(8):
        arv = float(input(f"{i + 1}. arv: "))
        if arv > 0:
            korrutis *= arv
    print("Positiivsete arvude korrutis:", korrutis)
except ValueError:
    print("Palun sisetsa ainult nombrit. ")
elif valik=='4':
     while True:
   for i in range(10, 21):
    print(f"{i} ruut on {i ** 2}")
elif valik=='5':
    try:
     while True:
       N= int(input("Mitu arvu sisestad (N)? "))
       if N >
    summa = 0
    for i in range(N):
        arv = float(input(f"{i + 1}. arv: "))
        if arv < 0:
            summa += arv
    print("Negatiivsete arvude summa:", summa)
except ValueError:
    print("Palun sisesta kehtiv arv!")
elif valik=='6':
    try:
    N = int(input("Mitu arvu sisestad (N)? "))
    neg = 0
    pos = 0
    nullid = 0
    for i in range(N):
        arv = float(input(f"{i + 1}. arv: "))
        if arv < 0:
            neg += 1
        elif arv > 0:
            pos += 1
        else:
            nullid += 1
    print("Negatiivseid:", neg)
    print("Positiivseid:", pos)
    print("Nulle:", nullid)
except ValueError:
    print("Palun sisesta kehtiv arv!")




















    #1
i=0
kogus=0
while i < 15:
    arv= float(input(f"{i+1}. arv: "))
    if arv.is_integer():
        kogus+= 1
    i += 1
print("Täisarve:", kogus)


#2
try:
    while True:
        A=int(input("Sisesta arv A: "))
        if A > 0:
            summa=0
            for i in range(1, A + 1):
                summa +=i
            print("Summa:", summa)
            break
        else:
            print("palun sisetsa positiivne täisarv")
except ValueError:
    print("Palun sisesta kehtiv täisarv.")


    #3 Sisestatakse 8 arvu
try:
    korrutis = 1
    for i in range(8):
        arv = float(input(f"{i + 1}. arv: "))
        if arv > 0:
            korrutis *= arv
    print("Positiivsete arvude korrutis:", korrutis)
except ValueError:
    print("Palun sisetsa ainult nombrit. ")


   #4

    while True:
   for i in range(10, 21):
    print(f"{i} ruut on {i ** 2}")

    #5
 try:
     while True:
       N= int(input("Mitu arvu sisestad (N)? "))
       if N >
    summa = 0
    for i in range(N):
        arv = float(input(f"{i + 1}. arv: "))
        if arv < 0:
            summa += arv
    print("Negatiivsete arvude summa:", summa)
except ValueError:
    print("Palun sisesta kehtiv arv!")
     
    #6
    try:
    N = int(input("Mitu arvu sisestad (N)? "))
    neg = 0
    pos = 0
    nullid = 0
    for i in range(N):
        arv = float(input(f"{i + 1}. arv: "))
        if arv < 0:
            neg += 1
        elif arv > 0:
            pos += 1
        else:
            nullid += 1
    print("Negatiivseid:", neg)
    print("Positiivseid:", pos)
    print("Nulle:", nullid)
except ValueError:
    print("Palun sisesta kehtiv arv!")


