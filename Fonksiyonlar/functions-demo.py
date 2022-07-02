#1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gosteren 
# fonksiyonu yaziniz

def yazdir(txt, adet):
    print(txt * adet)

sonuc = yazdir('Merhaba/n', 5)
print(sonuc)

#2- Diktortgenin alan ve cevresini hesaplayan fonksiyonu yaziniz.

def hesapla(kisa, uzun):
    alan = kisa * uzun
    cevre = 2 * (kisa + uzun)

    return f"alan: {alan}, cevre: {cevre}"

print(hesapla(5,7))

#3- Yazi tura uygulamasini fonksiyon kullanarak yapiniz. (random modulü)

def yaziTuraAt():
    import random
    sayi = random.random()

    if sayi > 0.5:
        return "Tura"
    else:
        return "Yazi"

print(yaziTuraAt())

#4- Kendisine gonderilen 2 sayi arasindaki tum asal sayilari bulan fonksiyonu yaziniz.

def asalSayilariBul(sayi1, sayi2):
    for sayi in range(sayi1, sayi2+1):
        if (sayi > 1):
            for i in range(2, sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi) 

asalSayilariBul(10,20)

#5- Kendisine gonderilen bir sayinin tam bolenlerini bir liste seklinde donduren fonksiyonu yaziniz.

def tamBolenleriBul(sayi):
    tamBolenler = []

    for i in range(2,sayi+1):
        if (sayi %i == 0):
            tamBolenler.append(i)
    
    return tamBolenler

print(tamBolenleriBul(15))
print(tamBolenleriBul(35))
