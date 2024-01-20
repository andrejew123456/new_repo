#Wprowadzenie do programowania obiektowego

#Klasa
class Samochod:
    def __init__(self, rok, marka=None, model="Astra"):
        self.rok = rok
        self.marka = marka
        self.model = model

    def wyswietl_info(self):
        return f"Samochód: {self.marka} {self.model} {self.rok}"


#obiekt
moj_samochod = Samochod(1999)
twoj_samochod = Samochod(2000,"Toyota", "Corolla")

print(moj_samochod.rok, moj_samochod.model)
print(twoj_samochod.rok, twoj_samochod.model)
print(moj_samochod.wyswietl_info())