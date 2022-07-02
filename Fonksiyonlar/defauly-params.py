def selamlama(isim="Kullanici", mesaj = "İyi Gunler"):
    print(f"{mesaj} {isim}")

selamlama("Ali", "Gunaydin")
selamlama("Ali", "İyi gunler")
selamlama("Ali")
selamlama()
"""
def usAlma(taban, us):
    return taban ** us

sonuc = usAlma(2,3)
sonuc = usAlma(2,3)
sonuc = usAlma(3)
"""
def toplam(a,b):
    return a + b

def cikarma(a,b):
    return a - b

def islem(a,b,fn):
    return fn(a,b)

sonuc = islem(5,3)

print(sonuc)