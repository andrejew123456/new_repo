wiek = 20
ma_prawo_jazdy = True

if wiek >= 18:
    if ma_prawo_jazdy:
        print("Możesz prowadzić samochód.")
    else:
        print("Nie masz prawa jazdy.")
else:
    print("Nie jesteś pełnoletni.")
