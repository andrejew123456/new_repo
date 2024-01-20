"""
Stwórz klasę Pojazd, która będzie reprezentować ogólne cechy pojazdu. Klasa ta powinna zawierać:
-Atrybuty klasy
    liczba_kol (domyślnie 4)
-Konstruktor (__init__), który przyjmuje:
    marka (marka pojazdu, np. "Toyota")
    model (model pojazdu, np. "Corolla")
    rok_produkcji (rok produkcji pojazdu)
-Metodę instancji wyswietl_info, która wyświetla informacje o pojeździe w formacie: "Marka: [marka], Model: [model], Rok produkcji: [rok_produkcji], Liczba kół: [liczba_kol]".

"""

#####ROZWIAZANIE



class Pojazd:
    liczba_kol = 4

    def __init__(self, marka, model, rok_produkcji):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji

    def wyswietl_info(self):
        print(
            f"Marka: {self.marka}, Model: {self.model}, Rok produkcji: {self.rok_produkcji}, Liczba kół: {Pojazd.liczba_kol}")


moj_pojazd = Pojazd("Toyota", "Corolla", 2020)
moj_pojazd.wyswietl_info()

nowy_pojazd = Pojazd("Ford", "Focus", 2021)
nowy_pojazd.wyswietl_info()

Pojazd.wyswietl_info(moj_pojazd)
