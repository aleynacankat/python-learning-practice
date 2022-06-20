#1- Girilen bir sayının 50-100 arasında olup olmadığını kontrol ediniz.
"""
sayi = int(input("sayi: "))
sonuc = (sayi > 50) and (sayi <= 100 )

print(f"{sonuc}, 50 ile 100 arasındadır: {sonuc}")
"""
#2- Girilen bir sayının pozitif tek sayı olup olmadığını kontrol ediniz
"""
sayi = int(input('sayı: '))
sonuc = (sayi > 0) and (sayi % 2 == 1)
print('girilen sayı pozitif tek sayıdır: ', sonuc)
"""
#3- Username ve parola bilgileri ile giriş kontrolü yapınız.
"""
_username = "sadikturan"
_password = "1234"

girilenUsername = input('username: ')
girilenPassword = input('parola: ')

sonuc = (girilenUsername == _username) and (girilenPassword == _password)

print(f"girilen username ve password doğru: ", sonuc)
"""
#4 Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
x = input("sayi1: ")
y = input("sayi2: ")
z = input("sayi3: ")





