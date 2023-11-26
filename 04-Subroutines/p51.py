def suma(n):
    if n == 1:
        return 1
    else:
        return n + suma(n - 1)


wynik = suma(10)
print(f"Suma naturalnych liczb od 1 do 10 wynosi: {wynik}")
