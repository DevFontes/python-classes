import re
cpf = input("Type the CPF: ")
# cpf = '74682489070'
# cpf = '47505406643'
# cpf = '36598906874'
# cpf = '03636157680'
cpf = str(re.sub(
    r'[^0-9]',
    '',
    cpf))

multiplicator = 10
check = 0
for digit in cpf:
    if multiplicator > 1:
        check += int(digit) * multiplicator
        multiplicator -= 1
dec_digit = (check * 10) % 11
if dec_digit > 9 and int(cpf[9]) == 0:
    multiplicator = 11
    check = 0
    for digit in cpf:
        if multiplicator > 1:
            check += int(digit) * multiplicator
            multiplicator -= 1
    dec_digit = (check * 10) % 11
    if dec_digit > 9 and int(cpf[10]) == 0:
        print(f'CPF {cpf} is Valid!')
    elif dec_digit <= 9 and int(cpf[10]) == dec_digit:
        print(f'CPF {cpf} is valid!')
elif dec_digit == int(cpf[9]):
    multiplicator = 11
    check = 0
    for digit in cpf:
        if multiplicator > 1:
            check += int(digit) * multiplicator
            multiplicator -= 1
    dec_digit = (check * 10) % 11
    if dec_digit > 9 and int(cpf[10]) == 0:
        print(f'CPF {cpf} is Valid!')
    elif dec_digit <= 9 and int(cpf[10]) == dec_digit:
        print(f'CPF {cpf} is valid!')
    else:
        print(f'***CPF {cpf} is invalid***')
else:
    print(f'***CPF {cpf} is invalid***')

