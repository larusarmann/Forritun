#Lárus Ármann Kjartansson
#10.03.19
#random æfing
import random

on = True
while on == True:
    print("1. teningakast3")
    print("2. yatzi kast")
    print("3. finna oddatölur")
    print("5. Break - True og false")
    print("6. Hætta")
    val = int(input("hvað viltu gera"))

    if val ==1:
        tala = random.randint(1,6)
        print("kastið er", tala)
    elif val ==2:
        for x in range (1,6):
            tala = random.randint(1,6)
            print("teningur ",x,"er",tala)
    elif val ==3:
        summa=0
        oddasumma=0
        for x in range(25):
            randomtala = random.randint(1,100)
            summa = summa + randomtala
            if randomtala %2 != 0:
                print("hei ég fann oddatölu", randomtala)
                oddasumma = oddasumma +randomtala
            else:
                print(randomtala)
            print("heildarsumman er;",summa)
            print("summa oddatalna er:",oddasumma)
    elif val ==5:
        fann99=False
        for x in range(250):
            randomtala = random.randint(25,115)
            if randomtala ==73:
                print("STOPP!",randomtala)
                break
            if randomtala == 99:
                fann99=True
            print(randomtala)
        if fann99 ==True:
            print("talan 99 kom upp amk 1 sinni")
    elif val ==6:
        on = False