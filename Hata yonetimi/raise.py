
#print(10/0)

# x = 10

# if x > 5:
#     raise ValueError('x 5den buyuk olmaz.')

def colorize(text, color):
    colors = ("blue","red","white","black","orange")
    if type(color) is not str:
        raise TypeError("text str tipinde olmalidir.")

    if type(color) is not str:
        raise TypeError("renk str tipinde olmalidir.")

    if color not in colors:
        raise ValueError("gecersiz bir renk ismi.")
    print(f"{text} {color} renk olarak yazırıldı.")
try:
    colorize("selam","red")
except (Exception, ValueError) as ex:
    print(ex)




