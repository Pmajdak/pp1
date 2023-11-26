def f(x, y):
    liczba_ujemnych_parzystych = 0
    
    for liczba in range(x, y):
        if liczba < 0 and liczba % 2 == 0:
            liczba_ujemnych_parzystych += 1
    
    return liczba_ujemnych_parzystych
