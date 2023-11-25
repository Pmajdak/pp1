x = 5
y = 2


if x > 0 and y > 0:
    cwiartka = "w pierwszej ćwiartce"
elif x < 0 and y < 0:
    cwiartka = "w trzeciej ćwiartce"
elif x < 0 and y > 0:
    cwiartka = "w drugiej ćwiartce"
elif x > 0 and y < 0:
    cwiartka = "w czwartej ćwiartce"
elif x == 0 and y == 0:
    cwiartka = "w położeniu (0,0)"
elif x == 0 and y > 0 or x == 0 and y < 0:
    cwiartka = "na osi x"
elif x > 0 and y == 0 or x < 0 and y == 0:
    cwiartka = "na osi y"

print(f'Punkt P({x},{y}) znajduje się {cwiartka} wykresu współrzędnych')