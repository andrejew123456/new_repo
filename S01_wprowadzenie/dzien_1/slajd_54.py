#zastosowanie range()
def testuj_funkcje(n):
    return n * n

# Testowanie funkcji z różnymi wartościami
for n in range(1, 5):
    wynik = testuj_funkcje(n)
    print(f"Test dla n={n}: {wynik}")

def symuluj_klikniecie(i):
    print( i * "CLICK ")
    
# Iteracja przez liczby do symulacji
for i in range(3):
    symuluj_klikniecie(i)
