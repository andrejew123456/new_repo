class Samochod:
    @staticmethod
    def czy_naped_hybrydowy(jest_hybrydowy):
        return "Hybrydowy" if jest_hybrydowy else "Niehybrydowy"

# Użycie metody statycznej
print(Samochod.czy_naped_hybrydowy(True))
