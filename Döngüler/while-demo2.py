#kullanicidan alacaginiz sinirsiz urun bilgisini urunler 
#listesi icinde saklayiniz.
#urun sayisini kullaniciya sorun.
# dictionary listesi yapisi (urunAdi, fiyat) seklinde olsun
# urun ekleme islemi bittiginde urunleri ekranda while ile listeleyin.


i = 0
adet = int(input('kac adet urun eklemek istiyorsunuz: '))

urunler = []

while(i < adet):
    urunAdi = input("urun adini giriniz: ")
    fiyat = input("urun fiyati: ")
    urunler.append({
        'urunAdi': urunAdi,
        'fiyat': fiyat
    })
    i += 1
"""
for urun in urunler:
    print(f"urun adi: {urun['urunAdi']} urun fiyati {urun['fiyat']}" )
"""
i = 0
adet = int(input('kac adet urun eklemek istiyorsunuz: '))

urunler = []
a = 0
while (a < len(urunler)):
    print(f"urun adi: {urun['urunAdi']} urun fiyati {urun['fiyat']}" )
    a += 1
