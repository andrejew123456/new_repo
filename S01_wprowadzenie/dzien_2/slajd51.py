####   ROZWIAZANIE   ####
"""
Zadanie: Kalkulator Dzielący z Obsługą Wyjątków
Opis Zadania:
Stwórz prosty kalkulator, który wykonuje dzielenie dwóch liczb podanych przez użytkownika. Zadbaj o to, aby program obsługiwał wyjątki związane z nieprawidłowym wejściem (np. dzielenie przez zero, wprowadzenie wartości, która nie jest liczbą).
"""

"""Krok 1: Definicja Funkcji dzielenie
Stwórz funkcję dzielenie, która przyjmuje dwa argumenty i wykonuje dzielenie, a następnie obsługuje potencjalne wyjątki.
"""
def dzielenie(a, b):
    try:
        wynik = a / b
    except ZeroDivisionError:
        return "Błąd: Dzielenie przez zero!"
    except TypeError:
        return "Błąd: Nieprawidłowy typ danych!"
    else:
        return wynik


"""Krok 2: Testowanie Funkcji
Stwórz kilka testowych przypadków, aby przetestować działanie funkcji dzielenie.
"""
# Przykładowe testy
print(dzielenie(10, 2))  # Poprawne dzielenie
print(dzielenie(5, 0))   # Dzielenie przez zero
print(dzielenie("5", 2)) # Nieprawidłowy typ danych
