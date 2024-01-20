###   GETTERY i SETTERY   ####

class Osoba:
    def __init__(self, imie, wiek):
        self.imie = imie
        self._wiek = wiek

    @property
    def wiek(self):
        return self._wiek

    @wiek.setter
    def wiek(self, nowy_wiek):
        if nowy_wiek > 0:
            self._wiek = nowy_wiek
        else:
            raise ValueError("Wiek musi być wartością dodatnią")

# Użycie klasy
osoba = Osoba("Jan", 30)
print(osoba.wiek)  # 30
osoba.wiek = 35   # poprawne ustawienie wieku
print(osoba.wiek)  # 35
osoba.wiek = -5   # wywoła wyjątek ValueError