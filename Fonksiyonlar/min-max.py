
sayilar = [1,5,7,45,25,89]
harfler = ['a','v','h','s']
isimler = ['aleyna','cankat','kaan','ozgul','sadik']

sonuc = min(sayilar)
sonuc = max(sayilar)
sonuc = min(harfler)
sonuc = max(harfler)

sonuc = max(isimler)

sonuc = min(len(isim) for isim in isimler)
sonuc = max([len(isim) for isim in isimler])

sonuc = max(isimler, key=lambda n: len(n))
sonuc = min(isimler, key=lambda n: len(n))

print(sonuc)

urunler = [
    {"title":"iphone x", "price": 5000},
    {"title":"iphone xr", "price": 6000},
    {"title":"iphone 11", "price": 7000},
]

sonuc = max(urunler, key = lambda urun: urun['price'])['title']
print(sonuc)
sonuc = min(urunler, key=lambda urun: urun['price'])

max = 0 

for urun in urunler:
    if urun["price"]>max:
        max = urun["price"]

print(urun)


