satisM=500
fiyat=20
ciro=5000
i=1
while True:
    satisM=satisM+200
    fiyat=fiyat+20
    ciro=satisM*fiyat
    i=i+1
    if(ciro>500000):
        print(i,"ay sonra cironuz",ciro)
        break
