def f(detector):
    obecnosc = 0
    
    for znak in detector:
        obecnosc += 1 if znak == '+' else -1
        
        if obecnosc >= 3:
            return True
    
    return False
