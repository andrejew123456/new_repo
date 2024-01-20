"""Zadanie 1: System Rezerwacji Pokoi Hotelowych
Opis:
Stwórz kilka klas: Hotel, Pokój, i Gosc. Klasa Hotel powinna zawierać listę pokojów i metody do rezerwacji.
Klasa Pokoj powinna przechowywać informacje o dostępności, numerze pokoju i cenie.
Klasa Gość powinna przechowywać dane o gościach.
"""

class Pokoj:
    def __init__(self, numer, cena):
        self.numer = numer
        self.cena = cena
        self.dostepny = True


class Gosc:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

class Hotel:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        self.pokoje = []

    def dodaj_pokoj(self, pokoj):
        self.pokoje.append(pokoj)

    def rezerwuj_pokoj(self, gosc, numer_pokoju):
        for pokoj in self.pokoje:
            if pokoj.numer == numer_pokoju and pokoj.dostepny:
                pokoj.dostepny = False
                return f"Pokój {numer_pokoju} został zarezerwowany przez {gosc.imie} {gosc.nazwisko}"
        return "Pokój nie jest dostępny."



# Tworzenie hotelu i pokoi
hotel = Hotel("Hotel Centralny")
hotel.dodaj_pokoj(Pokoj(101, 200))
hotel.dodaj_pokoj(Pokoj(102, 250))

# Tworzenie gościa
gosc = Gosc("Jan", "Kowalski")

# Rezerwacja pokoju
wynik_rezerwacji = hotel.rezerwuj_pokoj(gosc, 101)
print(wynik_rezerwacji)

# Próba rezerwacji tego samego pokoju
wynik_rezerwacji = hotel.rezerwuj_pokoj(gosc, 101)
print(wynik_rezerwacji)
