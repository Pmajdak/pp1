def f(kod_produktu):
    return int(kod_produktu[0]) + int(kod_produktu[1]) + int(kod_produktu[2]) % 7 == int(kod_produktu[3])
