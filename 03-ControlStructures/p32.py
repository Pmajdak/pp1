q1 = input("Are you interested in computer science? (Y/N): ")
q2 = input("Do you like playing computer games? (Y/N): ")
q3 = input("Do you have an Instagram account? (Y/N): ")

if q1 == "Y":
    a1 = "Yes"
else:
    a1 = "No"

if q2 == "Y":
    a2 = "Yes"
else:
    a2 = "No"

if q3 == "Y":
    a3 = "Yes"
else:
    a3 = "No"


print(f'Interested in computer science: {a1}')
print(f'Playing computer games: {a2}')
print(f'Has an Instagram account: {a3}')
