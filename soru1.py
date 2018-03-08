def gelirHesapla(finansGelir,pazarGelir,kiraGelir):
    global toplamGelir
    toplamGelir=finansGelir+pazarGelir+kiraGelir
    return toplamGelir

def giderHesapla(ucret,finansGider,pazarGider,kiraGider,muhasebeGider):
    global toplamGider
    toplamGider=ucret+finansGider+pazarGider+kiraGider+muhasebeGider
    return toplamGider
def karHesapla(toplamGelir,toplamGider):
    kar=toplamGelir-toplamGider
    if (kar>1000):
        print(kar,"TL İLE İŞLETME KAR NOKTASINDADIR")
    elif kar<1000:
        print(kar,"TL İLE İŞLETME ZARARDADIR")
    else:
        print(kar,"İŞLETMENİNİZ BAŞABAŞ NOKTASINDADIR")

print("***GELİRLER***")
finansGelir=int(input("Finansman Gelirlerini Giriniz:"))
pazarGelir=int(input("Pazar Gelirlerini Giriniz:"))
kiraGelir=int(input("Finansman Gelirlerini Giriniz:"))

print("***GİDERLER***")
ucret=int(input("Ücret Gelirlerini Giriniz:"))
finansGider=int(input("Finansman Giderlerini Giriniz:"))
pazarGider=int(input("Pazar Giderlerini Giriniz:"))
kiraGider=int(input("Kira Giderlerini Giriniz:"))
muhasebeGider=int(input("Muhasebe Giderlerini Giriniz:"))

gelirim=gelirHesapla(finansGelir,pazarGelir,kiraGelir)
giderim=giderHesapla(ucret,finansGider,pazarGider,kiraGider,muhasebeGider)
kar=karHesapla(gelirim,giderim)







