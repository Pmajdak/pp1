a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

circum = a + b + c
p = circum / 2
area = (p*(p-a)*(p-b)*(p-c))**(1/2)

print('Triangle area:', area)
print('Traingle circumference:', circum)