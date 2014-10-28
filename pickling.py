import pickle

shopfile = 'shoplist.data'
shoplist = ['apples', 'mango', 'carrot']

f = open(shopfile, 'wb')
pickle.dump(shoplist, f)
f.close()

del shoplist

f = open(shopfile, 'rb')
storedlist = pickle.load(f)
print(storedlist)