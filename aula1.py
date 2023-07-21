import datetime

'''nome = 'Jolinha Fontes'
altura = 1.91
peso = 102
imc = peso / altura ** 2

linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'pesa {peso} e tem IMC de {imc:.2f}'
print(linha_1)
# print(nome, 'tem', altura, 'de altura')
print(linha_2)
# print('pesa', peso, 'quilos e tem IMC') 
# print(imc)

"f-strings"

a = 'A'
b = 'BBB'
c = 1.1
string = 'a={} b={} c={:.2f}'
formato = string.format(a, b, c)
print(formato)


idade_gata = int(input('Qual a idade da Gata? '))
# ano_nascimento = idade_gata - datetime.date
soma = idade_gata + 1
# print(datetime.date(year=))
print(f'A Jola tem', idade_gata, 'anos e nasceu em ', soma)


entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no imaginário!')
elif entrada ==  'sair':
    print('Nunca mais será o mesmo, até a vista!')
else:
    print('Você só tem 2 opções')
'''

first_value = input('Type the first value: ')
second_value = input('Type the second value: ')

if first_value > second_value:
    print(
        f'{first_value} is better '
        f'than {second_value}!'
    )
elif second_value > first_value:
    print(
        f'{second_value} is better '
        f'than {first_value}!'
    )
elif first_value == second_value:
    print(
        f'The values are equals!'
    )
