class SharedData:
    spam = 42           #Wygenerowanie atrybutu danych klasy

x = SharedData()        #Utworzenie dwóch instancji
y = SharedData()

print(x.spam, y.spam)    #dziedzicza i współdzielą zmienną spam
SharedData.spam = 99
print(x.spam, y.spam, SharedData.spam)

x.spam = 88
print(x.spam, y.spam, SharedData.spam)
