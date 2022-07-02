def selamla(isim):
    return "Merhaba, " + isim

sonuc = selamla("Aleyna")
sonuc = selamla("Kaan")

def toplam(a,b):
    return a + b

sonuc = toplam(10,20)
sonuc = toplam(120,240)
sonuc = toplam(20,30)

def yasHesapla(dogumYili):
    return 2021 - dogumYili

sonuc = yasHesapla(1983)


def emekliligeKacYilKaldi(dogumYili, isim):
    yas = yasHesapla(dogumYili)

    kalanSure = 65 - yas

    if kalanSure > 0:
        print(f"{isim}, emekliliginize {kalanSure} yil kaldi.")
    else:
        print(f"{isim}, zaten {abs(kalanSure)} yil once emekli oldunuz.")
    
emekliligeKacYilKaldi(2000,"Aleyna")
