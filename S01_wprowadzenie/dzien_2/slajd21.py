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


class Cat(Mammal):
   def __init__(self):
       Mammal.__init__(self)
       print('Cat!')

   def purr(self):
       print('purr!')


mammal_1 = Mammal()
mammal_1.introduce_yourself()
mammal_1.increase_age()

print('-')

cat_1 = Cat()
cat_1.introduce_yourself()
cat_1.purr()
cat_1.increase_age()