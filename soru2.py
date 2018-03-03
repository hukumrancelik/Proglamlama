print("----------------------------------")
print("KULLANACAĞINIZ FONKSİYONU YAZINIZ")
print("----------------------------------")
print("EKİPMAN KULLANABİLİRLİK için:'ekipmanKullan()'")
print("PERFORMANS ORANI için:'performansOrani()'")
print("KALİTE ORANI için:'kalite()'")
print("EKİPMAN ETKİNLİK ORANI için:'etkinlik()'")

def ekipmanKullan():
    print("***EKİPMAN KULLANABİLİRLİK***")
    planUretimSur=int(input("Planlamış Üretim Süresini Giriniz:"))
    plansizUretimSur=int(input("Plansız Üretim Süresini Giriniz:"))
    kullanabilirlik=(planUretimSur-plansizUretimSur)/planUretimSur
    print("Kullanabilirlik:",kullanabilirlik)

def performansOrani():
    print("***PERFORMANS ORANI***")
    standCevSur=int(input("Standart Cevrim Süresini Giriniz:"))
    uretimMik=int(input("Üretim Miktarını Giriniz:"))
    planUretimSur=int(input("Planlamış Üretim Süresini Giriniz:"))
    plansizUretimSur=int(input("Plansız Üretim Süresini Giriniz:"))
    performans=(standCevSur*uretimMik)/(planUretimSur-plansizUretimSur)
    print("Kullanabilirlik:",performans)
    
def kalite():
    print("***KALİTE ORANI***")
    saglamUrun=int(input("Sağlam Urun Miktarını Giriniz:"))
    toplamUrun=int(input("Toplam ürün Miktarını Giriniz:"))
    kalite=saglamUrun/toplamUrun
    print("Kalite Oranı:",kalite)
   

def etkinlik():
    print("***EKİPMAN ETKİNLİK ORANI***")
    kullanabilirlik=float(input("Kullanabilirlik Oranın Giriniz:"))
    performans=float(input("Performans Oranını Giriniz:"))
    kalite=float(input("Kalite Oranını Giriniz:"))
    oee=(kullanabilirlik*performans*kalite)*100
    print("Ekipman Etkinlik Oranı",oee)
   
