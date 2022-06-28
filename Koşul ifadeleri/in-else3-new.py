
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

yazili1 = int(input("yazili1: "))
yazili2 = int(input("yazili2: "))
sozlu = int(input("sozlu: "))

ortalama = (yazili1 + yazili2 + sozlu)/3

print(round(ortalama,2))





