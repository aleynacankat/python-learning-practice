"""
sayilar = [1,2,3,6,8,9]
isimler = ["ali", "deniz","yagmur"]
isim  = "Sadik Turan"

for i in sayilar:
    print(i)

for i in sayilar:
    print(isim)

_tuple = [(1,2),(4,5),(6,7)]

for a,b in _tuple:
    print(a,b)
"""
"""
_dict = {"k1":1,"k2":2,"k3":3}

for x in _dict:
    print(x)

for x in _dict:
    print(_dict[x])

for x in _dict.values():
    print(x)

for x in _dict.values():
    print(x)

for key,value in _dict.items():
    print(key,value)
"""

urunler = [
    {'name':"iphone 8 ", 'price':"4000"},
    {'name':"iphone 8 Plus",'price':"5000"},
    {'name':"iphone X",'price':"6000"},
    {'name':"iphone XR",'price':"7000"},
    {'name':"iphone 11",'price':"8000"},
    {'name':"iphone s10",'price':"6000"},
]

#1-Tüm ürün bilgilerini listeleyiniz.
"""
for urun in urunler:
    print(f"urun adi: {urun['name']} ve urun fiyati: {urun['price']} TL")
"""

#2-Urunlerin fiyatlari toplami nedir?

toplam = 0
for urun in urunler:
    toplam = toplam + int(urun('price'))
print(f'urun toplamlari: , {toplam} TL')