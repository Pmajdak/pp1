import random

a = random.randint(1,6)

answer = int(input('Zgadnij liczbę: '))

wynik = a == answer

print(f'Liczba jest taka sama jak wylosowana przez komuter?: {wynik}')

print(f'Liczba wylosowana: {a}')
