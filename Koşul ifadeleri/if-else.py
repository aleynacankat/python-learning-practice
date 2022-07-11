username = "sadikturan"
password = "1234"

isLoggedin = (username == "sadikturan") and (password == "1234")


"""
if ((username == "sadikturan") and (password == "1234")):
    print("merhabaaa")
else:
    print("username ya da parola yanlış")

"""
if (username == "sadikturan"):
    if (password == "1234"):
        print("Uygulamaya hoş geldiniz.")
else:
    print("username yanlış")



kullanici_username = "aleynacankat"
kullanici_password = "12345"

isLogin = (kullanici_username == "aleynacankat") and (kullanici_password == "12345")

if isLogin == True:
    print(f"kullanici girisi dogru, {kullanici_username} hosgeldiniz")
else:
    print("kullanici girisi hatali")