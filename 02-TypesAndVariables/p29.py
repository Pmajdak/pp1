import random

a = random.randint(1,6)
b = random.randint(1,6)
c = random.randint(1,6)
suma = [a, b, c]
print('Rzut kostką nr.1:', a)
print('Rzut kostką nr.2:', b)
print('Rzut kostką nr.3:', c)

print('Suma oczek z kości:', sum(suma))