print("***GELİRLER***")
finansGelir=int(input("Finansman Gelirlerini Giriniz:"))
pazarGelir=int(input("Pazar Gelirlerini Giriniz:"))
kiraGelir=int(input("Finansman Gelirlerini Giriniz:"))
toplamGelir=finansGelir+pazarGelir+kiraGelir

print("***GİDERLER***")
ucret=int(input("Ücret Gelirlerini Giriniz:"))
finansGider=int(input("Finansman Giderlerini Giriniz:"))
pazarGider=int(input("Pazar Giderlerini Giriniz:"))
kiraGider=int(input("Kira Giderlerini Giriniz:"))
muhasebeGider=int(input("Muhasebe Giderlerini Giriniz:"))
toplamGider=ucret+finansGider+pazarGider+kiraGider+muhasebeGider
kar=toplamGelir-toplamGider

if kar==0:
   print(kar,"TL İLE İŞLETME BAŞABAŞ NOKTASINDADIR")

elif kar<1000:
    print(kar,"TL İLE İŞLETME ZARARDADIR")
else:
    print(kar,"TL İLE İŞLETME KAR NOKTASINDADIR")
