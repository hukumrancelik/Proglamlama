def eo3 (bs3,ys3,ps3,iss3,ts3):
    global etkilesimO3
    etkilesimO3=(((bs3+ ys3 + ps3)/iss3)/ts3) * 100
    return etkilesimO3


print("YBS3 İÇİN:")
bs3=float(input("BEĞENİ SAYISI:"))
ys3=float(input("YORUM SAYISI:"))
ps3=float(input("PAYLAŞIM SAYISI:"))
iss3=float(input("İÇERİK SAYISI:"))
ts3=float(input("TAKİPÇİ SAYISI:"))


eo3 (bs3,ys3,ps3,iss3,ts3)


