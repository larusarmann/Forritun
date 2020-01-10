#Lárus Ármann Kjartansson
#31.10.19
#tímaverkefni 2

on = True
while on == True:
    print("1. metrar, desimetrar og sentimetrar")
    print("2. veldi")
    print("3. heiltala")
    print("4. hætta")
    val = int(input("Veldu hvað þú villt gera"))

    if val == 1:
        aftur = "ja"
        while aftur == "ja":
            senti = int(input("sláðu inn fjölda sentimetra"))
            meter = senti // 100
            afgmetri = senti % 100
            desimetri = afgmetri // 10
            sentimetri = afgmetri % 10
            print(meter, "metrar")
            print(desimetri, "desimetrar")
            print(sentimetri, "sentimetrar")
            aftur=str(input("viltu gera aftur ja/nei"))
    elif val == 2:
        aftur = "ja"
        while aftur == "ja":
            tala = int(input("Sláðu inn tölu:"))
            veldi = int(input("Sláðu inn veldisvísi:"))
            summa = (tala ** veldi)
            print(summa)
            aftur = str(input("viltu gera aftur ja/nei"))
    elif val ==3:
         tala=int(input("sláðu inn tölu á mill 1-9"))
         for i in range(-int(tala), int(tala) + 1, 1): print(abs(i) * "*")
    elif val ==4:
        on = False
