
#1: Faktoriyel fonksiyonu olusturup, fonksiyona gelen deger için hata mesajları verin.
def faktoriyel(x):
    x = int(x)

    if (x<0):
        raise ValueError("Negatif deger")

    sonuc = 1
    for i in range(1, x + 1):
        sonuc *= i

    return sonuc

for i in [5,7,2,-4,'10a']:
    try:
        x = faktoriyel(i)
    except ValueError as e:
        print(e)
        continue
    else:
        print(x)

#2: girilen parola icinde turkce karakter hatası veriniz.

def parolaKontrol(parola):
    turkce_karakterler = "şçğüöıİ"

    for i in parola:
        if i in turkce_karakterler:
            raise TypeError("Parola turkce karakter iceremez.")
        else:
            pass

    print('gecerli parola')

parola = input('parola: ')

try:
    parolaKontrol(parola)
except TypeError as e:
    print(e)
