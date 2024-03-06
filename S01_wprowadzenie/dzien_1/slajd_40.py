D = {}                              # pusty słownik
D2 = {"mielonka": 2, "jajka": 3}     #słownik dwuelementowy
D = {"abc": {"def": 1, "ghi": 2}}   # zagnieżdżenie
D = dict(name = "Bob", age=40)      #technika konstruowania słownika
# D = dict(zip(keylist, valslist))    #zzipowane pary kluczy
D=dict.fromkeys(["a", "b"], 0)         #przypisanie klucza a i b do wartości 0
D["jajka"]                          #indeksowanie po kluczu
D["jedzenie"]["szynka"]             #indeks indeksu
"jajka" in D                        #sprawdzenie przynaleznosci
D.keys()                            #lista kluczy
D.values()                          #lista wartosci
D.items()                           #lista kluczy i wartiosci
D.copy                              #kopia obiektu
D.update(D2)                        #dodanie
D.pop("key")                          #usuwanie klucza
len(D)                              #dlugosc slownika
D["key"]  = 42                        #przypisanie wartosci do klucza
del D["key"]                        #usuniecie klucza
list(D.keys())                      #lista kluczy
