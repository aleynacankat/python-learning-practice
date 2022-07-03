# Kendisine gonderilen 2 sayidan hangisi buyuk bulan fonksiyonu yaziniz.
"""
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
 
def update_list(list, command, position, value =None):
        if (command == "remove" and position == "end"):
            return list.pop()
        elif (command == "remove" and position == "begin"):
            return list.pop(0)
        elif (command == "add" and position == "end"):
            list.insert(0,value)
            return list
        elif (command == 'add' and position == 'beginning'):
            list.insert(0,value)
            return list

sonuc = update_list([1,2,3], "add","end","4")
print(sonuc)
"""
# Kendisine gonderilen renk isimlerimdem icinde "blue" rengi varsa True donduren 
# fonksiyonu yaziniz.

def contains_blue(*args):
    if "blue" in args:
        return True
    return False

sonuc = contains_blue("blue","yellow","red")
sonuc = contains_blue("green","yellow","red","black")

print(sonuc)
