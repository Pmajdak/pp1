import p20
import p21

x = int(input("Wprowadź liczbę (1-9): "))
y = p21.generate_number()
if x == y:
    print("You won the game!")
    print(f"Random number: {y}")
else:
    print("Try again!")
    print(f"Random number: {y}")