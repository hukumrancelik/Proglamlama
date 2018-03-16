def donemBasiStok(koltuk1,yatak1,dolap1):
    global donemBasi
    donemBasi=koltuk1+yatak1+dolap1
  
def donemSonuStok(koltuk2,yatak2,dolap2):
    global donemSonu
    donemSonu=koltuk2+yatak2+dolap2
  
def stokOrtalama(donemBasi,donemSonu):
    global ortalama
    ortalama=(donemBasi+donemSonu)/2

print("DÖNEM BAŞI STOK")
koltuk1=int(input("Koltuk Adetini Giriniz:"))
yatak1=int(input("Yatak Adetini Giriniz:"))
dolap1=int(input("Dolap Adetini Giriniz:"))

print("DÖNEM SONU STOK")
koltuk2=int(input("Koltuk Adetini Giriniz:"))
yatak2=int(input("Yatak Adetini Giriniz:"))
dolap2=int(input("Dolap Adetini Giriniz:"))

sonuc1=donemBasiStok(koltuk1,yatak1,dolap1)
sonuc2=donemSonuStok(koltuk2,yatak2,dolap2)
sonuc3=stokOrtalama(donemBasi,donemSonu)
print("ORTALAMA STOK DEĞERİNİZ",ortalama)
