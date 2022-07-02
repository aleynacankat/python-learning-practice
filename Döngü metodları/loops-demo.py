#1-100 arasında rasgele üretilecek bir sayıyı aşağı yukarı
#ifadeleri ile buldurmaya çalışın.
#*** "random modülü" için python random şeklinde arama yapın
# 100 üzerinden puanlama yapın. Her soru 20 puan
# Hak bilgisini kullanıcıdan alın ve her soru belirtilen can 
# sayisi uzerinden hesaplasin

import random

sayi = random.randint(1,10)
can = int(input('kac hak kullanmak istersiniz? '))
hak = can
sayac = 0

while hak > 0:
    hak -=1
    sayac += 1
    tahmin = int(input('tahmin: '))

    if sayi == tahmin:
        print(f'Tebrikler, {sayac}. defa bildiniz. Toplam puaniniz: {100 - ((100/can) * (sayac-1))}')
        break
    elif sayi > tahmin:
        print('yukari')
    else:
        print('asagi')

    if hak == 0:
        print(f'hakkiniz bitti. Tutulan sayi: {sayi}')