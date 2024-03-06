"""Opis Zadania:
Napisz program, który analizuje oceny uczniów zapisane w słowniku.
Dla każdego ucznia, program powinien określić kwalifikację na podstawie średniej oceny.
"""

# Krok 1: Przygotowanie Danych
# Zdefiniuj słownik zawierający nazwiska uczniów i listy ich ocen.

# Krok 2: Analiza Oceny i Przypisanie Kwalifikacji
# Użyj pętli for do iteracji przez słownik i instrukcji warunkowych do przypisania kwalifikacji.

# Krok 3: Wyświetlenie Wyników
# Wyświetl kwalifikację każdego ucznia.

oceny_uczniow = {
    "Anna Kowalska": [4, 3, 5, 4],
    "Jan Nowak": [5, 5, 4, 5],
    "Paweł Wiśniewski": [2, 3, 3, 2],
    "Zofia Baranowska": [5, 5, 5, 5]
}

# Krok 2: Analiza Oceny i Przypisanie Kwalifikacji
kwalifikacje = {}

for uczen, lista_ocen in oceny_uczniow.items():
    srednia = sum(lista_ocen) / len(lista_ocen)

    if srednia >= 4.75:
        kwalifikacje[uczen] = "Bardzo Dobry"
    elif srednia >= 4:
        kwalifikacje[uczen] = "Dobry"
    elif srednia >= 3:
        kwalifikacje[uczen] = "Dostateczny"
    else:
        kwalifikacje[uczen] = "Niedostateczny"

# Krok 3: Wyświetlenie Wyników
for uczen, kwalifikacja in kwalifikacje.items():
    print(f"{uczen}: {kwalifikacja}")
