"""Napisz funkcję w Pythonie, która sprawdza, czy dany ciąg znaków (string) jest palindromem. Palindrom to słowo, fraza, liczba lub inny ciąg znaków, który czytany od przodu i od tyłu brzmi tak samo, na przykład 'kajak' lub 'radar'.
Przykłady:
Kobyła ma mały bok
kajak
radar

"""
def czy_palindrom(ciag):
    # Oczyszczenie ciągu ze spacji i zamiana na małe litery
    ciag = ciag.replace(" ", "").lower()

    # Sprawdzenie, czy ciąg jest taki sam jak jego odwrócenie
    return ciag == ciag[::-1]

# Testowanie funkcji
print(czy_palindrom("kajak"))  # Powinno zwrócić: True
print(czy_palindrom("Python"))  # Powinno zwrócić: False

