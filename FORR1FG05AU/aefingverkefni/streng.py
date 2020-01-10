#Lárus Ármann Kjartansson
#15.10.19
#Æfingaverkefni Strengir

on = True
while on == True:
    print("1.Anna Marín Jónasdóttir")
    print("2.Random tölur")
    print("3.Að telja orð")
    print("4.Afturábak")
    print("5.Hætta")
    val = int(input("Veldu hvað þú vilt gera:"))

    if val == 1:
        nafn = input("Sláðu inn nafn:")
        stafur = input("Veldu staf sem þú vilt breyta:")
        nyja = ""
        for x in nafn:
            if x == stafur:
                nyja = nyja + "*"
            else:
                nyja = nyja + x
        print(nyja)

    elif val == 2:
        usernafn = input("Sláðu inn nafnið þitt:")
        usernafn = usernafn.upper()
        print(usernafn)
        usernafn = usernafn.lower()
        print(usernafn)
        stafur = input("Veldu staf sem þú vilt breyta:")
        nyja = ""
        for x in usernafn:
            if x == stafur:
                nyja = nyja + "@"
            else:
                nyja = nyja + x
        print(nyja)

    elif val == 3:
        setning = input("Sláðu inn setningu:")
        fjBila = 0
        for x in setning:
            if x == "":
                fjBila = fjBila + 1
            print("Fjöldi orða í setningunni er", fjBila + 1)

    elif val == 4:
        setning = input("Sláðu inn setningu:")
        print(setning[::-1])

    elif val == 5:
        on = False