print('Simple assign')
shoplist = ['Apple', 'Mango', 'Carrot', 'Bananas']

mylist = shoplist

del shoplist[0]
print('shoplist:', shoplist)
print('mylist:', mylist)

print('Copy throw full :')
mylist = shoplist[:]
del mylist[0]

print('shoplist:', shoplist)
print('mylist:', mylist)