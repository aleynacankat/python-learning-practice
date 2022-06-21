

# email, password => database

# email == 'info@sadikturan.com'
# password = '12345'

# a, b, c, d = 5, 5, 20, 4

# username = 'sadikturan'
# password = '12345'

# sonuc = (True == 1)

# sonuc = False == 0
# sonuc = False + True + 50

# print(sonuc)
# print(int(True)) #1

# Girilen 2 sayıdan hangisi büyüktür ? 

# sayi1 = input('sayi1: ')
# sayi2 = input('sayi2: ')

# sonuc = (sayi1 > sayi2)

# print(f"{sayi1} {sayi2} den büyüktür: {sonuc}")

# vize1 = float(input("vize1: "))
# vize2 = float(input("vize2: "))
# final = float(input("final: "))

# ortalama = (((vize1 + vize2) / 2 ) * 0.6) + (final * 0.4)
# print(f"not ortalamanız: {ortalama} ve dersten geçme durumunuz: {ortalama>=50}")

"Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz"
#email: info@sadikturan.com parola: 12345

# _email = "info@sadikturan.com"
# _password = "12345"

# email = input("email: ")
# password = input("password: ")

# isEmail = (email.lower().strip() == _email)
# isPassword = (password.strip() == _password)

# print(f"email doğruluğu: {isEmail} ve parola doğruluğu: {isPassword}")

from re import A

# yas => 18 ve (mezuniyet == "lise" ya da mezuniyet == "üniversite")

x = 10

sonuc = 5 < x < 15

sonuc = (x > 5) and (x < 15) #True ve True 
#True ve True => True 
#False ve True => False
#False ve False => False

hak = 1
devam = 'e'

sonuc = (hak > 0) and (devam == 'e')

# or operatörü (veya)

(x > 0) #sayı pozitif

(x % 2 == 0) #sayı çift 

sonuc = (x > 0) and (x % 2 == 0)

print(sonuc)

sonuc = not(x > 0)

"x, 5-10 arasında bir çift sayı mı ?"
"""
sonuc = (x>5) and (x<10)

print(sonuc)
"""
#Girilen bir sayının 50-100 arasında olup olmadığını kontrol ediniz.
"""
sayi = int(input("sayi: "))
sonuc = (sayi > 50) and (sayi <=100)
print(f"{sayi}, 50 ile 100 arasındadır: {sonuc}")"""
""""
#Girilen bir sayının pozitif tek sayı olup olmadığını kontrol ediniz.
sayi = int(input("sayi:"))
sonuc = (sayi > 0) and (sayi % 2 == 1)

"""

# _username = "aleynacankat"
# _password = "1234"

# girilenUsername = input("username: ")
# girilenPassword = input("password: ")

# sonuc = (girilenUsername == _username) and (girilenPassword == _password)
# print("girilen username ve parola doğru", sonuc)
"""
x = int(input('x: '))
y = int(input('y: '))
z = int(input('z: '))

sonuc = (x>y) and (x>z) # x en büyük
print("x en büyük sayi: ", sonuc) 

sonuc = (y>x) and (y>z) # x en büyük 
print("y en büyük sayi: ", sonuc)

sonuc = (z>x) and (z>y) # x en büyük 
print("z en büyük sayi: ", sonuc)
"""
#2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
# eğer ortalama 50 ve üstüyse geçti değilse kaldı
# ortalama 50 olsa bile final notu en az 50 olmalı
# finalden 70 alındığında ortalamanın bi önemi yoktur
"""
vize1 = float(input('vize1: '))
vize2 = float(input('vize2: '))
final = float(input('final: '))

kosul1 = final >= 50
sonuc2 = ((((vize1 + vize2)*0.6) + (final*0.4))/2) > 50
notu = ((((vize1 + vize2)*0.6) + (final*0.4))/2)
result = kosul1 and sonuc2

print("Geçer", result, notu)
"""

# ad = input('adiniz: ')
# kg = float(input('kilonuz: '))
# hg = float(input('boyunuz: '))

# kiloIndeks = kg / (hg ** 2)

# zayif = (kiloIndeks >= 0) and (kiloIndeks <= 18.4)
# normal = (kiloIndeks > 18.4) and (kiloIndeks <= 24.9)
# kilolu = (kiloIndeks > 24.9) and (kiloIndeks <= 29.9)
# obez = (kiloIndeks >= 29.9) and (kiloIndeks <= 34.9)

# print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo degerlendirmen zayif: {zayif}")
# print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo degerlendirmen zayif: {normal}")
# print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo degerlendirmen zayif: {kilolu}")
# print(f"{ad} kilo indeksin: {kiloIndeks} ve kilo degerlendirmen zayif: {obez}")



