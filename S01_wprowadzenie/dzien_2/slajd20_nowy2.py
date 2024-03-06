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

dog = Mammal()
dog.increase_age()



# ///////////////////////////////////////////////////
# class Animal:
#    def __init__(self):
#        print('Animal!')
#        self.some_value = 1
#
#    def increase_age(self):
#        print('increase_age!')
#
#
# class Mammal(Animal):
#    def __init__(self):
#        print('Mammal!')
#        print(self.some_value)
#
#    def introduce_yourself(self):
#        print('introduce_yourself!')
#
#
# mammal_1 = Mammal()