#Lárus Ármann Kjartansson

#liður 1 MinnstaTalan

tala1= int(input("sláðu inn fyrri töluna "))
tala2= int(input("sláðu inn seinni töluna "))

if tala2 > tala1:
    print("talan", tala1, "er minni")
elif tala1 > tala2:
    print("talan", tala2, "er minni")
else:
    print ("Tölurnar eru jafnstórar")

#liður NumerManada

strengur1= str(input("sláðu inn mánuð "))

if strengur1 == "janúar":
    print(1)
elif strengur1 == "febrúar":
    print(2)
elif strengur1 == "mars":
    print(3)
elif strengur1 == "apríl":
    print(4)
elif strengur1 == "maí":
    print(5)
elif strengur1 == "júní":
    print(6)
elif strengur1 == "júlí":
    print(7)
elif strengur1 == "ágúst":
    print(8)
elif strengur1 == "september":
    print(9)
elif strengur1 == "október":
    print(10)
elif strengur1 == "nóvember":
    print(11)
elif strengur1 == "desember":
    print(12)
else:
    print("þetta er ekki mánuður")

#liður 3 Aldur

aldur= int(input("sláðu inn aldur"))
if aldur < 7 and aldur >= 0:
    print("Nú, svo þú ferð að byrja í skóla")
elif aldur >=7 and aldur <=15:
    menntaskoli= str(input("ætlar þú í menntaskóla?"))
    if "j"== menntaskoli:
        print("Til Hamingju!")
    elif "n":
        print("Afhverju Ekki")
    else:
        print("lárus")
elif aldur >=16 and aldur <=105:
    print("Gangi þér vel í framtíðinni")
else:
    print("þú hefur svarað spurningunni vitlaust.")

#4. MargfaldaFasta
tala= int(input("sláðu inn tölu á milli 0 og 25"))
if tala >= 0 and tala <= 25:
    print(tala*1.7)
else:
    print("Rangur innsláttur")

#liður 5 Brandari

brandari= input("viltu heyra brandara?")
if  brandari == "já":
    print("Afhverju fara hafnfirðingar alltaf með stiga útí búð? (því verðið er svo hátt)")
else:
    print("Allt í lagi, kannski seinna")









