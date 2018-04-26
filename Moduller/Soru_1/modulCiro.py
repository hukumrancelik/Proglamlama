def kar (gelir,gider):
    global isletmeKar
    isletmeKar=gelir-gider
    return isletmeKar
    
def ciro (tc,tcs):
    global adamCiro
    adamCiro=tc/tcs
    return adamCiro
    
gelir=int(input("Geliri Giriniz:"))
gider=int(input("Gideri Giriniz:"))
tc=int(input("Toplam Ciro:"))
tcs=int(input("Toplam Çalışan Sayısı:"))

kar (gelir,gider)
ciro (tc,tcs)
