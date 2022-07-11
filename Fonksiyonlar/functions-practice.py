#Fonksiyon kavrami ve onemi : Aynı şeyi Tekrar tekrar yazmamızda, kullanıcağımız işlemlerde, fonksiyon kullanmak daha mantıklıdır.
#Fonksiyonlari tanimlama ve calistirma
#Parametre almayan ve alan fonksiyonlar
#Return anahtar kelimesi
#Parametrelere varsayılan değerler atamak
"""
def selamla(isim):
    print("Merhaba" + isim)

selamla("Aleyna")
"""
"""
def topla(x,y):
    print(f"x + y = {x + y}")

topla(3,6)
"""
"""
def ortalamaHesapla(liste):
    toplam = sum(liste)
    adet = len(liste)
    ortalama = toplam / adet
    print(f"girilen sayilarin ortalamasi: {ortalama}")

ortalamaHesapla([1,2,3,4,5,6,7])
"""
"""
def buyukHarfeCevir(metin):
    metin = metin.upper()
    print(metin)

buyukHarfeCevir("anSdfrTsD")
"""
"""
def selamla(mesaj, isim = "Anonim"):
    print(f"{mesaj} {isim}")

selamla("merhaba")
"""
"""
def indirimYap(fiyat, yuzde = 20):
    indirimMiktari = fiyat * (yuzde/100)
    indirimliFiyat = fiyat - indirimMiktari
    print(f"İndirimli tutar: {indirimliFiyat}")

indirimYap(50,10)
"""
"""
def topla(x,y):
    print(x + y)
    return x + y

sonuc = topla(3,8)
print(sonuc)
"""
"""
def ortalamaHesapla(x,y):
    return(x+y)/2

a = ortalamaHesapla(2,6)
b = ortalamaHesapla(6,10)
print(a + b)
"""
"""
def buyukHarfeCevir(metin):
    return metin.upper()

a = buyukHarfeCevir("AsDfG")
print(a)
"""

# def buyukHarfeCevir(metin):
#     return metin.upper()

# func = buyukHarfeCevir

# sonuc = func("HuOfdE")
# print(sonuc)
"""
from xml.dom.expatbuilder import theDOMImplementation


def topla(a,b): #Fonksiyonumuzun ne işe yaradigini belirttik
    c = a + b #Fonksiyonun, iceri gelen a ve b sayilariyle ne yapacgina karar verdik
    return c # a ve b sayilarinin toplamiyle olusan c sayisinin istenilen yere yani toplama
    #ulastirilmasini sagladik.

toplam = topla(3,2)
print(toplam) 
# 'toplam' ( toplam = c ) olarak düsünmek daha kolay olur. Cunku 
#aslinde c degerini yazdiriyor.
"""

def topla(a,b):
    c = a + b
    return

topla(2,3)