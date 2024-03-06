#### Obsluga wyjatkow ###,

try:
    liczba = int(input("Podaj liczbę: "))
except ValueError:
    print("To nie jest liczba!")
