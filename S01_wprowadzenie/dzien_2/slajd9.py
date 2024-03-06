class SharedData:
    spam = 42           #Wygenerowanie atrybutu danych klasy

x = SharedData()        #Utworzenie dwóch instancji
y = SharedData()

print(x.spam, y.spam)    #dziedzicza i współdzielą zmienną spam
SharedData.spam = 99     #przypisanie zmiennej spam za pośrednictwem klasy
print(x.spam, y.spam, SharedData.spam)

x.spam = 88             #przypisanie zmiennej spam za pośrednictwem instancji zamiast klasy
print(x.spam, y.spam, SharedData.spam)

