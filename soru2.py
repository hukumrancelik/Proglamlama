def ekipmanKullan( planUretimSur, plansizUretimSur):
    global kullanabilirlik
    kullanabilirlik=(planUretimSur-plansizUretimSur)/planUretimSur
    return kullanabilirlik

def performansOrani( standCevSur,uretimMik,):
    performans=(standCevSur*uretimMik)/(planUretimSur-plansizUretimSur)
    return performans
    
def kaliteHesap(saglamUrun,toplamUrun):
    global kalite
    kalite=saglamUrun/toplamUrun
    return kalite
    
def etkinlik(kullanabilirlik,performans,kalite):
    oee=kullanabilirlik*performans*kalite*100

    if(oee>75):
        print("Verimlilik İyidir")
    elif(50<oee<75):
        print("Verimlilik Normal")
    else:
        print("Verimlilik Kötü")

planUretimSur=int(input("Planlamış Üretim Süresini Giriniz:"))
plansizUretimSur=int(input("Plansız Üretim Süresini Giriniz:"))

standCevSur=int(input("Standart Cevrim Süresini Giriniz:"))
uretimMik=int(input("Üretim Miktarını Giriniz:"))

saglamUrun=int(input("Sağlam Urun Miktarını Giriniz:"))
toplamUrun=int(input("Toplam ürün Miktarını Giriniz:"))

k=ekipmanKullan( planUretimSur, plansizUretimSur)
p=performansOrani( standCevSur,uretimMik,)
etkinlik(kullanabilirlik,performans,kalite)


