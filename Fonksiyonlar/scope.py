
from re import X


x = 'global x'

def function():
    # local scope
    x = 'local x'
    print(x)

function()
print(x)
####################
name = 'Aleyna'

def changeName(new_name):
    name = new_name
    print(name)

changeName('Kaan')
print(name)

###############

name = 'global string'

def greeting():
    # name = 'Aleyna'

    def hello():
        # name = 'Kaan'
        print('hello' + name)

    hello()

greeting()

##########

x = 50
def test():
    #local
    global x #globalde degistirmek istedigim icin global keywordunu kullandim.
    print(f'x: {x}')

    x = 100
    print(f'change x to {x}')

test()

print(x)