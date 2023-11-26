def f(x, y):
    suma_podzielnych = 0
    
    for liczba in range(x, y + 1):
        if liczba % 2 == 0 and liczba % 3 == 0 and liczba % 4 != 0:
            suma_podzielnych += liczba
    
    return suma_podzielnych
