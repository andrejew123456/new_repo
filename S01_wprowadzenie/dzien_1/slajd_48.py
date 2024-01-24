### ZADANIE  ###
"""
Stwórz program, który na podstawie temperatury wprowadzonej przez użytkownika (input) poda komentarz, czy jest zimno, ciepło, czy gorąco (użyj zagnieżdżonych instrukcji warunkowych).
"""
# Pobranie temperatury od użytkownika i konwersja na liczbę całkowitą
temperatura = int(input("Podaj temperaturę w stopniach Celsjusza: "))

# Zagnieżdżone instrukcje warunkowe
if temperatura < 10:
    print("Jest zimno!")
elif temperatura >= 10:
    if temperatura < 25:
        print("Jest ciepło.")
    else:
        print("Jest gorąco!")