
liste = [10,4,7,9,70]
sayilar = []
"""
for i in range(10):
    sayilar.append(i)

sayilar = [i for i in range(10)]
"""
# [expression for item in list]

for i in liste:
    i *= 2
    sayilar.append(i)

sayilar = [i*i for i in range(10)]
sayilar = [i*2 for i in liste]

isim = "Ahmet"
sonuc = [c.upper() for c in isim]
sonuc = [str(sayi) for sayi in liste]
isimler = ["Ahmet","Ali","Çınar","HakTan"]
sonuc = [c.upper() for c in isim]
sonuc = [str(sayi) for sayi in liste]
sonuc = [i.lower() for i in isimler]
print(sayilar)

