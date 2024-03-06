class Animal:
   def __init__(self, age, name):
       self.age = age
       self.name = name
       print('Animal!')

   def increase_age(self):
       print('increase_age!')

#///////////////////////////////
#
# class Mammal(Animal):
#    def __init__(self):
#        Animal.__init__(self)
#        print('Mammal!')
#
#    def introduce_yourself(self):
#        print('introduce_yourself!')
#
#
# class Cat(Mammal):
#    def __init__(self, age, name):
#        Mammal.__init__(self)
#        print('Cat!')
#
#    def purr(self):
#        print('purr!')

 #OK!!!!!!!!!!!!

class Mammal(Animal):
   def __init__(self, age, name):
       Animal.__init__(self, age, name)
       print('Mammal!')

   def introduce_yourself(self):
       print(f'introduce_yourself! {self.name}')


class Cat(Mammal):
   def __init__(self, age, name):
       Mammal.__init__(self, age, name)
       print('Cat!')

   def purr(self):
       print('purr!')


# mammal_1 = Mammal()
# mammal_1.introduce_yourself()
# mammal_1.increase_age()

print('-')

cat_1 = Cat(2, "Pablo")
cat_1.introduce_yourself()
cat_1.purr()
cat_1.increase_age()