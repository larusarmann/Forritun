#Lárus Ármann Kjartansson
#05.09.2019

#liður 1
#hér tek ég 3 tölur frá notenda
tala1= int(input("sláðu inn tölu 1"))
tala2= int(input("sláðu inn tölu 2"))
tala3= int(input("sláðu inn tölu 3"))
if tala1 == tala2 or tala1==tala3 or tala2 == tala3:
    print("þú mátt ekki slá inn sömu töluna tvisvar")
#hér velur forritið hvaða tala er í miðjunni
else:
    if tala1> tala2 and tala1<tala3:
        print("tala 1:", tala1, "er í miðjunni")
    elif tala1 < tala2 and tala1 > tala3:
        print("tala 1:", tala1,"er í miðjunni")
    elif tala2<tala1 and tala2 > tala3:
        print("tala 2:", tala2, "er í miðjunni")
    elif tala2>tala1 and tala2<tala3:
        print("tala 2 :", tala2, "er í miðjunni")
    else:
        print("tala 3:", tala3, "er í miðjunni")

#liður 2
#hér spyr forritið hvort notendi vilji gefa upp lengd í cm eða tommum
svar= int(input("hvort viltu breyta cm í tommur (1) eða tommur í cm (2) "))
#núna reiknar forritið út lengdina
if svar ==1:
    sentim = float(input("hversu marga sentimetra ertu með?"))
    utkoma= sentim / 2.54
    print(sentim, "sentimetrar eru", utkoma, "tommur")
elif svar == 2:
    tomm= float(input("hversu margar tommur ertu með?"))
    utkoma2= tomm*2.54
    print(tomm, "tommur eru", utkoma2, "sentimetrar")
else:
    print("þú hefur valið rangt")


#liður 3
#hér slær notandi inn númer mánuð
man=int(input("sláðu inn númer mánaðar"))
#hér velur forritið hvað það á að prenta út
if man==1 or man==2 or man==3:
    print("nú er daginn tekið að lengja.")
elif man==4 or man==5:
    print("vorið er komið og grundirnar gróa.")
elif man==6 or man==7 or man==8:
    print("núna er sumarið komið með blóm í haga.")
elif man==9 or man==10:
    print("núna er haustið gengið í garð.")
elif man==11 or man==12:
    print("núna styttist í jólin")
else:
    print("rangur innsláttur")

#liður 4
#hér tekur forritið við nafni og kyns notenda
nafn=input("hvað heitir þú?")
kvkk=input("hvort ert þú karl(kk)eða kona(kv)")

talan1= int(input("sláðu inn tölu"))
talan2= int(input("sláðu inn tölu"))

if kvkk == "kk":
    print("blessaður", nafn)
elif kvkk =="kv":
    print("blessuð", nafn)
else:
    print("blessaður eða blessuð ég veit ekki hvors kyns þú ert",nafn)
#hér velur forritið hvor talan er stærri
if talan1 < talan2:
    print("tala 2 er stærri")
elif talan2 < talan1:
    print("tala 1 er stærri")
else:
    print("tölurnar eru jafn stórar")

mismunur=tala1-tala2
#hér finnur forritið hvort það sé meira eða minna en 100 á milli talnana
if mismunur > 100:
    print("mismunur er stærri en 100")
else:
    print("mismunur er minni en 100")

#liður 5
#hér tekur forritið við tölu sem er lægri enn 0 og stærri en 10
tala= int(input("sláðu inn tölu sem er minni en 0 eða stærri en 10"))
if tala <0 or tala >10:
    print("vel gert")
else:
    print("Þessi tala er ekki lægri en núll eða hærri en 10")
