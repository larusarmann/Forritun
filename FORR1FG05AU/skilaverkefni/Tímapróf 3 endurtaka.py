#Lárus Ármann Kjartansson
#10/12/2019
#Tímapróf 3
import random

on = True
while on == True:
    print("1. sléttar tölur")
    print("2. Randomtölur")
    print("3. Texti")
    print("4. samanburður")
    print("5. hætta")
    val = int(input("Veldu hvað þú villt gera"))

    if val == 1:
        for n in range(100, 400):
            if n % 2 == 0:
                print(n, end=" ")

    elif val == 2:
        listi1 = []
        listi2 = []
        listi3 = []
        for x in range(100):
            randomtala = random.randint(100, 201)
            listi1.append(randomtala)
        teljari = 0
        for number in listi1:
            if (number % 3 == 0):
                listi3.append(number)
        for x in listi1:
            if (x > 150):
                listi2.append(x)
            if (x == 151):
                teljari = teljari + 1
        summa = sum(listi3)
        lengd = len(listi3)
        medallengd = summa / lengd
        aukastafir = round(medallengd, 2)
        print("summa talnana er:", sum(listi1))
        print("talan 151 kom", teljari, "sinnum")
        print("meðaltal talnana sem gekk upp í 3 er:",aukastafir)
        print("tölurnar yfir 150 eru:", sorted(listi2))

    elif val == 3:
        teljari = 0
        teljari1 = 0
        texti = input("Skrifaðu texta:")
        tel = len(texti.split())
        for i in texti:
            if i == 'K':
                teljari1 = teljari1 + 1
            elif i == 'k':
                teljari = teljari + 1
        print("fjöldi orða: " + str(tel))
        print("fjöldi 'K' ", teljari1)
        print("fjöldi 'k' ", teljari)
    elif val == 4:
        ord1 = input("sláðu inn orð")
        ord2 = input("sláðu inn annað orð")
        stafir1 = ord1[:-2]
        stafir2 = ord2[:-2]
        if stafir1 == stafir2:
            print("síðustu 2 stafirnir eru eins")
        else:
            print("síðustu tveir stafirnir eru ekki eins")
    elif val == 5:
        on = False