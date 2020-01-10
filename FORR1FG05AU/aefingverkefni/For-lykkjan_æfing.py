#Lárus Ármann Kjartansson
#10.01.19
#Æfing For-Lykkjan

on = True
while on == True:
    print("1. Talnaruna")
    print("2. Slétt talnaruna")
    print("3. Tölur 30-40")
    print("4. 10-33 talnaruna")
    print("5. prenta A")
    print("6. Hætta")
    val=int(input("Veldu hvað þú villt gera"))

    if val ==1:
        print("#Liður 1")
        for stak in range(1, 6):
            print(stak)
    elif val ==2:
        print("#Liður 2")
        for slett in range(2, 12, 2):
            print(slett)
    elif val ==3:
        print("#Liður 3")
        for þrátíu in range(30, 41, 1):
            print(þrátíu)
    elif val ==4:
        print("#Liður 4")
        teljari = 1
        for x in range(10, 34):
            if teljari % 6 == 0:
                print(x)
            else:
                print(x, end=" ")
            teljari = teljari + 1
    elif val ==5:
        print("#liður 5")
        for x in range(1, 6):
            print("A" * x)
    elif val ==6:
        on = False