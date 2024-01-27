#ValueError
int("xyz")

#IOError
with open("nieistniejacy_plik.txt") as f:
    content = f.read()