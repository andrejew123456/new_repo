#Wprowadzenie do programowania obiektowego

#Klasa
class Samochod:
    def __init__(self, marka, model):
        self.marka = marka
        self.model = model

    def wyswietl_info(self):
        return f"Samochód: {self.marka} {self.model}"


#obiekt
moj_samochod = Samochod("Toyota", "Corolla")
print(moj_samochod.wyswietl_info())