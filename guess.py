number = 23
run = True
while run:
    guess = int(input("Введите число: "))
    if guess == number:
        print('ура угодали')
        run = False;
    elif guess < number:
        print('Загаданное число больше')
    else:
        print('Загаданное число меньше')
else:
    print('The end...')