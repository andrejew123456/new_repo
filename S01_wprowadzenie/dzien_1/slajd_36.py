#krotka
tuple = (1, 2,3,4)
len(tuple)

# tuple[4] = 0


### Mutowalnosc  ###

immutable = (1, 2, 3)  # Krotka, niemutowalna
mutable = [1, 2, 3]	# Lista, modyfikowalna
mutable[0] = 100   	# Zmiana zawartości listy


l = ["Ala", " ", "ma", " ", "kota"]
tl = ("Ala", " ", "ma", " ", "psa", " ", "w", " ", "tupli")
print(l)
print(tl)
print("$".join(l))

txt = "#Ala #ma #kota"
print(txt.split("#"))