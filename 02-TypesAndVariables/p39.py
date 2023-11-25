cena = float(input('Wprowadź cenę produktu: '))
rabat = float(input('Wprowadź wartość rabatu: '))

rabat1 = rabat * 0.01
cena_po_rabacie = cena - cena * rabat1
roznica = cena - cena_po_rabacie


print(f'Cena produktu: {cena}')
print(f'Rabat %: {rabat}')
print(f'Cena produktu po rabacie: {cena_po_rabacie}')
print(f'Różnica cen produktu: {roznica}')