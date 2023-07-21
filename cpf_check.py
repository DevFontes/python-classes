# cpf = input("Type the CPF (only numbers): ")
cpf = '74682489070'
multiplicator = 10
check = 0

for digit in cpf:
    if multiplicator > 1:
        check += int(digit) * multiplicator
        multiplicator -= 1
check *= 10
dec_digit = check % 11
if dec_digit > 9:
    if int(cpf[9]) == 0:
        print("First digit is correct!")
    else:
        print("***First digit is wrong***")
else:
    if int(cpf[9]) == dec_digit:
        print('First digit is correct!"')
    else:
        print("***First digit is wrong***")

