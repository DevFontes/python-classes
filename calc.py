while True:
    num_1    = input('Type one number: ')
    num_2    = input('Type other number: ')
    operator = input('Type the operator (+-/*): ')

    valid_numbers = None

    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        valid_numbers = True
    except:
        valid_numbers = None

    if valid_numbers == None:
        print('Some invalid Number')
        continue

    allow_operators = '+-/*'

    if operator not in allow_operators:
        print('Invalid Operator')
    
    if len(operator) > 1:
        print('Type only one operator')
    
    print('Calculating....')

    if operator == '+':
        print(f'{num_1_float} + {num_2_float} =', num_1_float + num_2_float)
    if operator == '-':
        print(f'{num_1_float} - {num_2_float} =', num_1_float - num_2_float)
    if operator == '/':
        print(f'{num_1_float} / {num_2_float} =', num_1_float / num_2_float)
    if operator == '*':
        print(f'{num_1_float} * {num_2_float} =',num_1_float * num_2_float)
    else:
        ('Error!')


    exit = input('Exit? [y]es: ').lower().startswith('y')

    if exit:
        break