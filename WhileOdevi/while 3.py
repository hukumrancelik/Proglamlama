giris=""
toplam=0
while True:
    giris=int(input("Sayınızı giriniz:"))
    kalan=giris%3
    toplam=toplam+kalan
    print(giris,"sayısının 3'e bölümünden kalan:",kalan)
    print("Kalanların toplamı:",toplam)
    if(giris==0):
        print("0 a bastınız program durdu")
        break

