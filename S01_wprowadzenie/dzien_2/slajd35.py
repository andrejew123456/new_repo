###   ROZWIAZANIE   ###
"""
Zadanie
Stwórz dekorator, który będzie mierzył i wyświetlał czas wykonania dowolnej funkcji. Dekorator ten może być używany do monitorowania wydajności różnych części kodu.
"""

"""Krok 1: Definicja Dekoratora
Stwórz funkcję dekoratora, która przyjmuje funkcję jako argument i zwraca nową funkcję, która mierzy czas wykonania oryginalnej funkcji.
"""
import time
def measuretime(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Time needed: {end - start} seconds")
    return wrapper

"""Krok 2: Użycie Dekoratora
Użyj dekoratora measuretime do zmierzenia czasu wykonania przykładowej funkcji.
"""
@measuretime
def wastetime():
    sum([i**2 for i in range(1000000)])

@measuretime
def suma(a, b):
    return a + b

@measuretime
def sleep(sec):
    time.sleep(sec)

wastetime()
sleep(20)
