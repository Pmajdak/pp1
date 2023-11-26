def f(n):
    liczby_pierwsze = []
    aktualna_liczba = 2
    
    while len(liczby_pierwsze) < n:
        for liczba in liczby_pierwsze:
            if aktualna_liczba % liczba == 0:
                break
        else:
            liczby_pierwsze.append(aktualna_liczba)
        
        aktualna_liczba += 1
    
    return liczby_pierwsze[-1]
