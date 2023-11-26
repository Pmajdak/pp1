def f(number):
    num_str = str(number)
    suma_powtarzajacych_sie_cyfr = 0
    sprawdzone_cyfry = set()
    
    for cyfra in num_str:
        if cyfra not in sprawdzone_cyfry:
            ilosc_powtorzen = num_str.count(cyfra)
            
            if ilosc_powtorzen > 1:
                suma_powtarzajacych_sie_cyfr += int(cyfra) * ilosc_powtorzen
            
            sprawdzone_cyfry.add(cyfra)
    
    return suma_powtarzajacych_sie_cyfr
