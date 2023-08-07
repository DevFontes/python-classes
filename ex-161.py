import copy

from products import products

# Create new products list and increase price in 10%

# price + 10%
new_products = [
    {**p, 'price': round(p['price'] * 1.1, 2)}
    for p in copy.deepcopy(products)
]

# descending order name
sorted_products = sorted(
    products,
    key=lambda p: p['name']
)

# descending order price
sorted_price_products = sorted(
    products,
    key=lambda p: p['price']
)


print('Original list')
print(*products, sep='\n')
print('\n')
print('Price increase in 10%')
print(*new_products, sep='\n')
print('\n')
print('Descending name order')
print(*sorted_products, sep='\n')
print('\n')
print('Descending price order')
print(*sorted_price_products, sep='\n')
