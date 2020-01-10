#Lárus Ármann Kjartansson
#10.03.19
#For og Range æfing

on = True
while on == True:
    print("1. innslegið talnabil")
    print("2. Oddaölur 1-99")
    print("3. Summa 1-15")
    print("4. Hætta")
    val=int(input("Veldu hvað þú villt gera"))

    if val ==1:
            byrjun = int(input("Hvar viltu byrja:"))
            endir = int(input("Hvar viltu enda:"))
            if endir == byrjun:
                print("Ekki nota sömu töluna tvisvar")
            elif endir - byrjun <= 1:
                print("Það þarf að hafa meiri bil á milli talnanna")
            else:
                for x in range(byrjun+1,endir):
                    print(x)
    elif val == 2:
        for x in range(1, 100, 2):
            print(x)
    elif val == 3:
        summa = 0
        for x in range(1, 16):
            summa = summa + x
            print("Samtals er þetta:", summa)
    elif val == 4:
        on = False