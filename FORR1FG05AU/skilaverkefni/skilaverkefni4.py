import random
#Lárus Ármann Kjartansson
#10.10.19
#skilaverkefni 4

on = True
while on == True:
    print("1. 5 sinnum taflan") #val 1
    print("2. ártal") #val 2
    print("3. heiltala") #val 3
    print("4. 1-9") #val 4
    print("5. hætta") #val 5
    val = int(input("Veldu hvað þú villt gera")) #forritið hættir

    if val == 1:
        aftur = "ja" #þetta svar ákveður hvort það eigi að keyra liðin aftur
        while aftur == "ja": #ef svarað er ja heldur forritið afram
            tala = int(input("Sláðu inn heiltölu 10 - 1000")) #tekur við tölu
            if tala % 5 == 0: #chekkar hvort talan sé deilanleg með 5
                print("Þessi tala er í 5 sinnum töflunni!.") #<-- prentar þetta
            aftur = str(input("viltu gera aftur?-ja/nei:")) #spyr hvort vilji keyra forritið aftur

    elif val == 2:
        aftur = "ja"
        while aftur == "ja":
            artal = int(input("Sláðu inn ártal:")) #tekur ártal frá notenda
            if (artal % 4) == 0:#deilir artalinu i 4
                if (artal % 100) == 0:#passar að sé ekki aldamót
                    if (artal % 400) == 0:#nema 4 hvert aldamót
                        print(artal,"er hlaupaár!.") #prentar út
                    else:
                        print(artal, "er ekki hlaupaár!.") #prentar út
                else:
                    print(artal, "er hlaupaár!.") #prentar út
            else:
                print(artal, "er ekki hlaupaár!") #prentar út
            aftur = str(input("viltu gera aftur?-ja/nei:")) #spyr hvort vilji gera forritið aftur

    elif val == 3:
        aftur = "ja"
        while aftur =="ja":
            summa = 1#summa
            tala = int(input("Sláðu inn tölu:")) #tekur tölu frá notenda
            for x in range(tala,0,-1): #for lykkja sem telur niður frá tölu notenda
                print(x)#prentar tölurnar í röð niður afturabak
                summa = summa * x #margfaldar allar tölurnar saman
            print("Summa allra talnanna er", summa)#prentar
            aftur = str(input("viltu gera aftur?-ja/nei:"))#hvort þú viljir keyra forritið aftur

    elif val == 4:
        aftur = "ja"
        while aftur == "ja":
            tala = int(input("Sláðu inn tölu 1-9:")) #tekur tölu frá notenda
            for tala in range(1,tala+1,1):#for lykkja fyrir hversu oft á að bæta við línu af * merkjum
                print("*" * tala) #prentar
            aftur = str(input("viltu gera aftur?-ja/nei:"))

    elif val == 5:
        on = False #slekkur á forritinu