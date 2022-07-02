#1- Çarpım tablosu hazirlayiniz.
for i in range(0,11):
    print('***********')
    for k in range(1,11):
        print("{} x {} = {}".format(i,k,i*k))

#2- Girilen bir sayinin asal olup olmadigini kontrol ediniz.
# Asal sayi 1 ve kendisi hariç tam boleni olmayan sayilara denir.

sayi = int(input('sayi: '))

asalmi  = True
if (sayi == 1):
    asalmi = False

for i in range(2,sayi):
    if (sayi % i == 0):
        asalmi = False
        break

if asalmi:
    print('sayi asaldir.')
else:
    print('sayi asal degildir.')