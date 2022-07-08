"""
mesaj = "Aleyna Cankat"


print(len(mesaj))



sayi = 22 / 7
sayi1 = 3.234235
print(round(sayi))
print(round(sayi1,3))
print(3 * (5 + 6))
#Matematiksel İşlemler
#Toplama "+"
#Çıkarma "-"
#Çarpma "*"
#Bölme "/"
#Tamsayı Bölmesi "//"
#Kuvvet alma "**"
#Mutlak değer "abs"
#Yuvarlama "round"
#Karşılaştırma operatorleri
#Esittir "=="
#Kucuktur "<"
#Buyuktur ">"
#Kucuk esittir
#Buyuk esittir
#Esit degildir
# String ve Integerlari Birbirine cevirme
"""
""""""
# sayi = 123
# sayi2 = str(sayi)
# print(sayi2)
# i = 1
# i = i + 2 #(i += 2)
# print(i)
"""
renkler = ["Siyah","Beyaz","Sarı","Mavi","Yeşil"]
print(renkler[::2])

renkler.append("Gri")
print(renkler)

renkler.insert(0,"Gri") #eklerken, eklemek istegimiz yere ekleme yaptık!!
print(renkler)

renkler.remove("Sarı")
print(renkler)

renkler2 = ["Turuncu", "Pembe"] #Liste olarak degil, direk icine ekledi!
renkler.extend(renkler2)
print(renkler)

silinen = renkler.pop()
print(renkler) #pembeyi silmiş
print(silinen) #pembe

renkler.reverse() #ters cevirdi
print(renkler)

renkler.sort(reverse = True) # alfabetik sıra
renkler.reverse()

liste4 = sorted(renkler)
print(liste4)
print(renkler)

sayilar = [1,2,39,4,5,7,8]

print(min(renkler))
print(max(sayilar))
print(sum(sayilar))


for i in renkler:
    print(i)

print(list(enumerate(renkler, start=3)))

print("Siyah" in renkler)

#Listeyi stringe cevirdikkkk!
renkler7 = ["Siyah", "Beyaz", "Sarı", "Mavi", "Yeşil"]
stringRenkler = ", ".join(renkler)
print(stringRenkler)

print(type(stringRenkler))

print(stringRenkler)

renkler10 = stringRenkler.split(" MA ")

print(renkler10)

#Tuple (demet) nedir ? 
#Tuple ve List yapilarinin farki ve benzerlikleri
# "Sari", "Mavi", "Yeşil", "Kirmizi", "Siyah"

demet = ("Sari", "Mavi", "Yeşil", "Kirmizi", "Siyah")
print(type(demet))
print(len(demet))
demet[2] = "Pembe"
"""
#Küme nedir ve nasil tanimlanir ? 
# Kümeleri yazdırma
# Kümelere eleman ekleme - silme
# remove - discard metotlarinin farki

kume = {"Sari","Mavi","Yeşil","Kirmizi","Siyah"} 
print(kume)
#append listelerde kullanilir, kumelerde append yok ama add var

kume.add("Pembe")
print(kume)

kume.remove("Sari")


kume.discard("Gri")

kume1 = {"Sari","Mavi","Yesil","Kirmizi","Siyah"}
kume2 = {"Sari","Mavi","Yesil","Beyaz","Siyah"}

print(kume1.intersection(kume2))
print(kume2.difference(kume1))

print("Sari" in kume1)

bosListe1 = []
bosListe2 = list()

bosDemet1 = () #icinde eleman olmayan tuple
bosDemet = tuple() #tuple()

boskume1 = set()
boskume2 = {} # bu bir sozluktur

print(type)

python = set("PYTHON")
print(python)
py = {}

#Sozluk nedir? 
#Sozluk nasil olusturulur ? 
#Sozluk nasil yazdirilir ? 
#Sozlukte verilere nasil erisilir ? 
#Sozlukte veriler nasıl degistirilir ? 
#Sozlukte birden fazla alan nasil degistirilir ? 
#Sozlukten bir alan nasil silinir?
#keys ve values ve items metotlari
#sozlugu for dongusu yardimiyle nasil yazdiririz
#'isim': "ali"


kisi = {"isim":"ali", "yas":20, "cinsiyet":"m","hobiler":["Sinema","Konser","Yazilim"]} #key mutlaka string, values farketmez

print(kisi)

print(kisi["hobiler"])

print(kisi)
kisi["isim"] = "Aleyna"
print(kisi)

kisi.update({"isim":"Aleyna", "yas":30})
print(kisi)

kisi["id"] = 12345 #dictionarye key, value ekledik.
print(kisi) #{'isim': 'Aleyna', 'yas': 30, 'cinsiyet': 'm', 'hobiler': ['Sinema', 'Konser', 'Yazilim'], 'id': 12345}

del kisi["id"] #del fonksiyonuyla silmis olduk
print(kisi)

for x in kisi:
    print(kisi[x]) #value'ları aldım

print(kisi.keys())

print(kisi.values())

print(kisi.items())

for k,v in kisi.items():
    print(k,v)

print(kisi.get("id","Bulunamadi")) #degeri almamizda kullaniyoruz


