sayilar = [4,6,9,10,35,57,89,125,244]

# 1: sayilar listesini white ile ekrana yazdırın.
"""
for i in sayilar:
    print(i)
"""
"""
i = 0
while (i<10):
    print(sayilar[i])
    i += 1
"""
"""
while sayilar:
    print(sayilar.pop())

print(sayilar)
"""
# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki 
# tüm tek sayıları ekrana yazdırın
"""
baslangic = int(input("başlangıç: "))
bitis = int(input("bitis: "))

i = baslangic

while i < bitis:
    i += 1
    if (i%2==1):
        print(i)
"""
# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.
"""
i = 100

while (i>0):
    print(i)
    i -= 1
"""

# Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şeklilde yazdırın.
sayilar = []
i = 0
while (i<5):
    sayi = int(input("sayi: "))
    sayilar.append(sayi)
    i += 1

sayilar.sort
print(sayilar)
