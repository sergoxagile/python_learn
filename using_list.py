shoplist = ['яблоко', 'манго', 'морковь', 'бананы']

print('я должен сделать', len(shoplist), 'bues')

print('Byes:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\nAlso need to bye beer')
shoplist.append('beer')
print('Now my list is:', shoplist)

print('Sort list')
shoplist.sort()
print('Now my list looks like', shoplist)

print('First what i nedd to bye it:', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I both', olditem)
print('now my shoplist:', shoplist)