haftalikMesai=""
while True:
    haftalikMesai=float(input("Haftalik Mesai Saatini Giriniz:"))
    ekMesai=((90*0.10)*50*30)
    toplamMaas=(50*90*30)+(haftalikMesai*ekMesai)#normal maaş+#mesai
    print("Ek mesai için ödenecek aylık ücret:",ekMesai,"TL")
    print("Personele ödenecek mesaili toplam aylık maaş:",toplamMaas,"TL")
    if(haftalikMesai>22/4):
        print("Aylık Maksimum Mesai Saati 22'dir")
        break
