import turtle
t=turtle
#Lárus Ármann Kjartansson
#08.10.119
#skilaverkefni4 For lykkja

on = True
while on == True: # valmynd
    print("1. 20 línur")
    print("2. 10 línur stækkandi")
    print("3. 10 hringir")
    print("4. 15 hringir")
    print("5. eigið mynstur")
    print("6. Hætta")
    val=int(input("Veldu hvað þú villt gera"))

    if val==1:
        t.shape("turtle") #formið á hlutinum sem teiknar línuna
        t.color("red") #litur línunar
        t.speed(5) #hraðinn
        for i in range(20): #hversu oft á að keyra lykkjuna
            t.width(5) #breidd línu
            t.forward(10) #línan fer áfram um 10
            t.up() #lyftir pennanum
            t.right(180) #snýr við í halfhring
            t.forward(10) #áfram 10
            t.left(90) #snýr í 1/4 hring
            t.forward(10) #áfram 10
            t.left(90) #snýr 1/4 hring
            t.down() #setur pennan aftur niður
    elif val==2:
        t.shape("turtle")
        t.color("blue")
        t.speed(5)
        for i in range(10,210,20): #hækkar um 20 í einu frá 10 upp í 210 sem gerir að það bætist alltaf við auka lengd á
            t.width(5)
            t.forward(i)
            t.right(180)
            t.fd(i)
            t.up()
            t.left(90)
            t.fd(10)
            t.left(90)
            t.down()

    elif val==3:
        t.shape("turtle")
        t.color("green")
        t.speed(5)
        for i in range(10,100,10): #lykkja sem stækkar radiusin um 10 i hvert skipti sem nýr hringur er gerður
            t.circle(i)

    elif val==4:
        t.shape("turtle")
        t.color("red")
        t.speed(5)
        for i in range(5, 150, 10): #teiknar hringi sem byrjar á 5 í radius og svo bætist 10 á í hvert skipti 15 sinnum
            t.right(90)
            t.forward(i)
            t.right(270)
            t.down()
            t.circle(i)
            t.up()
            t.home()


    elif val==5:
        t.shape("turtle")
        t.color("purple")
        t.speed(5)
        for i in range(5,150,2): #veit ekki nakvæmlega hvað þetta gerir þetta leit bara agætlega út.
            t.circle(i)
            t.up()
            t.right(90)
            t.forward(10)
            t.down()
    elif val==6:
        on=False#slekkur á lykkjuni



















turtle.mainloop()