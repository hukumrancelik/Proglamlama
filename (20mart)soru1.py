def katmaDeger(toplamSatis,hammadde,bakim,sevkiyat,satinAlinan):
    global ciroHesap
    ciroHesap=toplamSatis-(hammadde+bakim+sevkiyat+satinAlinan)
    if ciroHesap>1000:
        print(ciroHesap,"TL ile işletme Katma Değer Cirosu Yüksek")
    elif ciroHesap<500:
        print(ciroHesap,"TL ile işletme Katma Değer Cirosu Düşük")
    else:
        print(ciroHesap,"TL ile işletme Katma Değer Cirosu Normal")

toplamSatis=int(input("Toplam Satış Değerini Giriniz:"))
hammadde=int(input("Hammadde Değerini Giriniz:"))
bakim=int(input("Bakim onarim giderlerini giriniz:"))
sevkiyat=int(input("Sevkiyat giderlerini giriniz:"))
satinAlinan=int(input("Satin alınma hizmet giderlerini giriniz:"))
ciroSonuc=katmaDeger(toplamSatis,hammadde,bakim,sevkiyat,satinAlinan)
        
