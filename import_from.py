from math import *
n = int(input('Enter value -'))
p = [2,3]
count = 2
a = 5
while (count < n):
    b = 0
    for i in range(2, a):
        if (i <= sqrt(a)):
            if(a % i == 0):
                print('a neprost', a)
                b = 1
    if(b!=1):
        print('a prost', a)
        p = p + [a]
    count += 1
    a += 2
print(p)