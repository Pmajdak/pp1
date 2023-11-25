import random

a = random.randint(1,6)

wynik = a == 1 or a == 6

print(f'Dice rolled: {a}')
print(f'Special number: {wynik}')