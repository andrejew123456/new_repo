## Rozwiązanie  ###

pracownicy = {
    "001": {"imię": "Jan", "nazwisko": "Kowalski", "stanowisko": "Programista", "rok_zatrudnienia": 2018},
    "002": {"imię": "Anna", "nazwisko": "Nowak", "stanowisko": "Analityk", "rok_zatrudnienia": 2020},
    "003": {"imię": "Marek", "nazwisko": "Wiśniewski", "stanowisko": "Tester", "rok_zatrudnienia": 2019}
}

# Dodanie Nowego Pracownika: Dodaj nowego pracownika do słownika. Na przykład, pracownika o ID "004" z odpowiednimi danymi osobowymi.

D2 = {"004": {"imię": "Karol", "nazwisko": "Wiśniewski", "stanowisko": "Tester", "rok_zatrudnienia": 2019}}
pracownicy.update(D2)

# drugi sposob:
pracownicy["005"] = {"imię": "Bartosz", "nazwisko": "Wiśniewski", "stanowisko": "Tester", "rok_zatrudnienia": 2019}


# Usunięcie Pracownika: Usuń pracownika z bazy danych. Na przykład, pracownika o ID "002".
pracownicy.pop("002")

# Aktualizacja Danych Pracownika: Zaktualizuj dane jednego z pracowników. Na przykład, zmień stanowisko pracownika o ID "001" na "Starszy Programista"
pracownicy["001"]["stanowisko"] = "starszy programista"
