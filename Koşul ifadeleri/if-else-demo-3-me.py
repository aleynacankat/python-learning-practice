# 1) Kullanıcıdan isim yaş ve eğitim bilgileri isteyip ehliyet alabilme durumunu kontrol ediniz.
# Ehliyet  alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.
"""
isim = input('isim: ')
yas = int(input('yaş: '))
egitim = input('eğitim: ')

if (yas >= 18):
     if (egitim == 'lise' or egitim == 'üniversite'):
        print('ehliyet alabilirsiniz.')
     else:
        print(f'{isim} ehliyet alamazsınız çünkü eğitim durumu yetersiz.')
else:
    print(f'{isim} ehliyet alamazsınız çünkü yaşınız tutmuyor.')
"""
isim = input("isim: ")
yas = int(input("yasiniz: "))
egitim = input("egitim seviyesi: ")


if (yas >= 18):
     if (egitim == 'lise' or egitim == 'universite'):
          print('ehliyet alabilirsiniz.')
     else:
          print(f"{isim} ehliyet alamazsiniz, cunku egitim durumu yetersiz!")
else:
     print(f"{isim}, ehliyet alamazsiniz. Yasiniz yetersiz!")


# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık 
# gelen not bilgisini yazdırınız.
#    0 -24  => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100 => 5
"""
yazili1 = float(input('1.yazılı: '))
yazili2 = float(input('2.yazılı: '))
sozlu = float(input('sözlü: '))

ortalama = (yazili1 + yazili2 + sozlu) / 3

if(ortalama >= 0) and (ortalama < 25):
     print(f'ortalamanız: {ortalama} ve notunuz: 0')
elif (ortalama >= 25) and (ortalama<45):
     print(f'ortalamanız: {ortalama} ve notunuz: 1')
elif (ortalama >= 45) and (ortalama<55):
     print(f'ortalamanız: {ortalama} ve notunuz: 2')
elif (ortalama >= 55) and (ortalama<70):
     print(f'ortalamanız: {ortalama} ve notunuz: 3')
elif (ortalama >= 70) and (ortalama<85):
     print(f'ortalamanız: {ortalama} ve notunuz: 4')
elif (ortalama >= 85) and (ortalama<=100):
     print(f'ortalamanız: {ortalama} ve notunuz: 5')
else:
    print('yanlış bilgi girdiniz.')

"""
#    0 -24  => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100 => 5

"""
yazili1 = float(input("yazili1: "))
yazili2 = float(input("yazili2: "))
yazili3 = float(input("yazili3: "))

ortalama = yazili1 + yazili2 + yazili3
if(ortalama >= 0) and (ortalama < 25):
     print(f"ortalamanız: {ortalama} ve notunuz: 0")
elif (ortalama >= 25) and (ortalama < 44):
     print(f"ortalamanız: {ortalama} ve notunuz: 1")
elif (ortalama >= 44) and (ortalama < 54):
     print(f"ortalamanız: {ortalama} ve notunuz: 2")
elif (ortalama >= 54) and (ortalama < 69):
     print(f"ortalamanız: {ortalama} ve notunuz: 2")
"""

# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
#    1. Bakım => 1. yıl     
#    2. Bakım => 2. yıl      
#    3. Bakım => 3. yıl     
#    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız..
#    *** datetime modülünü kullanmanız gerekiyor.  
#    (simdi) - (2018/8/1) => gün

import datetime

tarih = input('aracınız hangi tarihte trafiğe çıktı (2019/7/11)')
tarih = tarih.split('/')

simdi = datetime.datetime.now()
trafigeCikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))

fark = simdi - trafigeCikis
gun = fark.days

print(gun)

if (gun<= 365):
    print('1.servis bakımı.')
elif (gun>365) and (gun<=365*2):
    print('2.servis bakımı')
elif (gun>=365*2) and (gun<=365*3):
    print('3.servis bakımı')
else:
    print('hatalı bilgi girdiniz.')
