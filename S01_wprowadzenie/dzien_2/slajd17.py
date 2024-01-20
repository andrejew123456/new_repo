class NextClass:                    #Zdefiniowanie klasy
    def printer(self, text):        #Zdefiniowanie metody
        self.message = text         #Modyfikacja instancji
        print(self.message)         #Dostęp do instancji


x = NextClass()                     #Utworzenie instancji
x.printer("wywołanie instancji")    #Wywołanie tej metody
x.message                           #Modyfikacja instancji



NextClass.printer(x, "wywołanie klasy") #Bezposrednie wywolanie klasy
x.message                                   #Ponowna modyfikacja instancji

