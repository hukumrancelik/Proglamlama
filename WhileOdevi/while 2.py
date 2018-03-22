satisM=500
fiyat=20
ciro=5000
i=0
while True:
    ciro=(ciro)+satisM*fiyat
    satisM=satisM+200
    fiyat=fiyat+10
    i=i+1
    if(ciro>500000):
        print(i,"ay sonra cironuz",ciro)
        break
