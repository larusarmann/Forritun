#Lárus Ármann Kjartansson
#07/11/19
#æfingaverkefni listar
import random

on = True
while on == True:
    print("1. innkaupalisti")
    print("2. Random tölur")
    print("3. Fyrsta og síðasta")
    print("4. Nemendur")
    print("5. Hætta")
    val = int(input("Veldu hvað þú vilt gera:"))

    if val == 1:
        svar = "ja"
        innkaupalisti=[]
        while svar == "ja":
            vara = input("hvað viltu kaupa")
            innkaupalisti.append(vara)
            svar = input("viltu kaupa meira ja/nei")
        print("innkaupalistinn er:")
        list.sort(innkaupalisti)
        for x in innkaupalisti:
            print("- ", x)
    elif val == 2:
        randomlisti =[]
        for x in range(15):
            tala = random.randint(5,25)
            randomlisti.append(tala)
            randomlisti.sort()
            randomlisti1 = max(randomlisti)
            randomlisti2 = min(randomlisti)
            randomlisti3 = len(randomlisti)
        print(randomlisti)
        print(randomlisti1)
        print(randomlisti2)
        print(randomlisti3)

    elif val == 3:
        randlisti = []
        nyr = []
        for x in range(20):
            tala = random.randint(1,100)
            randlisti.append(tala)
        print(randlisti)
        fyrsti = randlisti[0]
        sidasti = randlisti[-1]
        nyr.append(fyrsti)
        nyr.append(sidasti)
        print(nyr)

    elif val == 4:
        nafnalisti =[]
        teljari = 0
        while teljari <10:
            nafn =input("sláðu inn nafn")
            if nafn in nafnalisti:
                print("mátt ekki slá inn sama nafn tvisvar")
            else:
                nafnalisti.append(nafn)
                nafnalisti.sort()
                teljari = teljari +1
        print(nafnalisti)
    elif val == 5:
        on = False