def counting(tekst, value):
    return tekst.lower().count(value.lower())


tekst = "You never get a second chance to make a first impression"
value = "e"

print(f"The number of letter '{value}': {counting(tekst, value)}")