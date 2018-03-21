gunlukUrun=200
defoluMal=""
toplamDefo=0
i=0
while True:
    print("****************************")
    defoluMal=int(input("Günlük defolu ürün sayısınız giriniz:"))
    toplamDefo=toplamDefo+defoluMal
    i=i+1
    print(i,"günlük toplam defolu ürün sayınız:",toplamDefo)
    if(defoluMal>(gunlukUrun*0.20)):
        print("Defolu ürün sayınız günlük mal üretiminizin %20'nin üzerindedir")
        break
    
