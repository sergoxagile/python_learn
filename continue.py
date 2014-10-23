while True:
    s = input('Enter string more then 3 symbols : ')
    if s == 'exit':
        break
    if len(s) < 4:
        print('Too short...')
        continue
    print('Entered {} - {}'.format(s, len(s)))
print('The end')