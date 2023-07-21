line = 10
column = 20

name = 'Neozinho Bala'
new_name = ''
lenght_name = len(name)

count_name = 0

while count_name < lenght_name:
    letter = name[count_name]
    new_name += f'*{letter}'
    count_name += 1

print(new_name)