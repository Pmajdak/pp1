def f(wyrazenie):
    operatory_i_cyfry = [element.strip() for element in wyrazenie.replace('+', ' + ').replace('-', ' - ').split()]
    
    wynik = 0
    
    aktualna_operacja = '+'
    
    for element in operatory_i_cyfry:
        if element in ('+', '-'):
            aktualna_operacja = element
        else:
            wynik = wynik + int(element) if aktualna_operacja == '+' else wynik - int(element)
    
    return wynik
