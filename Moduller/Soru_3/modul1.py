#aktifler
def eo1 (bs1,ys1,ps1,iss1,ts1):
    global etkilesimO1
    etkilesimO1=(((bs1+ ys1 + ps1)/iss1)/ts1) * 100
    return etkilesimO1


print("YBS1 İÇİN:")
bs1=float(input("BEĞENİ SAYISI:"))
ys1=float(input("YORUM SAYISI:"))
ps1=float(input("PAYLAŞIM SAYISI:"))
iss1=float(input("İÇERİK SAYISI:"))
ts1=float(input("TAKİPÇİ SAYISI:"))


eo1 (bs1,ys1,ps1,iss1,ts1)



