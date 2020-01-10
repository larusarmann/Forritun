#Lárus Ármann Kjartansson
#03.09.19
#heiltöludeiling

#liður 1:

gradur= int(input("sláðu inn gráðu",))
hringur=gradur//360
afggradur = gradur%360
if hringur <= 1:
    print("þetta er", hringur, "hringur og", afggradur,"gráður")
else:
    print("þetta eru", hringur, "hringir og", afggradur,"gráður")

#Liður 2:

mæting=int(input("hvað eru margir mættir á æfingu?"))
lið= int(input("hvað eiga að vera margir í liði?"))
lið2=mæting//lið
afglið=mæting%lið
print("Þetta verða þá" ,lið2, "lið og", afglið, "varamenn")

#liður 3:

sekundur=int(input("sláðu inn fjölda sekúnda"))
klst=sekundur//3600
afgklst=sekundur%3600
min=afgklst//60
sekundur=afgklst%60

print("það eru",klst, "klst,", min , "min,og" , sekundur, "sek")

#liður 4
mm=int(input("sláðu inn fjölda millimetra"))
metrar=mm//1000
afgmetri=mm%1000
cm=afgmetri//10
millim=afgmetri%10
print("það eru",metrar,"metrar",cm,"sentímetrar", "og",millim, "millimetrar")

#liður 5
peningur=int(input("Hvað ertu með margar krónur"))
tusund=peningur//1000
afgtusund=peningur%1000
fimhund=afgtusund//500
afgfimmh=afgtusund%500
hundr=afgfimmh//100
afghundr=afgfimmh%100
print("Þetta gerir", tusund, "stk 1000kr seðla",fimhund,"stk 500kr seðla",hundr, "stk 100kr peninga og",afghundr, "krónur")

#liður 6

tala=int(input("sláðu inn tölu"))
if tala%2 ==0:
    print("þetta er slétt tala")
else:
    print("þetta er oddatala")