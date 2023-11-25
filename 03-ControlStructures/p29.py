czas_prania_kurtka = 40
czas_prania_bielizna = 70
czas_prania_buty = 20
dodatkowe_opcje_plukanie = 15
dodatkowe_opcje_wirowka = 9

produkt_do_prania = "buty"
plukanie = True
wirowka = False

czas_calkowity = 0

if produkt_do_prania == "buty":
    czas_calkowity += czas_prania_buty
elif produkt_do_prania == "bielizna":
    czas_calkowity += czas_prania_bielizna
elif produkt_do_prania == "kurtka":
    czas_calkowity += czas_prania_kurtka
else: 
    print('Nieznany produkt do prania')

if plukanie == True:
    czas_calkowity += dodatkowe_opcje_plukanie

if wirowka == True:
    czas_calkowity += dodatkowe_opcje_wirowka


print(f"Całkowity czas prania: {czas_calkowity} minut.")