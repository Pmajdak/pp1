def f(kostka):
    najczestsza_liczba = None
    obecna_liczba = None
    obecna_ilosc = 0
    najwyzsza_ilosc = 0
    
    for cyfra in kostka:
        cyfra = int(cyfra)
        
        if cyfra == obecna_liczba:
            obecna_ilosc += 1
        else:
            obecna_liczba = cyfra
            obecna_ilosc = 1
        
        if obecna_ilosc > najwyzsza_ilosc:
            najwyzsza_ilosc = obecna_ilosc
            najczestsza_liczba = obecna_liczba
    
    return najczestsza_liczba
