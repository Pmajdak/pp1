num1 = int(input('Enter number one: '))
num2 = int(input('Enter number two: '))

if num1 >= 0 or num2 >= 0:
    print(f'At least one of entered numbers {num1} and {num2} is not negative')
else:
    print('Both numbers are negative')
