import re

cpf = input("Type the CPF: ")

cpf = str(re.sub(
    r'[^0-9]',
    '',
    cpf))

multiplicator = 10

def calc(x, y):
    calc_digit = 0
    for i in x:
        if y > 1:
            calc_digit += int(i) * y
            y -= 1
    calc_digit = (calc_digit * 10) % 11
    return calc_digit

if calc(cpf, multiplicator) > 9 and int(cpf[9]) == 0:
    multiplicator = 11
    if calc(cpf, multiplicator) > 9 and int(cpf[10]) == 0:
        print(f'CPF {cpf} is Valid!')
    elif calc(cpf, multiplicator) <= 9 and int(cpf[10]) == calc(cpf, multiplicator):
        print(f'CPF {cpf} is valid!')
elif calc(cpf, multiplicator) == int(cpf[9]):
    multiplicator = 11
    if calc(cpf, multiplicator) > 9 and int(cpf[10]) == 0:
        print(f'CPF {cpf} is Valid!')
    elif calc(cpf, multiplicator) <= 9 and int(cpf[10]) == calc(cpf, multiplicator):
        print(f'CPF {cpf} is valid!')
    else:
        print(f'***CPF {cpf} is invalid***')
else:
    print(f'***CPF {cpf} is invalid***')

