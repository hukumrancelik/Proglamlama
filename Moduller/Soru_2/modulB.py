#aktifler
def donenV (kasa,alinanCekler,bankaH,alicakS,ticariM):
    global donenVarliklar
    donenVarliklar=(kasa+alinanCekler+bankaH+alicakS+ticariM)
    return donenVarliklar
    
def duranV (binalarH,tasitlarH,demirbasH):
    global duranVarliklar
    duranVarliklar=(binalarH+tasitlarH+demirbasH)
    return duranVarliklar

def aktif(donenVarliklar,duranVarliklar):
    global aktifToplam
    aktifToplam=donenVarliklar+duranVarliklar
    return aktifToplam

#pasifler
def kvyk (bankaK,saticiH):
    global kisaV
    kisaV=(bankaK+saticiH)
    return kisaV

def uvyk (ubankaK,borcSenet):
    global uzunV
    uzunV=(ubankaK+borcSenet)
    return uzunV
    
def ok (sermayeH):
    global ozKaynak
    ozKaynak=(sermayeH)
    return  ozKaynak
    
def pasif(kisaV,uzunV,ozKaynak):
    global pasifToplam
    pasifToplam=(kisaV+uzunV+ozKaynak)
    return pasifToplam


print("DÖNEN VARLIKLAR")  
kasa=int(input("KASA HESABI:"))
alinanCekler=int(input("ALINAN ÇEKLER:"))
bankaH=int(input("BANKALAR HESABI"))
alicakS=int(input("ALICAK SENETLERİ"))
ticariM=int(input("TİCARİ MALLAR"))

print("-"*20)


print("DURAN VARLIKLAR")  
binalarH=int(input("BİNALAR HESABI:"))
tasitlarH=int(input("TAŞITLAR HESABI:"))
demirbasH=int(input("DEMİRBAŞLAR HESABI"))

print("-"*20)

print("KISA VADELİ YABANCI KAYNAKLAR")  
bankaK=int(input("BANKA KREDİLERİ HESABI:"))
saticiH=int(input("SATICILAR:"))

print("-"*20)

print("UZUN VADELİ YABANCI KAYNAKLAR")  
ubankaK=int(input(" UZUN VADELİ BANKA KREDİLERİ HESABI:"))
borcSenet=int(input("BORÇ SENETLERİ HESABI:"))
sermayeH=int(input("SERMAYE HESABI:"))

print("-"*20)



donenV(kasa,alinanCekler,bankaH,alicakS,ticariM)
duranV (binalarH,tasitlarH,demirbasH)
aktif(donenVarliklar,duranVarliklar)
kvyk (bankaK,saticiH)
uvyk (ubankaK,borcSenet)
ok (sermayeH)
pasif(kisaV,uzunV,ozKaynak)

if(aktifToplam==pasifToplam):
    print("-"*20)
    print("***Kapanış Bilançosu Doğru Hesaplanmıştır***")
else:
    print("-"*20)
    print("!!!Kapanış Bilançosu Yanlış Hesaplanmıştır*!!!")




