number = int(input('Enter number of products: '))
price = int(input('Enter product price: '))

if number > 2:
    amount = price * number * 0.75
else:
    amount = price * number

print(f'Amount to pay: {amount:.2f}')