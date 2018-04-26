def eo2 (bs2,ys2,ps2,iss2,ts2):
    global etkilesimO2
    etkilesimO2=(((bs2+ ys2 + ps2)/iss2)/ts2) * 100
    return etkilesimO2


print("YBS2 İÇİN:")
bs2=float(input("BEĞENİ SAYISI:"))
ys2=float(input("YORUM SAYISI:"))
ps2=float(input("PAYLAŞIM SAYISI:"))
iss2=float(input("İÇERİK SAYISI:"))
ts2=float(input("TAKİPÇİ SAYISI:"))


eo2(bs2,ys2,ps2,iss2,ts2)



