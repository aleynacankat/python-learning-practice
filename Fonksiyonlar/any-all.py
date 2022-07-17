

sonuc = all([True, True, False])
sonuc = all([True, True, True])
sonuc = any([True, True, False]) #herhangi bi eleman true ise bize true yu döndürür.

# And => true and True = True => All()
# Or => true or False = True => Any()

sayilar = [0,1,3,6,8,9,10]
sonuc = all([bool(sayi) for sayi in sayilar])
sonuc = any([bool(sayi for sayi in sayilar if sayi %2 == 1)])
sonuc = all([sayi %2 == 0 for sayi in sayilar])

kisiler = ["ali","ahmet","cinar"]
sonuc = all([kisi[0] == 'a' for kisi in kisiler])
sonuc = any([kisi[0] == 'a' for kisi in kisiler])
sonuc = all([kisi[0] == 'a' for kisi in kisiler if kisi[0] == 'a'])



print(sonuc)
