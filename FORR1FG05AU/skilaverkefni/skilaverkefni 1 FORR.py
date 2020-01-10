#Lárus Ármann Kjartansson
#29.08.2019

#Liður 1:

#hér bið ég um nafn notenda
nafn= input("hvað heitir þú?")
#núna bið ég um uppáhalds áfanga notenda
uafangi= input("hvað er uppáhaldsfagið þitt?")
#hérna fæ ég forritið til að skrifa velkomin í áfangann
print("Velkomin í áfangann", uafangi)
#hér prenta ég að það verði skemmtileg önn, nafn notenda
print("þetta verður skemmtileg önn hjá okkur", nafn)

#Liður 2:

#hér bið ég um tölu sem er hærri en 100
tala100= int(input("veldu tölu sem er hærri en 100"))
#hérna reiknar forritið út töluna deilt í 5,5
taladeila=tala100/5.5
#hérna prentar forritið töluna með 2 aukastöfum
print(format(taladeila, ".2f"))

#Liður 3:

#hér bið ég um fyrri töluna
tala1= int(input("skrifaðu inn tölu 1"))
#hér bið ég um seinni töluna
tala2= int(input("skrifaðu inn tölu 2"))
#hér margfalda ég tölurnar tvær
margf= tala1*tala2
#hér prenta ég út svar tveggja talnana
print("margfaldað saman verður svarið=",margf)
#hér dregur forritið fyrri töluna frá seinni tölunni
minus= tala2-tala1
#hér skrifar forritið töluna út+
print("fyrri talan dregin frá seinni tölunni=", minus)

#Liður 4:

#hér fæ ég hæð kassans frá notenda
haed= int(input("skrifaðu hæð kassa"))
#hér fæ ég lengd kassans
leng= int(input("skrifaðu lengd kassans"))
#hér fæ ég breidd kassans
breid= int(input("skrifaðu breidd kassans"))
#hér reiknar forritið út rúmmál
rummal=haed*leng*breid
#hér prenta ég út rúmmálið
print("rúmmál kassans er", rummal)

#Liður 5:

#hér fæ ég aldur notenda og pabba þeirra
barn=int(input("hvað ert þú gamall/gömul?"))
pabbi=int(input("hvað er pabbi þinn gamall?"))
#hér dreg ég frá aldur barnsins frá aldri pabbans
faeddist= pabbi-barn
#hér prenta ég út aldur pabba þegar notendi fæddist
print("pabbi þinn var", faeddist, "ára þegar þú fæddist")

#Liður 6:

#hér fæ ég aldur einstaklinga
ald1með= int(input("skrifaðu inn aldur 1"))
ald2með= int(input("skrifaðu inn aldur 2"))
ald3með= int(input("skrifaðu inn aldur 3"))
#hér fæ ég summu talnanna
summa=ald1með+ald2með+ald3með
#hér verður sú tala deilt í 3
meðal=summa/3
#hér er ég að minnka aukastafina
utkoma= round(meðal, 2)
#hér prenta ég meðalaldurinn
print("meðalaldurinn er",utkoma)

print("Gaman að geta aðstoðað þig við þessa útreikninga",nafn)