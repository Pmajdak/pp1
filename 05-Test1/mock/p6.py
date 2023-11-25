def f(number, even):
    digits = [int(digit) for digit in str(number)]
    
    selected_digits = [digit for digit in digits if (digit % 2 == 0) == even]
    
    return sum(selected_digits)
