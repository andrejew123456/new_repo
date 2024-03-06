####   Tworzenie własnych wyjątków   ###
class NieprawidlowaWartosc(Exception):
    """Wyjątek rzucany, gdy wartość nie spełnia oczekiwań."""
    pass

def ustaw_wiek(wiek):
    if wiek < 0:
        raise NieprawidlowaWartosc("Wiek nie może być wartością ujemną.")
    print(f"Wiek ustawiony na {wiek}.")

# Przykładowe wywołanie funkcji
try:
    ustaw_wiek(-5)
except NieprawidlowaWartosc as e:
    print(e)

