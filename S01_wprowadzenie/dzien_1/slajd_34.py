"""Kontrola przepływu"""

# Użycie break
while True:
    odpowiedz = input("Wpisz 'exit', aby wyjść: ")
    if odpowiedz == "exit":
        break


# Użycie continue
for liczba in range(10):
    if liczba % 2 == 0:
        continue
    print(liczba)
