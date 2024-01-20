class MixedNames:               #Zdefiniowanie klasy
    data = "mielonka"           #przypisanie atrybutu klasy
    def __init__(self, value):  #przypisanie nazwy metody
        self.data = value       #przypisanie atrybutu instancji
    def dispaly(self):
        print(self.data, MixedNames.data)   #Atrybut instancji, atrybut klasy

x = MixedNames(1)               #Utworzenie dwóch obiektów instancji
y=MixedNames(2)                 #Każdy ma własne dane
print(x.dispaly(), y.dispaly())