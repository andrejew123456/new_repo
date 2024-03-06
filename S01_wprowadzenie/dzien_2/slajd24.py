"""Uzupełnić metodę def increase_age(self):, aby po jej wywołaniu:
zwiększała się wartość zmiennej self.age o jeden,
na konsoli wypisywany był napis z informacją o imieniu i wieku (czyli ile dany obiekt ma lat 😉 ).
Bazując na klasie Cat napisać klasę Dog, która:
    będzie dziedziczyła po klasie Mammal,
    będzie posiadała pole master, które będzie ustawiane w konstruktorze (analogicznie do klasy Cat),
    będzie posiadała pole favourite_toy, które będzie ustawiane w konstruktorze (analogicznie do pola master),
    będzie posiadała metodę def introduce_yourself(self):, w której kolejno:
wywołana zostanie metoda introduce_yourself z klasy bazowej,
na konsoli wypisywany zostanie napis z informacją o imieniu pana (czyli mastera),
na konsoli wypisywany zostanie napis z informacją o ulubionej zabawce, czyli wartością zmiennej favourite_toy.
Dla uproszczenia przygotuj rozwiązanie w jednym pliku, możesz do tego celu przygotować plik typu scratches,
Przetestuj rozwiązanie w analogiczny sposób do wcześniej prezentowanych, czyli dodając na końcu skryptu kod podobny do testów klasy Cat:
cat_1 = Cat(2, 'Garfield', 'Bob')
cat_1.introduce_yourself()
cat_1.purr()
cat_1.increase_age()
tylko, że dla instancji obiektu typu Dog wywołując kolejno:

Inicjalizację obiektu dog_1,
Wywołanie metody introduce_yourself,
Wywołanie metody increase_age.
"""


class Animal:
   def __init__(self, age, name):
       print('Animal!')
       self.age = age
       self.name = name

   def increase_age(self):
       self.age = self.age + 1
       print(f'{self.name} is {self.age} years old!')


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
       super().introduce_yourself()
       print(f'My master is {self.master}')

class Dog(Mammal):
   def __init__(self, age, name, master, favourite_toy):
       Mammal.__init__(self, age, name)
       self.master = master
       self.favourite_toy = favourite_toy
       print('Dog!')

   def introduce_yourself(self):
       super().introduce_yourself()
       print(f'My master is {self.master}')
       print(f'My favourite toy is {self.favourite_toy}')


cat_1 = Cat(2, 'Garfield', 'Bob')
cat_1.introduce_yourself()
cat_1.purr()
cat_1.increase_age()

print('-')

dog_1 = Dog(4, 'Lassie', 'Bob', 'Red Ball')
dog_1.introduce_yourself()
dog_1.increase_age()