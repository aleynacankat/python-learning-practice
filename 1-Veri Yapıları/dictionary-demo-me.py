# 1- 3 ürün bilgisini (id,ad,fiyat) kullanıcısından aldığınız dictionary içinde saklayınız.
# 2- Ürün id bilgisini kullanıcından alıp ilgili ürün bilgini gösterin
"""
Urun = {
    dict("Urun 1"): {
        "id": 1587,
        "ad": "Süt",
        "fiyat":"2.5 TL"
    },
    dict("Urun 2"): {
        "id": 1684,
        "ad": "Elma",
        "fiyat": "4 TL"
    },
    dict("Urun 3"): {
        "id": 1989,
        "ad": "Çilek",
        "fiyat": "10 TL"
    },
}
sonuc = Urun[0][0]
print(sonuc)

"""
"""
urunler = {}

id = input("id: ")
ad = input("ad: ")
fiyat = input("fiyat: ")

urunler[id] = {
    "ad": ad,
    "fiyat":fiyat
}

print(urunler)
"""




