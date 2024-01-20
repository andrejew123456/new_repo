class Pojazd:
    def __init__(self, nazwa, max_predkosc):
        self.nazwa = nazwa
        self.max_predkosc = max_predkosc
    def wyswietl_info(self):
        return f"{self.nazwa}, Max prędkość: {self.max_predkosc}"


class Samochod(Pojazd):
    def __init__(self, nazwa, max_predkosc, liczba_drzwi):
        super().__init__(nazwa, max_predkosc)
        self.liczba_drzwi = liczba_drzwi

    # def wyswietl_info(self):
    #     return f"{self.nazwa}, Max prędkość: {self.max_predkosc}, Drzwi: {self.liczba_drzwi}"


poj = Pojazd("Opel", 200)
print(poj.nazwa, poj.max_predkosc)
print(poj.wyswietl_info())

sam = Samochod("Cupra", 310, 4)
print(sam.wyswietl_info())