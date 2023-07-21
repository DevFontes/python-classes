number = input('Type an intenger number: ')

if number.isdigit():
    int_number = int(number)
    if int_number % 2 == 0:
        print(f'The number is even')
    else:
        print(f'The number is odd')
else:
    print(f'Need to imput a intenger number')

time = input('Inform the time: ')

if time.isdigit():
    if int(time) >= 0 and int(time) <= 11:
        print('Gopod Morning')
    elif int(time) >= 12 and int(time) <= 17:
        print('Good afternoon')
    elif int(time) >= 18 and int(time) <= 23:
        print('Good Night')
    else:
        print('Invalid time')
else:
    print('You entered an invalid time')

name  = input('Type your Name: ')

if len(name) > 1:
    if len(name) <= 4:
        print('Short Name!')
    elif len(name) >=5 and len(name) <= 6:
        print('Normal Name!')
    elif len(name) > 6:
        print('Your Name is too big!')
else:
    print('Type more than one letter')