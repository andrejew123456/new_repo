#funkcja range() simple

# for i in range(5):
#     print(i)
# Wynik: 0, 1, 2, 3, 4

#funkcja range z punktem startu i zakończenia
# for i in range(2, 6):
#     print(i)
# Wynik: 2, 3, 4, 5

#funkcja range() z start, stop i step
# for i in range(0, 10, 2):
#     print(i)
# Wynik: 0, 2, 4, 6, 8

my_list = ['apple', 'banana', 'orange']

for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")
