N = int(input("Podaj liczbę N: "))

liczby_pierwsze = []

def czy_pierwsza(liczba):
    if liczba < 2:
        return False
    for i in range(2, int(liczba**0.5) + 1):
        if liczba % i == 0:
            return False
    return True

liczba = 2
while len(liczby_pierwsze) < N:
    if czy_pierwsza(liczba):
        liczby_pierwsze.append(liczba)
    liczba += 1

print(f"Liczby pierwsze: {', '.join(map(str, liczby_pierwsze))}")


# Nie umiem!