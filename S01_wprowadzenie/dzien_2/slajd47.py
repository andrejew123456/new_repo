####   Instrukcja raise   ###

def dziel(a, b):
    if b == 0:
        raise ValueError("Dzielnik nie może być zerem.")
    return a / b

# Przykładowe wywołanie funkcji
try:
    wynik = dziel(10, 0)
except ValueError as e:
    print(e)

