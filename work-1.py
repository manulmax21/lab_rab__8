import numbers


def test():
    number = int(input('введите число: '))
    if number > 0:
        positive()
    elif number < 0:
        negative()
    else:
        print("я вас не совсем понял. ;)")
        test()
def positive():
    print('положительное')
def negative():
    print('отрицательное')
test()