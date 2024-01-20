class Samochod:

    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
    @classmethod
    def z_napedem_hybrydowym(cls, model):
        return cls("Toyota", model)

    def wyswietl_info(self):
        return f"Samochód marki {self.marka}, model {self.model}"

# Użycie metody klasy
hybrydowy = Samochod.z_napedem_hybrydowym("Prius")
print(hybrydowy.wyswietl_info())
