 # Ülesanne 1

from datetime import *

täna = date.today()
print(f"Täna on {täna}")

print(täna.strftime("%d/%m/%Y"))
print(täna.strftime("%B %d, %Y"))
print(täna.strftime("%m/%d/%y"))
print(täna.strftime("%b-%d-%Y"))


# Ülesanne 2

print(3 + 8 / (4 - 2) * 4)
print(3 + 8 / 4 - 2 * 4)
print((3 + 8) / (4 - 2) * 4)


# Ülesanne 3

from math import *

R = float(input("Sisesta ringi raadius: "))

ruudu_pindala = (2 * R) ** 2
ruudu_umbermoot = 8 * R

ringi_pindala = pi * R ** 2
ringi_umbermoot = 2 * pi * R

print("Ruudu pindala:", ruudu_pindala)
print("Ruudu ümbermõõt:", ruudu_umbermoot)
print("Ringi pindala:", ringi_pindala)
print("Ringi ümbermõõt:", ringi_umbermoot)


# Ülesanne 4

from math import *

maa_raadius = 6378
mundi_labimoot = 0.02575

maa_umbermoot = 2 * pi * maa_raadius
muntide_arv = maa_umbermoot / (mundi_labimoot / 1000)

print("Maa ümbermõõt:", maa_umbermoot, "km")
print("Müntide arv:", round(muntide_arv))


# Ülesanne 5

sona = "kill-koll"

print((sona + " ") * 2 + "killadi-koll", end=" ")
print((sona + " ") * 2 + "killadi-koll", end=" ")
print((sona + " ") * 3)
print(sona)


# Ülesanne 6
laul = """
Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?

Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill."""

print(laul.upper())


# Ülesanne 7

a = float(input("Sisesta esimene külg: "))
b = float(input("Sisesta teine külg: "))

umbermoot = 2 * (a + b)
pindala = a * b

print("Ümbermõõt:", umbermoot)
print("Pindala:", pindala)


# Ülesanne 8

liitrid = float(input("Sisesta kütuse liitrid: "))
kilomeetrid = float(input("Sisesta läbitud kilomeetrid: "))

kulu = liitrid / kilomeetrid * 100

print("Kütusekulu 100 km kohta:", kulu)


# Ülesanne 9
try:
    kiirus = 29.9
    minutid = float(input("Sisesta minutid: "))

    kaugus = kiirus * minutid / 60

    print("Läbitud kaugus:", kaugus, "km")
except ValueError:

# Ülesanne 10
try:
    minutid = int(input("Sisesta minutid: "))

    tunnid = minutid // 60
    jaak = minutid % 60

    print(f"{tunnid}:{jaak:02d}")
except ValueError:
     print("Palun sisesta täisarv!")
