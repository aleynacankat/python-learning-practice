from multiprocessing.sharedctypes import Value


markalar = ["opel", "bmw", "mercedes"]

# index = 0
# for marka in markalar:
#     print(f"{index}-{marka[index]}")
#     index += 1

# enumerate ile liste yazdırabiliyoruz.
"""
obj1 = enumerate(markalar)
print(type(obj1))
print(list(obj1))

for index,value in enumerate(markalar):
    print(f"{index+1} - {value}") #0 dan başlamasın diye 1 ekledim

for index,value in enumerate(markalar,1):
    print(f"{index+1} - {value}")
"""

liste1 = [1,2,3,4,5]
liste2 = ['a','b','c','d','e','f']
liste3 = [100,200,300,400,500]

print(list(zip(liste1, liste2, liste3))) #[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]

for item in zip(liste1, liste2):
    print(item)

for a,b,c in zip(liste1, liste2, liste3):
    print(a,b,c)
