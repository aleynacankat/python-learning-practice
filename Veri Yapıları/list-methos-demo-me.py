
isimler = ["Ada","Yiğit","Hasan","Beril"]
yaslar = [1998, 2000, 1998, 1987]
"""
1
isimler.append("Cenk")
sonuc = isimler
print(sonuc)
2
isimler.insert(0,"Sena")
sonuc = isimler

#3 
isimler.pop(1)
sonuc = isimler
print(sonuc)

#4
index = isimler.index("Yiğit")
print(index)

#5
sonuc = "Beril" in isimler
print(sonuc)

#6
isimler.reverse()
sonuc = isimler
print(sonuc)

#7
isimler.sort()
sonuc = isimler
print(sonuc)

#8
yaslar.sort()
sonuc = yaslar
print(sonuc)


#9
s = "IPhone X,IPhone XR"
sonuc = s.split(',')
print(sonuc)

#10
print(min(yaslar))
print(max(yaslar))

#11
yaslar.count(1998)
sonuc = yaslar
print(yaslar.count(1998))

#9 ve 12'yi anlamadım.

markalar = []

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

print(markalar)
"""
