try:
    text = input('Enter somthing -->')
except EOFError:
    print('Cntrl + d')
except KeyboardInterrupt:
    print('Cntrl + c')
else:
    print('Was inputed {}'.format(text))