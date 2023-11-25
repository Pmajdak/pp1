height = int(input('Enter your height in cm: '))
weight = int(input('Enter your weight in kg: '))

heightM = height * 0.01

bmi = weight/ heightM**2
correct_weight = 18.5 < bmi < 24.9

print('Twoje BMI: ', bmi)
print('Poprawna waga:', correct_weight)