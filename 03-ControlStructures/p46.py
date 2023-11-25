liczba_wierszy = 7
liczba_kolumn = 7

for i in range(1, liczba_wierszy + 1):
    for j in range(i, i + liczba_kolumn * liczba_wierszy, liczba_wierszy):
        print(f'{j:2}', end=' ')
    print()
