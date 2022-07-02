# Kendisine gonderilen 2 sayidan hangisi buyuk bulan fonksiyonu yaziniz.

def karsilastirma(a,b):
    if (a>b):
        return "a b'den buyuk"
    elif (b>a):
        return "b a'dan buyuk"
    return "a b'ye esit"

result = karsilastirma(a=10,b=20)
print(result)

# Kendisine gonderilen bir string icinde her karakter kacar kez tekrarlanmis bulunuz.

def karakterSayisiniBul(s):
    return {letter: string.count(letter) for letter in string} #{a: 5}

sonuc = karakterSayisiniBul("flutter")
# Kendisine gonderilen list, command, position ve value bilgilerine gore
# liste uzerinde guncellenme yap
# [1,2,3], ("add, remove"), ("beginnig, end"), value
# list_operation([1,2,3],"add","end","4") => [1,2,3,4]
# list_operation([1,2,3], "remove","beginning","4") => [2,3]
 
# Kendisine gonderilen renk isimlerimdem icinde "blue" rengi varsa True donduren 
# fonksiyonu yaziniz.
