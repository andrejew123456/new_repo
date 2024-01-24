"""
1. Napisz program, który wyświetla każdy drugi element z listy owoców.

2.Utwórz pętlę, która iteruje przez krotkę zawierającą różne typy danych (liczby, stringi, inne listy) i wyświetla ich typ
"""

#1
fruits = ['apple', 'pear', 'orange', 'banana', 'grape', 'mango', 'limon']

for i in range(1, len(fruits), 2):
    print(fruits[i])


#2
different_types = (123, "Python", [1, 2, 3], 45.67, {"jabłko", "banan"})

# Iterowanie przez krotkę i wyświetlanie typu każdego elementu
for element in different_types:
    print(type(element))
