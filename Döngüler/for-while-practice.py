#listeler, for, range, break-continue

# liste = [1,2,3,4,5,6]

# for rakam in liste:
#     print(rakam)

# isim = "Aleyna"

# for harf in isim:
#     print(harf)

""" Bir işlemi 10-202323 kere tekrar etmek istiyorsam RANGE kullanicam!! (bir işlemi belli bir sayıda tekrarlatmak demek"""


# demet = (1,2,3,4)

# for i in demet:
#     print(i)
"""
for i in range(0,10): #ilk sınırı dahil eder, ikinciyi dahil etmez!!
    print(i)

for i in range(1,17,2): #2şer 2şer yazdı!!
    print(i)

sonuc = 1
for i in range(0,10):
    sonuc *= 2
print(sonuc)
############
liste1 =["a", "b", "c"]
liste2 = [1,2,3]

for harf in liste1:
    for rakam in liste2:
        print(harf,rakam)
"""
#################
"""
liste = [1,2,3,4,5,6,7,8,9]

for i in liste:
    if i == 3:
        print("3'u atladik")
        continue #bunun anlamı 3 e gelince geç devam et 3ü atla demek istiyoruz.
    print(i)
"""
"""Eğer continue yerine break yazsaydım 3'ten sonrasını yazmayacaktı, farkı bu!!! DÖNGÜYÜ SONLANDIRIR! continue ise bir elemanı pas g
gecip, listenin sonuna kadar devam etmesini saglar."""
"""
for i in liste:
    if i == 3:
        print("3'u atladik")
        break
    print(i)


liste = range(100)

for i in liste:
    if i %3 != 0:
        continue #böyle yaptigimiz zaman da 3er 3er yazdirmis olduk.
    if i == 81:
        break
    print(i)
"""

# While dongusu belirli bir kosul saglandigi surece calisan bir dongudur! 
"""
x = 2

while x < 10:
    print(x)
    x += 1 #x 10'dan kucuk oldugu surece bunu yap demektir. Bu kosul bozulana kadar devam eder.
print("x:", x)
"""
"""
x = 2
y = 3 

while x*y < 1000:
    print(x,y)
    x += 2
    y += 2

i = 1 
while True:
    print(i)
    i += 1
    if i == 10:
        break
"""
"""
i = 1
while True:
    if i %2 == 0:
        i += 1
        continue
    print(i)
    i += 1
    if i == 10:
        break
"""

# sayi = float(input("Bir sayi giriniz: "))
# print(sayi)


#ekrandan alınan bir sayının faktoriyelini hesaplayan bir program yazınız.
"""
sayi = input("Bir sayi giriniz: ")
print(type(sayi))

sayi = int(input("bir sayi giriniz: "))

faktoriyel = 1

for i in range(1,11):
    faktoriyel *= i
    print(f"{sayi}! = {faktoriyel}")
"""
"""
sayi = int(input("Bir sayi giriniz: "))

faktoriyel = 1

i = 2
while i <= sayi:
    faktoriyel *= i

print(f"{sayi}! = {faktoriyel}")
"""

#ekrandan alınan bir sayinin asal olup olmadiginizi kontrol eden bir program yaziniz.
"Bir sayinin asal olup olmadigini kontrol ediyor"
"""
sayi = int(input("Bir sayi giriniz: "))

prime = True

for i in range(2,sayi):
    if sayi %i == 0:
        prime = False
        break
if prime == True:
    print(f"{sayi} sayisi asaldir.")
else:
    print(f"{sayi} sayisi asal degildir.")
"""
#ekrandan alınan bir sayinin pozitif kaç tane böleni oldugunu bulan bir program yaziniz.
"""
sayi = int(input("Bir sayi giriniz: "))

bolen_sayisi = 0
for i in range(1,sayi + 1):
    if sayi %i == 0:
        bolen_sayisi += 1
print(f"{sayi} sayisinin {bolen_sayisi} tane boleni vardir.")
"""
#ekrandan okunan bir sayinin rakamlari toplamini hesaplayan bir program yaziniz.
"""
sayi = int(input("Bir sayi giriniz: "))
str_sayi = str(sayi)
toplam = 0
for rakam in str_sayi:
    toplam += int(rakam)
print(toplam)
"""
"""
sayi = int(input("Bir sayi giriniz: "))

toplam = 0
gecici_sayi = sayi

while gecici_sayi != 0:
    basamak = gecici_sayi % 10
    toplam += basamak
    gecici_sayi //= 10

print(toplam)
"""
#ekrandan pespese okunan 5 sayisinin en kucugunu ve en buyugunu ekrana yazdiran bir program yaziniz.
"""
liste = []

for i in range(5):
    sayi = int(input("Bir sayi giriniz: "))
    liste.append(sayi)
print(f"en buyuk sayi: {max(liste)}")
print(f"en kucuk sayi: {min(liste)}")
"""
#ekrandan okunan bir sayinin herhangi bir sayinin karesi olup olmadigini kontrol eden bir program yaziniz.
"""
sayi = int(input("Bir sayi giriniz: "))

karekok = sayi ** 0.5

if karekok == int(karekok):
    print("Tamkare")
else:
    print("Tamkare degil")
"""
#ekrandan okunan bir metinde hangi harfin kaç kez kullanıldıgına dair program yaziniz.
"""
metin = input("Bir metin yaziniz: ")
sozluk = dict()

for harf in metin:
    if harf in sozluk:
        sozluk[harf] += 1
    else:
        sozluk[harf] = 1
for harf, adet in sozluk.items():
    print(harf, adet)
"""
#ekrandan okunan bir metinde a harflerini buyuk yapan bir programa yaziniz

metin = input("Bir metin giriniz: ")

metin2 = " "

for harf in metin:
    if harf == "a":
        metin2 += "A"
    else:
        metin2 += harf
print(metin2)


