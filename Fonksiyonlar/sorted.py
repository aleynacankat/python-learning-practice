
sayilar = [1,53,45,67,97,5,7]

sayilar.sort()
sonuc = sorted(sayilar, reverse = True)
sonuc = sorted((1,53,45,67,97,5,7))

users = [
    {"username": "aleynacankat", "tweets":["tweet1","tweet2"],"email":"info@gmail.com"},
    {"username": "aleynacankat", "tweets":[]},
    {"username": "aleynacankat", "tweets":["tweet1"],"name":"","phone":"1231234"}
]


sonuc = sorted(users, key=len)
sonuc = sorted(users, key=len, reverse = True)
sonuc = sorted(users, key=lambda user: user["username"])
sonuc = sorted(users, key=lambda user: len(user["tweets"]))

kurslar = [
    {"title":"python kursu","students":25000},
    {"title":"web gelistirme kursu","students":35000},
    {"title":"javascript kursu","students":5000},
]

sonuc = sorted(kurslar, key = lambda kurs: kurs["students"])
sonuc = sorted(kurslar, key = lambda kurs: kurs["students"], reverse=True)
sonuc = map(lambda kurs: kurs["title"] sorted(kurslar, key = lambda kurs: kurs["students"], reverse=True))

print(list(sonuc))

print(sayilar)
print(sonuc)

