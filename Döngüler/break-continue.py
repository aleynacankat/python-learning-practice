
"""
name = "Aleyna Cankat"

for harf in name:
    if (harf == "a"):
        break
    print(harf)
"""
"""
i = 0
while (i < 5):
    if (i == 3):
        break
    print(i)
    i += 1
print('dongu bitti.')
"""
"""
i = 0
while (i < 5):
    i += 1
    if (i == 3):
        continue
    print(i)
   i += 1
print('dongu bitti.')
"""

#1-100 arasindaki cift sayilar toplami:

i = 1
toplam = 0

while (i <= 100):
    i += 1
    if (i %2 == 1):
        continue
    toplam += 1
    

print(f"toplam: {toplam}")
