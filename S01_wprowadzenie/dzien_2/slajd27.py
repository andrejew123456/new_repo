####   ROZWIĄZANIE   ######

"""
Krok 1: Stwórz Klasę Bazową Publikacja
Stwórz klasę Publikacja, która będzie zawierała wspólne atrybuty dla książek i czasopism, takie jak tytuł i autor/autorzy.
"""

class Publikacja:
    def __init__(self, tytul, autorzy):
        self.tytul = tytul
        self.autorzy = autorzy

    def pokaz_info(self):
        return f"Tytuł: {self.tytul}, Autorzy: {self.autorzy}"


"""
Krok 2: Stwórz Klasy Pochodne Ksiazka i Czasopismo
Klasy Ksiazka i Czasopismo będą dziedziczyć z klasy Publikacja i będą miały dodatkowe specyficzne atrybuty.
"""

class Ksiazka(Publikacja):
    def __init__(self, tytul, autorzy, liczba_stron):
        super().__init__(tytul, autorzy)
        self.liczba_stron = liczba_stron

    def pokaz_info(self):
        return f"{super().pokaz_info()}, Liczba stron: {self.liczba_stron}"

class Czasopismo(Publikacja):
    def __init__(self, tytul, autorzy, numer_wydania):
        super().__init__(tytul, autorzy)
        self.numer_wydania = numer_wydania

    def pokaz_info(self):
        return f"{super().pokaz_info()}, Numer wydania: {self.numer_wydania}"


"""
Krok 3: Testowanie Klas
Stwórz obiekty dla każdej klasy i przetestuj ich działanie.
"""

# Tworzenie obiektów
ksiazka = Ksiazka("Władca Pierścieni", "J.R.R. Tolkien", 1178)
czasopismo = Czasopismo("National Geographic", "Różni Autorzy", 202)

# Testowanie metod
print(ksiazka.pokaz_info())
print(czasopismo.pokaz_info())
