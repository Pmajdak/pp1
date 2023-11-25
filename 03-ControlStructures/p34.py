number = int(input('Enter the amount in PLN: '))

pln5 =  number // 5
rpln5 = number % 5

pln2 = rpln5 // 2
rpln2 = rpln5 % 2

pln1 = rpln2 // 1

print(f'5 zł - {pln5}')
print(f'2 zł - {pln2}')
print(f'1 zł - {pln1}')