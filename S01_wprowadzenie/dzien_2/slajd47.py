###   Przyklad zastosowania wlasnych wyjatkow   ###

class BrakDanych(Exception):
    """Wyjątek rzucany, gdy brakuje niezbędnych danych."""

def oblicz_srednia(oceny):
    if not oceny:
        raise BrakDanych("Lista ocen jest pusta.")
    return sum(oceny) / len(oceny)

# Przykładowe wywołanie funkcji
try:
    srednia = oblicz_srednia([])
except BrakDanych as e:
    print(e)
