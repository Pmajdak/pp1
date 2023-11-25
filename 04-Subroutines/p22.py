def month(n):
    if 1 <= n <= 12:
        miesiace = [
            "Styczeń", "Luty", "Marzec", "Kwiecień",
            "Maj", "Czerwiec", "Lipiec", "Sierpień",
            "Wrzesień", "Październik", "Listopad", "Grudzień"
        ]
        return miesiace[n - 1]
    else:
        return "Nieprawidłowy numer miesiąca"