def ilkAltiAyKar(yazilimGelir1,finansmanGelir1,urunGelir1,maaslar1,kira1,donanim1):
    global kar1
    kar1=(yazilimGelir1+finansmanGelir1+urunGelir1)-(maaslar1+kira1+donanim1)
    return kar1

def sonAltiAyKar(yazilimGelir2,finansmanGelir2,urunGelir2,maaslar2,kira2,donanim2):
    global kar2
    kar2=(yazilimGelir2+finansmanGelir2+urunGelir2)-(maaslar2+kira2+donanim2)
    return kar2

def karFark(kar1,kar2):
    fark=kar2-kar1
    if fark>5000:
        print(fark,"TL İLE İŞLETME KARI ÇOKTUR")
    elif fark<1000:
        print(fark,"TL İLE İŞLETME KARI DÜŞÜK")
    else:
        print(fark,"TL İLE İŞLETME KARI NORMAL")
        
print("***İLK 6 AY*** ")
print("GELİRLER")
yazilimGelir1=int(input("Yazılım gelirini giriniz="))
finansmanGelir1=int(input("Finansman gelirini giriniz="))
urunGelir1=int(input("Urun gelirini giriniz="))
print("GİDERLER")
maaslar1=int(input("Maaşlar giderini giriniz="))
kira1=int(input("Kira giderini giriniz="))
donanim1=int(input("Donanım Giderini giriniz="))

print("***SON 6 AY***")
print("GELİRLER")
yazilimGelir2=int(input("Yazılım gelirini giriniz="))
finansmanGelir2=int(input("Finansman gelirini giriniz="))
urunGelir2=int(input("Urun gelirini giriniz="))
print("GİDERLER")
maaslar2=int(input("Maaşlar giderini giriniz="))
kira2=int(input("Kira giderini giriniz="))
donanim2=int(input("Donanım Giderini giriniz="))

sonuc1=ilkAltiAyKar(yazilimGelir1,finansmanGelir1,urunGelir1,maaslar1,kira1,donanim1)
sonuc2=sonAltiAyKar(yazilimGelir2,finansmanGelir2,urunGelir2,maaslar2,kira2,donanim2)
sonuc3=karFark(kar1,kar2)

