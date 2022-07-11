# key - value 

# 41 => Kocaeli
# 34 => Istanbul
"""
sehirler = ["kocaeli","İstanbul"]
plakalar = [41,34]
print(plakalar[0],sehirler[0])

print(plakalar[sehirler.index("İstanbul")])


plakalar = {"kocaeli":41,"istanbul":34}
print(plakalar["kocaeli"])
print(plakalar["istanbul"])

plakalar["rize"] = 53
print(plakalar)

"""

ogrenciler = {
    100: {
        "ad": "Çınar",
        "soyad": "Turan",
        "yas": 4,
        "notlar": [70,80,70]
    },
    101: {
        "ad": "Ada",
        "soyad": "Bilgi",
        "yas": 10
    }
}
    
sonuc = ogrenciler[100]["notlar"][0]

print(type(ogrenciler[100]))

