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
   def __init__(self, age, name):
       Mammal.__init__(self, age, name)
       print('Cat!')

   def purr(self):
       print('purr!')


cat_1 = Cat(2, 'Pablo')
cat_1.introduce_yourself()
cat_1.purr()
cat_1.increase_age()