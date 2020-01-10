#Lárus Ármann Kjartansson
#19.09.19

#liður 1
tala=3
gisk=0
while gisk != tala:

    gisk = int(input("gískaðu á rétta tölu"))
if gisk ==tala:
    print("þú fannst rétta tölu")
else:
    print("þetta er ekki rétt tala")

#liður 2
teljari=0
while teljari <11:
    if teljari != 3:
        print(teljari)
    teljari = teljari+1