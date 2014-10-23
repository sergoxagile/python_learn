def getMax(a, b):
    print('input:', a, b)
    if a > b:
        printMax(a)
    elif a == b:
        print(a, '==', b)
    else:
        printMax(b)
    print('--------------')


def printMax(a):
    print(a, 'Max')

getMax(3,4)
a = 5
b = 5
getMax(a, b)
c = 3
d = 7
getMax(c,d)