"""
    module1 (db) : urunler
    module2 (methods) : urunEkle(), urunGuncelle(), urunleriGetir()
    module3 (app)

        yeni urun ekleme = urunEkle("iphone11 pro", 7000)
        urun guncelle = urunGuncelle(1, "iphone12 pro", 8000)
        urunleri listele = urunleriGetir()
"""




from methods import *
urunleriGetir()
print("******")
urunEkle("iphone 11 pro", 8000)
urunEkle("iphone 7s", 5000)

urunleriGetir()