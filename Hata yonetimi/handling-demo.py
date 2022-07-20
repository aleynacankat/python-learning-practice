liste = ["1","2","5a","10b","abc","10","50"]

#1: Liste elemanları icindeki sayisal degerleri bulunuz.
"""
for sayi in liste:
    try:
        sonuc = int(sayi)
        print(sonuc)
    except ValueError:
        continue
"""
#2: Kullanici 'q' degerini girmedikce aldiginiz her inputun sayi oldugundan emin
#olunuz aksi halde hata mesajı yazdiriniz

"""
while True:
    sayi2 = input('sayi: ')
    if (sayi2 == 'q'):
        break
    
    try:
        sonuc2 = float(sayi2)
        print(f"girilen sayi: {sonuc2}")
        break
    except ValueError:
        print('gecersiz sayi.')
        continue
"""
#3: Dict ve key bilgilerini parametre olarak alan get(d, key) fonksiyonu hazirlayiniz.

urun = {"urunAdi": "samsung s10"}

#d["fiyat"] ==> KeyError

#get(d, "fiyat") =>
#get(d, "urunAdi") => samsung S10

def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None

print(get(urun, 'fiyat'))
print(get(urun, 'urunAdi'))


