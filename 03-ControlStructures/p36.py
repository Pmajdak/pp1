number = int(input('Enter number (1-10): '))

i = 0
for i in range(1,11):
    answer = number * i
    print(f'{number} x {i} = {answer}')