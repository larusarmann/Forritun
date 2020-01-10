#Lárus Ármann Kjartansson
#17.09.19

#liður 1
nafn=input("hvað heitir þú?")
haed=float(input("hvað ert þú hávaxin í metrum?"))

haedcm=haed*100

utkoma=200-haedcm

print("góðan daginn",nafn,"þig vantar",utkoma,"sentimetra upp í að verða tveir metrar")

#liður 2
stig=int(input("hve mörg stig ertu með?"))

if stig>=1 and stig<=25:
    print("úpps þetta hefur ekki endað vel")
elif stig>=26 and stig<=50:
    print("þetta hefur gengið vel")
elif stig>=51 and stig<=80:
    print("geggjað vel gert")
elif stig<=0 or stig>=100:
    print("kjaftæði er þetta- þú þarft að vanda innsláttin")
else:
    print("rangur innsláttur")

#liður 3
tal1=int(input("sláðu inn tölu 1"))
tal2=int(input("sláðu inn tölu 2"))
tal3=int(input("sláðu inn tölu 3"))

summ=tal1+tal2
samtls=summ-tal3
print("(",tal1,"+",tal2,")-",tal3,"=",samtls)

#liður 4
buxur=int(input("hvað kosta buxurnar?"))
fimtusund=buxur//5000
afgfimtusund=buxur%5000
tusund=afgfimtusund//1000
afgtusund=afgfimtusund%1000
fimmhund=afgtusund//500
afgfimhund=afgtusund%500
hundr=afgfimhund//100
afghundr=afgfimhund%100
fimmti=afghundr//50
afgfimmtiu=afghundr%50

print("þá þarft þú",fimtusund,"fimmþúsundkr seðla",tusund,"þúsundkr seðla",fimmhund,"fimmhundruðkr seðla",hundr,"hundrað kalla",fimmti,"fimmtiu kalla","og",afgfimmtiu,"krónur")
