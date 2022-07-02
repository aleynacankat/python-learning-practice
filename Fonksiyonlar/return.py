def toplam():
    return 10+20

sonuc = toplam() + 50

# print(sonuc)
def yil():
    import datetime
    return datetime.datetime.now().year
#return yapmamın amacı o fonksiyonu cagirdigimda calismasi

def yasHesapla():
    return yil() - 1983

sonuc = yasHesapla()

def saat():
    import datetime
    return datetime.datetime.now().hour

def selamla():
    if (saat()<12):
        return "Günaydın"
    else:
        return "Merhaba"

sonuc = selamla() + "Sadik"

print(sonuc)
