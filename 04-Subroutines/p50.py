def factorial(n):

    if n == 0 or n == 1:
        return 1

    if n > 1:
        return n * factorial(n - 1)

wynik = factorial(5)
print(f"Silnia dla n = 5 wynosi: {wynik}")
