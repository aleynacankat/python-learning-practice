"""
try:
    x = int(input('x: '))
    y = int(input('y: '))
    print(x/y)
except ZeroDivisionError:
    print('y sifir olamaz.')
except ValueError:
    print('x ve y sayisal bir deger olmalidir.')
except:
    print('bilinmeyen bir hata olustu.')
"""
while True:
    try:
        x = int(input('x: '))
        y = int(input('y: '))
        print(x/y)
    # except (ZeroDivisionError, ValueError) as e:
    #     print('hata olustu')
    #     print(e)
    except Exception as e: 
        print('bilinmeyen bir hata olustu.')
        print(e)
    else:
        break
    finally:
        print('finally blogu calisir.')