def func_outer():
    x = 2
    print('x equal', x)

    def func_inner():
        nonlocal x
        x = 5

    func_inner()
    print('local x change', x)

x = 10
func_outer()
print('global x', x)
