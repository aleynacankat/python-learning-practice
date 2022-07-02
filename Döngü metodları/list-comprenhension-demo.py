isimler = ["Ahmet","ali","veLi","Aleyna"]
string = "Hello 12345 World"
yillar = [1983, 1999, 2008, 1956, 1986]
dereceler = [20,5,15,-2,0,-6]

#1- "1-100" arasindaki sayilardan 12'ye tam bölünebilen sayi listesi olusturunuz.

sonuc = [i for i in range(1,101) if i%3 == 0 if i%4==0]

#2- isimler listesindeki her ismi kucuk harke cevirip tersten yazdırın.

sonuc = [i.lower()[::-1] for i in isimler]
#3- verilen "string" içindeki rakamlari iceren bir liste olusturunuz.

sonuc = [i for i in string if i.isdigit()]

#4- "yillar" dizisindeki her dogum yili icin yas bilgisini iceren liste olusturunuz.

import datetime
simdi = datetime.datetime.now().year
sonuc = [simdi - yil for yil in yillar]

#5- "dereceler" listesinde bulunan hava sicaklık bilgisine gore eksi 
#deger icin buzlanma tehlikesi yaziniz.

sonuc = [i if i>=0 else "buzlanma tehlikesi" for i in dereceler]

print(sonuc)