class Samochod:
    def __init__(self, marka):
        self._marka = marka  # Atrybut chroniony

        print(self._marka)

class SportowySamochod(Samochod):
    def __init__(self, marka, model):
        super().__init__(marka)
        self.model = model
        print("Marka:", self._marka)  # Dostęp do atrybutu chronionego

auto = SportowySamochod("Toyota", "Supra")
print(auto._marka)
print(auto.model)

auto1 = Samochod("Audi")
print(auto1._marka)