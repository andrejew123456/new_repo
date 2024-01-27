class Samochod:
    def __init__(self, marka):
        self.__marka = marka  # Atrybut prywatny

    def pokaz_marke(self):
        return self.__marka

samochod = Samochod("Toyota")
print(samochod.pokaz_marke())  # Dostęp przez metodę klasy
print(samochod.__marka) # Błąd: atrybut nie jest dostępny z zewnątrz
# print(samochod._Samochod__marka)  #Dostanie sie do prywatnego atrybutu przez obj._ClassName__atrybut