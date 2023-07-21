l = range(10)
c = range(20)

for i in l:
    if i == 0 or i == 9:
        print(80 * '#')
    elif i < 9:
        print('#', 76 * ' ', '#')