import os

buy_list = []
functions = ('i', 'd', 'l', 'e')

while True:
    print('Chose a function:')
    function = input('[i]nsert  [d]elete  [l]ist  [e]xit: ')
    os.system('clear')

    if function not in functions:
        continue
    elif function == 'i':
        os.system('clear')
        new_item = input('Input a new item: ')
        buy_list.append(new_item)
    elif function == 'd':
        os.system('clear')
        for i, j in enumerate(buy_list):
            print(i, j)
        remove = input('Which item do you wish to remove? ')
        try:
            del buy_list[int(remove)]
        except ValueError:
            print('Please type the number of the item to remove')
        except IndexError:
            print('Impossible to remove this item')
        except Exception:
            print('Unknow Error')
    elif function == 'l':
        os.system('clear')
        for i, j in enumerate(buy_list):
            print(i, j)
    elif function == 'e':
        break