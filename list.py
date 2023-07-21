
names_list = ['Maria', 'Helena', 'Luiz']
names_list.append('Sebastião')

i = range(len(names_list))

for ind in i:
    print(ind, names_list[ind])

enumerate_names_list = enumerate(names_list)

for ind in enumerate_names_list:
    print(ind)

# Enumerate
pets_list = ['Jola', 'Neozinho', 'Petty']

print(pets_list)

for ind in enumerate(pets_list):
    print(ind)

print('Lista quebrada por \ n')
print(*names_list, sep='\n')

# Lists in lists
classroom = [
    ['Mary', 'Robert',],
    ['Alfred', ],
    ['Simon', 'Margareth', 'Paul',(100, 200, 300, 400)]
]

print(classroom)

print(classroom[0])
print(classroom[1])
print(classroom[2])

print(classroom[0][1])
print(classroom[2][2])

print(classroom[2][3][1])