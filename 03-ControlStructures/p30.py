time24 = input('Enter time (24-hour format): ')

godziny, minuty = map(int, time24.split(':'))

if godziny > 12:
    godziny1 = godziny - 12
    znak = 'pm'
else: 
    godziny1 = godziny
    znak = 'am'


print(f'Time in 12-hour format: {godziny}:{minuty} {znak}')