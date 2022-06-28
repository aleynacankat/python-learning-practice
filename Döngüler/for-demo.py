from itertools import count
from operator import index


sayilar = [1,5,15,35,37,57,72]

#1 sayilar listesindeki her bir elemanı yazdırın.
"""
for x in sayilar:
    print(x)
"""

#2 sayilar listesindeki hangi sayilar 5'in katidir ?
"""
for sayi in sayilar:
    if (sayi % 5 == 0):
        print(sayi)
"""

#3 sayilar listesinde sayiların toplami kaçtir?
"""
toplam = 0
for sayi in sayilar:
    toplam  = toplam + sayi
print(toplam)
"""
#4 sayilar listesinde çift sayiların karesini alınız.
"""
for sayi in sayilar:
    if (sayi % 2 == 0):
        print(sayi, sayi*sayi)
"""
"""
for sayi in sayilar:
    if (sayi %2 == 0):
        print(sayi, sayi*sayi)
"""

urunler = ["iphone 8", "iphone x", "iphone xr", "samsung s10"]
#5 urunler listesindeki tüm ürünlerin 2. karakterini ekrana yazdirin.
"""
for urun in urunler:
    print(urun[1])
"""
"""
for urun in urunler:
    print(urun[1])
"""
#6 urunler listesinde içinde iphone geçen kaç ürün vardır ? 
# (index, find)

"""
count = 0
for urun in urunler:
    index = urun.find("iphone")
    if (index > 1):
        count +=1
print(count)
"""
count = 0
for urun in urunler:
    index = urun.find("iphone")
    if (index > 1):
        count += 1
print(count) 

