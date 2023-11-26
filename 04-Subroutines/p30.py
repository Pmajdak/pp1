def f(number, even):
    digits = str(number)
    
    digit_sum = 0
    
    for digit in digits:
        if (int(digit) % 2 == 0 and even) or (int(digit) % 2 != 0 and not even):
            digit_sum += int(digit)
    
    # Return the final sum
    return digit_sum
