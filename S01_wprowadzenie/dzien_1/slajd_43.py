### Pliki ###
# myfile = open('myfile.txt', 'w') 	#Otwarcie do zapisu tekstowego
# myfile.write('witaj pliku tekstowy\n')  #   21  #Zapisanie wiersza tekstu
# myfile.close() 	#Zrzucenie bufora wyjściowego na dysk
# myfile = open('myfile.txt')  	#Otwarcie pliku
# myfile.readline()   #   'witaj pliku tekstowy\n'  #Wczytywanie wierszy
# myfile.readline()  #   ''  	#Pusty łańcuch znaków - koniec pliku


#do odczytu
# with open('dziennik_lab.txt') as file:
#     print(file.readline(10))
# #do odczytu
# with open('dziennik_lab.txt') as file:
#     print(file.read())
# #
# # #tryb dopisywania
# with open('dziennik_lab.txt', "a") as file:
#     print(file.write("nowy test 03.03 \n"))


# czytanie pliku wiersz po wierszu:

# for line in open('myfile.txt'):
#     print(line, end='')


"""

Opis:
W ramach tego zadania będziesz pracować z plikiem tekstowym, który reprezentuje dziennik laboratoryjny. Każda linia w pliku zawiera wpis z datą, nazwą eksperymentu i wynikami. Twoim zadaniem jest przetworzenie tego pliku w celu uzyskania i zapisania konkretnych informacji.
Zadania do wykonania:
Odczytanie i Wyświetlenie Zawartości Pliku: Otwórz plik i wydrukuj jego zawartość.
Dopisanie nowego eksperymentu do istniejącego pliku
Wskazówki:
Do odczytania pliku użyj with open(...) as file:

with open('dziennik_lab.txt') as file:
    print(file.read())
"""








#
# file = open('nowy_plik.txt')
# # new_file  = file.read()
# print(file.write("No hej 1111"))
# file.close()
# print(f"Is file closed?: {file.closed}")

with open('kursy.txt') as file:
    print(file.write())