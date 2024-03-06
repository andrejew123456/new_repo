class Animal:
   def __init__(self):
       print('Animal!')

   def increase_age(self):
       print('increase_age!')


class Mammal(Animal):
   def __init__(self):
       Animal.__init__(self)
       print('Mammal!')

   def introduce_yourself(self):
       print('introduce_yourself!')


mammal_1 = Mammal()
mammal_1.introduce_yourself()
mammal_1.increase_age()