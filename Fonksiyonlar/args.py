# liste = [10,20,30,40]

# def toplam(sayilar):
#     sonuc = 0
#     for i in sayilar:
#         sonuc += i
#     return sonuc

# print(toplam(liste))

"""
def toplam(*args):
    print(type(args))
    sonuc = 0
    for i in args:
        sonuc += i
    return sonuc

print(toplam(10,20,30))
print(toplam(10,20,30,40))

a = 10,20,30

for i in a:
    print(i)

    
print(a)
"""

liste = [10,20,30]

def toplam(sayilar):
    sonuc = 0
    for i in sayilar:
        sonuc += 1
    return sonuc

print(toplam(liste))


def toplam(*args):
    sonuc = 0
    for i in args:
        sonuc += i
    return sonuc
    #args ile kendi sectigimiz degerleri kullanabiliriz.


def toplam(a,b,c):
    return(a+b+c)


