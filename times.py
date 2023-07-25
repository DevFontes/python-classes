def times (*args):
    total = 1
    for i in args:
        total *= i
    return total

print(times(1,2,3,4))

def even_odd(check):
    return int(check) % 2 == 0

number = input('Input one number to check Even or Odd: ')
print(f'The number {number} is even? {even_odd(number)}')