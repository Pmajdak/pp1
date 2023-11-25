car_plate = input("Podaj numer rejestracyjny pojazdu: ")

czy_z_krakowa = car_plate.upper().startswith('KR') or car_plate.upper().startswith('KK')

print("Numer rejestracyjny pojazdu:", car_plate)
print("Czy samochód jest z Krakowa:", czy_z_krakowa)