## ZADANIE DOMOWE ###
# Opis Zadania:
# Stwórz grę, w której użytkownik musi odgadnąć losowo wygenerowany numer. Użytkownik ma ograniczoną liczbę prób. Po każdej próbie, program powinien informować, czy podana liczba jest za duża, za mała, czy prawidłowa. Jeśli użytkownik nie odgadnie liczby w wyznaczonej liczbie prób, gra kończy się porażką.
#
# Krok 1: Importowanie Modułu i Inicjalizacja Zmiennych
# Importuj moduł random do wygenerowania losowego numeru i zdefiniuj zmienne.

# Krok 2: Pętla while dla Gry
# Użyj pętli while do przetwarzania prób użytkownika.
#
# Krok 3: Sprawdzenie Warunku Zakończenia Gry
# Jeśli użytkownik nie zgadnie liczby w wyznaczonej liczbie prób, gra kończy się.

import random

# Krok 1: Importowanie Modułu i Inicjalizacja Zmiennych

# Wygeneruj losowy numer od 1 do 100
szukana_liczba = random.randint(1, 100)

# Maksymalna liczba prób
max_proby = 5
liczba_prob = 0


# Krok 2: Pętla while dla Gry
while liczba_prob < max_proby:
    # Prośba o wprowadzenie liczby przez użytkownika
    zgadnij = int(input("Zgadnij liczbę od 1 do 100: "))
    liczba_prob += 1

    # Sprawdzenie liczby i wyświetlenie odpowiedniego komunikatu
    if zgadnij < szukana_liczba:
        print("Za mało!")
    elif zgadnij > szukana_liczba:
        print("Za dużo!")
    else:
        print(f"Gratulacje! Zgadłeś liczbę po {liczba_prob} próbach.")
        break

# Krok 3: Sprawdzenie Warunku Zakończenia Gry
if zgadnij != szukana_liczba:
    print(f"Niestety, nie zgadłeś. Szukana liczba to {szukana_liczba}.")
