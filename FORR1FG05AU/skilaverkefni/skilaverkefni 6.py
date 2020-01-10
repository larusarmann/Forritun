#Lárus Ármann Kjartansson
#12/11/2019
#skilaverkefni 6 Listar
import random

on = True
while on == True:
    print("1. random tölur")
    print("2. talnabil")
    print("3. strengjalisti")
    print("4. samanburður")
    print("5. hætta")
    val = int(input("Veldu hvað þú villt gera"))

    if val == 1:
        randomlisti = []
        for x in range (50):
            tala = random.randint(5,70)
            randomlisti.append(tala)
        margfeldi = 1
        for x in randomlisti:
            margfeldi = margfeldi*x
        haesta = max(randomlisti)
        laegsta = min(randomlisti)
        print("margfeldi allra talnanna er:", margfeldi)
        print("hæsta talan er:",haesta)
        print("lægsta talan er:",laegsta)
        print("listin óraðaður:",randomlisti)
        print("listin raðaður:",sorted(randomlisti))
    if val == 2:
        listi = []
        for x in range(2000,3001):
            if x %7 ==0 and x%5!=0:
                listi.append(x)
        print(listi)
    if val == 3:
        ordalisti =[]
        for x in range(10):
            ordid= input("sláðu inn orð")
            ordalisti.append(ordid)
        print(ordalisti)
        print(sorted(ordalisti))
        fjorda =0
        for x in ordalisti:
            if len(x)==4:
                fjorda = fjorda +1
        print("fjöldi orða með 4 stafi er:",fjorda)

        staf = input("veldu staf til að eyða úr orði")
        nyrlisti= []
        for x in ordalisti:
            if x[0] != staf:
                nyrlisti.append(x)
        print("eftir að eytt hefur verið:",nyrlisti)
    if val == 4:
        pass
    if val == 5:
        on = False