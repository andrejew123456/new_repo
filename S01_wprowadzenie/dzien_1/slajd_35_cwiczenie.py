""""1. Napisz program, który używa pętli while do czytania liczby od użytkownika,
a następnie sumuje te liczby do czasu wprowadzenia '0', po czym zakończy działanie."""


def wykonaj_test():
    # Tutaj umieść logikę wykonującą test, która zwraca status testu
    # Na przykład, zwróć 'sukces', 'niepowodzenie' lub 'błąd'
    # Poniżej znajduje się przykładowa implementacja
    import random
    wyniki = ['sukces', 'niepowodzenie', 'błąd']
    return random.choice(wyniki)

# Główna pętla wykonująca testy
while True:
    wynik = wykonaj_test()
    print(f"Wynik testu: {wynik}")
    if wynik == 'błąd':
        print("Napotkano błąd, zatrzymywanie testów.")
        break




"""2. Utwórz pętlę, która przetwarza dane wejściowe od użytkownika 
i kontynuuje działanie do momentu wprowadzenia określonego słowa kluczowego"""


# Ustaw słowo kluczowe, które zakończy działanie pętli
słowo_kluczowe = "exit"

print("Wpisz 'exit', aby zakończyć.")

while True:
    dane_wejsciowe = input("Wprowadź dane: ")
    if dane_wejsciowe.lower() == słowo_kluczowe:
        print("Słowo kluczowe wprowadzone, zatrzymywanie programu.")
        break
    else:
        print(f"Otrzymano dane: {dane_wejsciowe}")
