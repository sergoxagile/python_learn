ab = {
    'Dred'    : 'soad2003@gmail.com',
    'Alena'   : 'idont@mail.ru',
    'Mam'     : 'shevich2003@gmail.com',
    'Spammer' : 'spammer@hotmail.com'
}

print('My adress:', ab['Dred'])
del ab['Spammer']
print('in adress book {} contacts'.format(len(ab)))
for name, adress in ab.items():
    print('Contact {} with adress {}'.format(name, adress))

ab['Dad'] = 'tsandr@gmail.com'

if 'Dad' in ab:
    print('Dad\'s adress:', ab['Dad'])