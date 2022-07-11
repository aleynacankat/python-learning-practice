
# def displayUser(*args):
#     print(type(args))
#     print(args)

# displayUser()
"""
def displayUser(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
    print(type(kwargs))
    print(kwargs)

displayUser(username = "aleynacankat", email = "aleynacankat0@gmail.com")

displayUser(username = "aleynacankat")
displayUser(username = "aleynacankat",email = "aleynacankat@gmail.com")
displayUser(username = "aleynacankat",email = "aleynacankat@gmail.com", country="Turkiye")

def myFunc(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,60,key1="value", key2 ="value 2")
"""
def displayUser(*args):
    print(type(args))

displayUser()

def displayUser(**kwargs): #direk dict icine yazdı
    print(type(kwargs))
    print(kwargs)

displayUser(username = "aleynacankat", mail = "aleyna@gmail")