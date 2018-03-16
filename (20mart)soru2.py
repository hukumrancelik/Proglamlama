def ilkYil(calisanSure1,toplamMusteri1):
    global ilkSure
    ilkSure=calisanSure1/toplamMusteri1

def ikinciYil(calisanSure2,toplamMusteri2):
    global ikinciSure
    ikinciSure=calisanSure1/toplamMusteri2

def fark(ilkSure,ikinciSure):
    global ikiYil
    ikiYil=ilkSure-ikinciSure
    

calisanSure1=int(input("2016 yılı için Çalışılan Süre:"))
toplamMusteri1=int(input("2016 yılı için Toplam Müşteri Sayisi:"))

print("**********************************")

calisanSure2=int(input("2017 yılı için Çalışılan Süre:"))
toplamMusteri2=int(input("2017 yılı için Toplam Müşteri Sayisi:"))

sonuc1=ilkYil(calisanSure1,toplamMusteri1)
sonuc2=ikinciYil(calisanSure2,toplamMusteri2)
sonuc3=fark(ilkSure,ikinciSure)
print("İki Yıl Arasındaki Fark:",ikiYil)
