#Lárus Ármann Kjartansson
#24.09.19
#Skilaverkefni 3

#Liður 1
#þetta forrit biður um tölur þangað til að notandinn skrifar eithvað annað en já
answer="já"
while answer=="já":
    tala = int(input("Sláðu inn tölu"))
    print("þú hefur valið töluna", tala)
    answer = str(input("viltu slá inn aðra tölu?"))

#Liður 2
#forritið tekur inn 3 tölur og reiknar flatarmál þeirra,
#forritið spyr svo hvort notandinn vilji halda áfram,
#ef svarað er já heldur forritið áfram, ef svarað er eithvað annað hættir forritið
svar="já"
while svar =="já":
    lngd=int(input("sláðu inn lengd"))
    breid=int(input("sláðu inn breidd"))
    flat=lngd*breid
    print(flat)
    svar=str(input("viltu halda áfram?"))

#Liður 3
#í þessu forriti tekur forritið við lykilorði frá notenda,
#ef svarað er rétt klárast forritið
#ef svarað er vitlaust heldur það áfram þangað til rétt lykilorð er slegið
passw=""
while passw != "tskoli2019":
    passw = str(input("sláðu inn passorð"))

print("þú hefur valið rétt passorð")

#Liður 4
#í þessu forriti skrifar notendi inn kr og forrititið skrifar út
#hversu marga 5000,1000,500 osfv. og skrifar töluna bara ef það er meira en 1 af tölunni
#ef það eru t.d. núll 1000 kr í dæminu þá sleppir forritið að prenta þá tölu
kr = int(input("Sláðu inn kr"))
fj5000=0
fj1000=0
fj500=0
fj100=0
fj50=0
fj10=0
fj5=0
fj1=0
while kr > 0:
    if kr - 5000 >= 0:
        fj5000 = fj5000 +1
        kr = kr -5000
    elif kr - 1000 >= 0:
        fj1000 = fj1000 +1
        kr = kr -1000
    elif kr - 500 >= 0:
        fj500 = fj500 +1
        kr = kr -500
    elif kr - 100 >= 0:
        fj100 = fj100 +1
        kr = kr -100
    elif kr - 50 >= 0:
        fj50 = fj50 +1
        kr = kr -50
    elif kr - 10 >= 0:
        fj10 = fj10 +1
        kr = kr -10
    elif kr - 5 >= 0:
        fj5 = fj5 +1
        kr = kr -5
    elif kr - 1 >= 0:
        fj1 = fj1 +1
        kr = kr -1

if fj5000 >0:
    print(fj5000,"stk 5000kr")
if fj1000 >0:
    print(fj1000, "stk 1000kr")
if fj500 >0:
    print(fj500, "stk 500kr")
if fj100 >0:
    print(fj100, "stk 100kr")
if fj50 >0:
    print(fj50, "stk 50kr")
if fj10 >0:
    print(fj10, "stk 10kr")
if fj5 >0:
    print(fj5, "stk 5kr")
if fj1 >0:
    print(fj1, "krónur")

#Liður 5
#þetta forrit gefur þér 3 valmöguleika, ef þú velur 1
#þá finnur forritið summu og meðaltal 10 talna
#ef þú velur 2 þá segir forritið hvort talan sé slétt eða oddatala
#ef þú velur 3 þá hættir forritið og skrifar hversu oft forritið var keyrt
#og skrifar út "ég er frábær forritari" 10 sinnum
keyrslutelj=0
ok = True
while ok ==True:
    print("1. tölur, meðaltal og summa")
    print("2. Jöfn tala eða oddtala")
    print("3. Hæetta")
    val = int(input("veldu hvað þú vilt gera"))
    if val ==1:
        keyrslutelj=keyrslutelj+1
        teljari=1
        summa=0
        while teljari <11:
            tal =int(input("sláðu inn tölu"))
            summa= summa+tal
            teljari=teljari + 1
            medaltal = summa / 10
        print("samanlagt er þetta",summa,"og meðaltalið er",medaltal)

    elif val ==2:
        keyrslutelj=keyrslutelj+1
        talaa = int(input("sláðu inn tölu"))
        if talaa % 2 == 0:
            print("þetta er slétt tala")
        else:
            print("þetta er oddatala")
    elif val ==3:
        ok = False
        print("ég er frábær forritari")
        print("ég er frábær forritari")
        print("ég er frábær forritari")
        print("ég er frábær forritari")
        print("ég er frábær forritari")
        print("ég er frábær forritari")
        print("ég er frábær forritari")
        print("ég er frábær forritari")
        print("ég er frábær forritari")
        print("ég er frábær forritari")
        print("þú keyrðir forritið",keyrslutelj,"sinnum")
    else:
        print("þú valdir rangt")

#liður F
#þetta er teljari, han heldur áfram þangað til að teljarinn kemst upp í 10 þá hættir forritið. printið skrifar svo út teljaran á meðan hann telur.

#þetta er eins nema það að teljarinn mun aldrei stoppa, teljarinn mun aldrei verða 10 sem þýðir að teljarinn mun ganga að eylífu.
