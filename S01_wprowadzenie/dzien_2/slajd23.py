class Pojazd:
    def __init__(self, nazwa, max_predkosc):
        self.nazwa = nazwa
        self.max_predkosc = max_predkosc

class Samochod(Pojazd):
    def liczba_kol(self):
        print("Ma 4 koła")

class Motocykl(Pojazd):
    def liczba_kol(self):
        print("Ma cztery koła")


samochod = Samochod("Opel", 200)
motocykl = Motocykl("Suzuki", 300)

print(samochod.nazwa)
print(samochod.max_predkosc)
samochod.liczba_kol()

print(motocykl.nazwa)
print(motocykl.max_predkosc)
motocykl.liczba_kol()
