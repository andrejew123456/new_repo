class Animal:
   def __init__(self, age, name):
       self.age = age
       self.name = name
       print('Animal!')

   def increase_age(self):
       print('increase_age!')


class Mammal(Animal):
   def __init__(self, age, name):
       Animal.__init__(self, age, name)
       print('Mammal!')

   def introduce_yourself(self):
       print(f'My name is {self.name}')


class Cat(Mammal):
   def __init__(self, age, name, master):
       Mammal.__init__(self, age, name)
       self.master = master
       print('Cat!')

   def purr(self):
       print('purr!')

   def introduce_yourself(self):
       print(f'My name is {self.name} and my master is {self.master}')

cat_1 = Cat(2, 'Pablo', 'Bob')
cat_1.introduce_yourself()
cat_1.purr()
cat_1.increase_age()

mammal_1 = Mammal(10, 'Nemon')
mammal_1.introduce_yourself()





#/////////////////////////////////////

#
#
# class Pojazd:
#     def __init__(self, nazwa, max_predkosc):
#         self.nazwa = nazwa
#         self.max_predkosc = max_predkosc
#     def wyswietl_info(self):
#         return f"{self.nazwa}, Max prędkość: {self.max_predkosc}"
#
#
# class Samochod(Pojazd):
#     def __init__(self, nazwa, max_predkosc, liczba_drzwi):
#         super().__init__(nazwa, max_predkosc)
#         self.liczba_drzwi = liczba_drzwi
#
#     # def wyswietl_info(self):
#     #     return f"{self.nazwa}, Max prędkość: {self.max_predkosc}, Drzwi: {self.liczba_drzwi}"
#
#
# poj = Pojazd("Opel", 200)
# print(poj.nazwa, poj.max_predkosc)
# print(poj.wyswietl_info())
#
# sam = Samochod("Cupra", 310, 4)
# print(sam.wyswietl_info())