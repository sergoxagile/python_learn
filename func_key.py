def func(a, b=5, c=10):
    print('a = {}, b = {}, c = {}'.format(a,b,c))

func(3,7)
func(25, c = 100)
func(c = 100, a = 200)