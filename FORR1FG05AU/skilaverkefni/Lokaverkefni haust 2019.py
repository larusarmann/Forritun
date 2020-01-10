#Lárus Ármann Kjartansson
#19/11/2019
#Lokeverkefni 20%
import random

on = True
while on == True:
    print("1. Fótboltalið")
    print("2. Þversumma")
    print("3. Skæri Blað Steinn")
    print("4. Texti")
    print("5. Heiltölur")
    print("6. Teningaspilið Craps")
    print("7. Hangman")
    print("8. hætta")
    val = int(input("Veldu hvað þú villt gera"))

    if val == 1:
        maeting = int(input("Fjöldi þáttakenda?")) #fæ að vita fjölda þáttakenda
        lid = int(input("Fjöldi í hverju liði?")) #fæ að vita fjölda liða
        lid2 = maeting // lid #hér er reiknað mæting deilt í lið = lid2
        afglid = maeting % lid #hér fer auka fólk til að vita hversu margir varamenn eru
        if maeting < lid: #ef að það eru færri fólk en þarf í lið
            print("Ekki næst í lið með þennan fjölda þáttakenda")#prentar þetta
        else: #annars prentar niðurstöður
            print("niðurstöður:")
            print("liðafjöldi:", lid2)
            print("Varamenn:", afglid)

    elif val == 2: # val 2
        tala = 1
        tala = int(input("sláðu inn tölu")) #input
        summa = 0
        if tala >0: #ef talan er stærri en 0
            for x in range(1,tala+1):
                summa = summa + tala #teljari
                if x == tala: #ef x = tala
                    print(x, end =" = ") #prentar
                else: #annars prentar þetta
                    print(x, end="+")
            print(summa)
        elif tala <0: #ef talan er minni en 0
            for x in range(tala,0):
                summa = summa + tala
                if x == -1:
                    print("(",x,")", end=" = ")
                else:
                    print("(",x,")", end="+")
            print(summa)

    elif val == 3:
        fulltnafn = input("hvað heitir þú?(fullt nafn): ") #input
        aldur = input("hvað ert þú gamall/gömul: ") #input
        vinn = 0 #teljari
        tap = 0 #teljari
        jafntefli = 0 #teljari
        on = True
        while on is True:
            print("1. Skæri") #prentar
            print("2. Blað") #prentar
            print("3. Steinn") #prentar
            print("4. Hætta") #prentar
            val = int(input("Veldu hvað þú vilt gera: ")) #input
            if val == 1:
                randtala = random.randint(0, 2) #random tala frá 0-2
                if randtala == 0: #ef tala = 0 þá er jafntefli
                    print("Jafntefli")
                    jafntefli = jafntefli + 1 #bætir við í teljarann
                elif randtala == 1: # tala = 1 þá er vinn
                    print(fulltnafn, "vinnur, talvan valdi Blað")
                    vinn = vinn + 1 #bætir við teljarann
                elif randtala == 2:# tala = 2 þá er tap
                    print(fulltnafn, "tapar, talvan valdi Steinn")
                    tap = tap + 1 #bætir við teljarann
            if val == 2: #þetta er það sama og fyrra svo ég sleppi því að kommenta allt aftur
                randtala = random.randint(0, 2)
                if randtala == 0:
                    print("Jafntefli")
                    jafntefli = jafntefli + 1
                elif randtala == 1:
                    print(fulltnafn, "vinnur, talvan valdi Steinn")
                    vinn = vinn + 1
                elif randtala == 2:
                    print(fulltnafn, "tapar, talvan valdi Skæri")
                    tap = tap + 1
            if val == 3:
                randtala = random.randint(0, 2)
                if randtala == 0:
                    print("Jafntefli")
                    jafntefli = jafntefli + 1
                elif randtala == 1:
                    print(fulltnafn, "vinnur, talvan valdi Skæri")
                    vinn = vinn + 1
                elif randtala == 2:
                    print(fulltnafn, "tapar, talvan valdi Blað")
                    tap = tap + 1
            if val == 4: #prentar út hversu oft leikmaður vann,tapaði,jafntefli og hversu oft var spilað
                print(fulltnafn)
                print(aldur,"ára")
                print("samtals spilaðir þú", vinn + tap + jafntefli, "sinnum")
                print("þú vannst", vinn,"sinnum")
                print("þú tapaðir", tap,"sinnum")
                print("það var jafntefli", jafntefli,"sinnum")
                break #breakar loopið

    elif val == 4:
        texti = str(input("sláðu inn orð/setningu")) #input
        stafir = ["J","j","b","l","n"] #stafir sem á að halda
        for x in stafir:
            texti = texti.replace(x, "*") #skiptir út stafinum fyrir *
            texti = texti.replace(" ", "_") #skiptir út bilum með "_"
        print(texti) #prentar
    elif val == 5:
        listi = [] #segjir að þetta sé listi
        for x in range(0, 12, 1): #for lykkja til að taka 12 heiltölur
            listi.append(int(input("sláðu inn heiltölu")))
        print("minnsta talan er:", min(listi)) #prentar
        print("stærsta talan er:", max(listi)) #prentar
        print("summa listans er:", sum(listi)) #prentar
        print("meðaltal listans er:", sum(listi)/12) #prentar

    elif val == 6:
        teningur1 = random.randint(1, 6) #random teningakast
        teningur2 = random.randint(1, 6) #random teningakast
        teljari = 1 #teljari
        summa = teningur1 + teningur2 #plúsar teningana saman
        print("Í 1 kasti fékkst þú",summa) #prentar
        if summa == 7 or summa == 11: #ef summa er 7 eða 11
            print("leikmaður vann") #prentar
        elif summa == 2 or summa == 3 or summa == 12: #ef summan er 2, 3 eða 12 þá vinnur húsið
            print("húsið vinnur") #prentar
        else:
            running = True #þannig að forritið reyni aftur og aftur þangað til að annað hvort leikmaður eða hús vinnur
            while running == True:
                teningur1 = random.randint(1, 6) #random teningur
                teningur2 = random.randint(1, 6) #random teningur
                summa1 = teningur1 + teningur2 #summa teninga
                teljari = teljari + 1 #teljari
                print("Í",teljari,"kasti fékkst þú",summa1,"það er vitlaust!, Reyndu aftur") #prentar
                if summa1 == 7:
                    print("húsið vinnur, húsið náði 7 áður enn að þú náðir",summa) #prentar
                    running = False #breakar loop
                elif summa1 == summa:
                    print("leikmaður vinnur, Þú náðir sömu tölunni og í fyrsta kasti") #prentar
                    running = False #breakar loopið
    elif val == 7:
        i = False
        while i == False:
            nafn = input("Hvað heitir þú? ") #input
            print("Halló", nafn,":", "gangi þér vel i hengimanni") #prentar
            print("Þú hefur 12 líf") #prentar
            list = ["forritun", "tolva", "python", "superman", "banani", "tækniskolinn", "flugvel", "turn", "eldur",
                    "sprengja", "heyrnartol", "hugmynd", "fugl", "ananas", "epli"] #sýnir að það sé listi
            list2 = [] #listi 2 til að geyma notaða stafi
            randint = random.randint(0, 14) #random orð úr listanum á milli 0 til 14
            ord = list[randint]
            gisk = ""
            lif = 12 #hversu mörg líf á að vera
            while lif > 0: #ef að þú ert ekki búin að tapa
                fails = 0
                for char in ord:
                    if char in gisk:
                        print(char, end=' ') #prentar
                    else:
                        print("_", end=' ') #prentar
                        fails += 1
                if fails == 0:
                    print("Þú vannst") #prentar

                    break

                stafur = input("Giskaðu á staf: ") #input
                if stafur not in list2: #ef stafur ekki í list2
                    list2.append(stafur) #bætir við í lista
                    gisk += stafur
                    if stafur not in ord: #ef stafur er ekki í orðinu
                        lif -= 1 #dregur frá 1 líf
                        print("Rangt, reyndu aftur") #prentar
                        print("Þú hefur", lif, "líf eftir") #prentar
                else:#segir að þú hafir slegið það inn áður
                    print("þú hefur slegið inn þetta áður") #prentar
                    print("þetta er/eru stafirnir sem þú hefur slegið inn",list2) #prentar
            if lif == 0: #ef að líf er 0 þá tapar þú
                print("Þú tapaðir") #prentar
                print("orðið var:", ord) #prentar

            aftur = str(input("Viltu spila aftur? (ja/nei) ")).lower() #input
            if aftur == "nei":
                break

    elif val == 8:
        on = False
