#Lárus Ármann Kjartansson
#Skilaverkefni 5
#Strengir

on = True
while on == True:
    print("1. kennitala")
    print("2. búa til nýtt orð")
    print("3. sneið af streng")
    print("4. hætta")
    val = int(input("Veldu hvað þú villt gera"))

    if val==1:
        aftur = "ja"
        while aftur == "ja":
            kt= input("Sláðu inn kennitölu:")
            if len(kt)==10:
                dagur = int(kt[0:2])
                man= int(kt[2:4])
                ar= int(kt[4:6])
                if dagur > 0 and dagur < 32:
                    if man > 0 and man <13:
                        if ar >19 and ar <30:
                            print("rangt ár")
                        else:
                            print("rétt kennitala")
                            aftur = "nei"
                    else:
                        print("mán rangur")
                else:
                 print("dagsetningin er röng")
            else:
                print("lengdin er ekki rétt, gerðu aftur.")
        aftur = "Gerðu aftur"
    elif val==2:
        texti = input("Sláðu inn orð:")
        fyrri = texti[0:2]
        seinni = texti[-2:]
        saman = (fyrri + seinni)
        print("nýja orðið er", saman)
        saman = saman.lower()
        print(saman)
        saman = saman.upper()
        print(saman)
    elif val==3:
        nafn = input("Sláðu inn nafn:")
        for x in range(len(nafn)):
            print(nafn[x:])

    elif val==4:
        on=False