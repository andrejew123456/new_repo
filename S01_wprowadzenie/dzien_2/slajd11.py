#Wprowadzenie do programowania obiektowego

#Klasa
# class Samochod:
#     def __init__(self, marka, model):
#         self.marka = marka
#         self.model = model
#
#     def wyswietl_info(self):
#         return f"Samochód: {self.marka} {self.model}"
#
#
# #obiekt
# moj_samochod = Samochod("Toyota", "Corolla")
# print(moj_samochod.wyswietl_info())


#///////////////////////////////////////

class Human:
   def __init__(self, name):
       self.name = name
       print(f'New Human was born! His name is {self.name}')

   def speak(self):
       print(f'I can speak! My name is  {self.name}')

class Animal:
   def speak(self):
       print('I can not speak!')

# Class usage examples
print("Let's create Adam!")
adam = Human()

print("Let's create a dog!")
dog = Animal()

print('Now all speak!')
adam.speak()
dog.speak()


#///////////////////////

# class Human:
#    def __init__(self, name):
#        self.name = name
#        print(f'New Human was born! His name is {self.name}!')
#
#    def speak(self):
#        print(f'I can speak! My name is {self.name}!')
#
# class Animal:
#    def speak(self):
#        print('I can not speak!')
#
# print("Let's create Adam!")
# adam = Human('Adam')
# print("Let's create a dog!")
# dog = Animal()
# print('Now all speak!')
# adam.speak()
# dog.speak()