"""
Napisz program, który używa pętli while do czytania liczby od użytkownika,
a następnie sumuje te liczby do czasu wprowadzenia '0', po czym zakończy działanie.

Utwórz pętlę, która przetwarza dane wejściowe od użytkownika i kontynuuje działanie do momentu wprowadzenia określonego słowa kluczowego.
"""

# Inicjalizacja zmiennej do przechowywania sumy
suma = 0

while True:
    # Prośba o wprowadzenie liczby
    liczba = input("Wprowadź liczbę (lub '0' aby zakończyć): ")

    # Sprawdzenie, czy wprowadzona wartość to '0'
    if liczba == '0':
        break

    # Sprawdzenie, czy wprowadzona wartość jest liczbą
    # try:
    liczba = float(liczba)
    # except ValueError:
    #     print("To nie jest liczba. Proszę spróbować ponownie.")
    #     continue

    # Dodanie liczby do sumy
    suma += liczba

# Wyświetlenie sumy po wyjściu z pętli
print("Suma wprowadzonych liczb wynosi:", suma)
