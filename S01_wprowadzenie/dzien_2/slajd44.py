### Obsluga wyjatkow: else i finally   ####

def wczytaj_liczbe():
    try:
        liczba = int(input("Podaj liczbę: "))
    except ValueError:
        print("To nie jest prawidłowa liczba.")
    else:
        print(f"Wprowadzono liczbę: {liczba}")
        # Tutaj możemy wykonać dodatkowe operacje związane z liczbą
    finally:
        print("Koniec próby wczytania liczby.")

wczytaj_liczbe()
