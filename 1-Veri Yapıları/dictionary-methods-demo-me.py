"""

player 1:
    id = 1
    name = Coronel Whatsapp
    yearOfBirth = 1985
    nationality = Portugal
    current_team = Portugal
    history = Juventus,Real Madrid,Portugal

player 2:
    id = 2
    name = Lionel Messi
    yearOfBirth = 1987
    nationality = Argentina
    current_team = Barcelona
    history = Barcelona,Argentina,Portugal
"""

#1 Yukardaki bilgileri liste içinde saklayınız.
#2 id'ye göre arama yapınız.
#3 id'ye göre bilgi kayıt siliniz.

players = {
    "1":
    {
        "name": "Coronel Whatsapp","yearOfBirth": "1985", "nationalty": "Portugal", "current_team": "Portugal", "history": ["Juventus", "Real Madrid", "Portugal"]
    },
    "2":
    {
        "name": "Lionel Messi","yearOfBirth": "1987", "nationalty": "Argentina", "current_team": "Barcelona", "history": ["Barcelona", "Argentina", "Portugal"]
    }
}

id = input('oyuncu id: ')
name = input('oyuncu ad: ')
nationality = input("ülke: ")
yearOfBirth = input('doğum yılı: ')
current_team = input('takım: ')
history = input('oynadığı yerler: ')

print(players)





