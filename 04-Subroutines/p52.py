def potega(x, n):
    if n == 0:
        return 1
    else:
        return x * potega(x, n - 1)


wynik = potega(5, 3)
print(f"Wynik potęgowania 5^3 wynosi: {wynik}")
