import decimal

number_1 = 0.1
number_2 = 0.7
number_3 = number_1 + number_2

print(number_3)
print(f'{number_3:.2f}')
print(round(number_3, 2))

number_1_decimal = decimal.Decimal('0.1')
number_2_decimal = decimal.Decimal('0.7')
number_3_decimal = number_1_decimal + number_2_decimal

print('decimal', number_3_decimal)


