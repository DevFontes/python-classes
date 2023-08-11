list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = [1, 2, 3, 4]

lists_sum = []

# Using for
for i in range(len(list_b)):
    lists_sum.append(list_a[i] + list_b[i])

print(lists_sum)


# Manual Zip
def zipper(la, lb):
    smaller_list = min(len(list_a), len(list_b))
    return [(la[i] + lb[i]) for i in range(smaller_list)]

print(zipper(list_a, list_b))

# Using zip_longest
from itertools import zip_longest

lists_sum_zip = [x + y for x, y in zip_longest(list_a, list_b, fillvalue=0)]

print(lists_sum_zip)



