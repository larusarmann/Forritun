#Lárus Ármann Kjartansson
#26/11/2019
#Tímapróf 3
import random

on = True
while on == True:
    print("1. Oddatölur")
    print("2. Randomtölur")
    print("3. Texti")
    print("4. hætta")
    val = int(input("Veldu hvað þú villt gera"))

    if val == 1:
        for n in range(100, 400):
            if n % 2 == 1:
                print(n, end=":")
    elif val == 2:
        listi1 = []
        listi2 = []
        for x in range(100):
            randomtala = random.randint(200, 300)
            listi1.append(randomtala)
        teljari = 0
        for x in listi1:
            if (x > 250):
                listi2.append(x)
            if (x == 251):
                teljari = teljari + 1
        print("summa talnana er:",sum(listi1))
        print("talan 251 kom",teljari,"sinnum")
        print("tölurnar yfir 250 eru:",sorted(listi2))


    elif val == 3:
        text = input("Segðu eithvað: ")
        print("óbreytt texti : " + text)
        res = len(text.split())
        print("fjöldi orða: " + str(res))
        print("fjöldi 'n' í textanum", text.count('n'))
        stafir = ["a", "á", "b", "d", "ð", "e", "é", "f", "g", "h", "i", "í", "j", "k", "l", "m", "o", "ó", "p", "r",
                  "s", "t", "u", "ú", "v", "x", "y", "ý", "þ", "æ", "ö"]
        for x in stafir:
            if stafir != ["n", "N"]:
                pass
            else:
                texti = text.replace(x, "#")
        print(texti)

    elif val == 4:
        on = False