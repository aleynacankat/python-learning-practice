#1) Girilen 2 sayıdan hangisi büyüktür ? 
"""
sayi1 = int(input("sayi1: "))
sayi2 = int(input("sayi2: "))

sonuc = (sayi1 > sayi2)

print(f"{sayi1} {sayi2} den büyüktür: {sonuc}") 

"""
#2 Girilen bir sayının tek mi çift mi olduğunu yazdırın.
"""
sayi = int(input("sayı: "))

sonuc = (sayi % 2 == 0)

print(f"{sayi} çift sayidir: {sonuc}")
"""
#3 Girilen bir sayının negatif pozitif durumunu yazdırın.
"""
sayi = int(input("sayi: "))

sonuc = sayi > 0 

print(f"{sayi} negatiftir: {sonuc}")
"""
#4 Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
# Eğer ortalama 50 ve üstündeyse geçti, değilse kaldı yazdırın.
"""
vize = float(input("vize: "))
final = float(input("final: "))

ortalama = (vize * 0.60) + (final * 0.40)
sonuc = ortalama > 50

print(f"{sonuc} Geçti ")
"""
"""
vize1 = float(input("vize1: "))
vize2 = float(input("vize2: "))
final = float(input("final: "))
ortalama = (((vize1 + vize2) / 2) * 0.6) + (final * 0.4)

print(f"not ortalamanız: {ortalama} ve dersten geçme durumunuz: {ortalama >= 50}")

"""
#5 parola ve email bilgisini isteyip, doğruluğunu kontrol ediniz.

email_ = "asd@gmail.com"
parola_ = "1234"

email = input("email: ")
parola = input("parola: ")

isEmail = (email.lower().strip() == email_)
isPassword = (parola.strip() == parola_)

print(f"email doğruluğu: {isEmail} ve parola doğruluğu: {isPassword}")


