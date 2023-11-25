def f(liczba_binarna):
    return all(bit in '01' for bit in liczba_binarna)


binarny1 = "101101"
binarny2 = "1311a10100"

print(f"f('{binarny1}') zwraca {f(binarny1)}")
print(f"f('{binarny2}') zwraca {f(binarny2)}")