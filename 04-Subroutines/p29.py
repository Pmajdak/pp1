def f(amount_to_pay):
    pln5 = amount_to_pay // 5
    rpln5 = amount_to_pay % 5
    pln2 = rpln5 // 2
    rpln2 = rpln5 % 2
    pln1 = rpln2 // 1
    return pln5 + pln2 + pln1

print(f(23))
print(f(8))
print(f(2))
print(f(0))