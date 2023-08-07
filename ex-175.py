from itertools import groupby

students = [
    {'name': 'Luiz',     'grade': 'A'},
    {'name': 'Letícia',  'grade': 'B'},
    {'name': 'Fabrício', 'grade': 'A'},
    {'name': 'Rosemary', 'grade': 'C'},
    {'name': 'Joana',    'grade': 'D'},
    {'name': 'João',     'grade': 'A'},
    {'name': 'Eduardo',  'grade': 'B'},
    {'name': 'André',    'grade': 'A'},
    {'name': 'Anderson', 'grade': 'C'},
]

def orders(student):
    return student['grade']

students_ordained  = sorted (students, key=orders)
students_grouped   = groupby(students_ordained, key=orders)

# print(*students, sep='\n')
# print('\n', '***### Ordained ###***', '\n')
# print(*students_ordained, sep='\n')
# print('\n', '***### Grouped ###***', '\n')
# print(*students_grouped, sep='\n')

for key, group in students_grouped:
    print(key)
    for student in group:
        print(student)