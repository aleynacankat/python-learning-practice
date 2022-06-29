
#Kullanıcıdan isim, yas ve egitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz.
# Ehliyet alma kosulu en az 18, egitim durumu lise ya da universite olmalidir.
"""
isim = input("isminiz: ")
yas = int(input("yasiniz: "))
egitim = input("egitim bilginiz: ")

if (yas >= 18) and (egitim == ("universite") or (egitim == "lise")):
    print("ehliyet almaya uygundur.")
else:
    print(f"{isim},ehliyet almaya uygun degildir.")
"""
#Bir ogrencinin 2 yazili bir sozlu notunu alip, hesaplanan ortalamaya gore not araligina karsilik geen not bilgisini
#  yazdiriniz

yazili1 = float(input("yazili1: "))
yazili2 = float(input("yazili2: "))
sozlu = float(input("sozlu: "))

ortalama = (yazili1 + yazili2 + sozlu)/3

if (ortalama >= 0) and (ortalama < 25): 
    print(f"ortalamaniz: {round(ortalama,2)}")
elif (ortalama >= 0) and (ortalama < 25):
    print(f"ortalamaniz: {round(ortalama,2)}")
elif (ortalama >= 0) and (ortalama < 25):
    





