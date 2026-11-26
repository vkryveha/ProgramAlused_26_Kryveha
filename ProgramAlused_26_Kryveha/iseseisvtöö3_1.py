#17 
arv = int(input("Sisesta arv:"))

for i in range(1, 10):
    tulemus = arv * i
    print(arv, "*", i, "=", tulemus)

#18
for i in range(20, 51):
    if i % 3 == 0 and i % 5 == 1:
        print(i)

#22
summa = 0

for i in range(100, 201):
    if i % 17 == 0:
        summa = summa + i

print(summa)
 #31 
K = int(input("Mitu kotletti? "))
M = int(input("Mitu kotletti mahub pannile? "))

tais = K // M
jaak = K - tais * M

if jaak > 0:
    tais = tais + 1

print("Täis pannitäisi:", tais)
print("Ülejäänud kotletid:", jaak)

#20
summa = 0

for i in range(1, 51):
    if i % 5 == 0 or i % 7 == 1:
        summa = summa + 1 

print("Summa:", summa)

 

