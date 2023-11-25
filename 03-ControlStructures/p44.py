suma = 0
ilosc = 0

while True:
    liczba = float(input('Wprowadź liczbę: '))

    if liczba == 0:
        break

    suma += liczba
    ilosc += 1

srednia = suma / ilosc if ilosc > 0 else 0


print(f"RESULT: Quantity={ilosc}, Sum={suma}, Mean={srednia}")
