name  = input('Type your Name: ')
age = input('Type your Age: ')

try:
    int_age = int(age)
except:
    print(f'Invalid Age!')
    exit

if name and age:
    print(f'Your name is: {name}')
    print('Your inverted Name is: ', name[::-1])
    
    if ' ' in name:
        print(f'Your Name has space(s)')
    else:
        print(f'Your Name has no space(s)')
    
    print(f'Your Name has {len(name)} characters')
    print(f'The first letter of your name is: ', name[0])
    print(f'The last letter of your name is: ', name[-1])
else:
    print('Sorry, you letf fields empty')