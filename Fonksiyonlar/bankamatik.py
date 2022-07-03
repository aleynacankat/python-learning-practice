# Bankamatik Uygulamasi

aleynaHesap = {
    'ad': 'Aleyna Cankat',
    'hesapNo': '12345',
    'bakiye': 3000,
    'ekHesap': 2000
}

kaanHesap = {
    'ad': 'Kaan Cankat',
    'hesapNo': '123456',
    'bakiye': 2000,
    'ekHesap': 1000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print('paranizi alabilirsiniz.')
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if (toplam >= miktar):
            ekHesapKullanimi = input('ek hesap kullanilsin mi (e/h)')

            if ekHesapKullanimi == 'e':
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print('paranizi alabilirsiniz.')
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadir.")
        else:
            print('uzgunuz, bakiye yetersiz :(')        



def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabinizda {hesap['bakiye']} TL bulunmaktadir. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadir.")

paraCek(aleynaHesap, 3000)
bakiyeSorgula(aleynaHesap)
print('**********')
paraCek(aleynaHesap, 2000)
bakiyeSorgula(aleynaHesap)