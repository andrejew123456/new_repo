ciag_znakow = "Python"
odwrocony_ciag = ""

# Iterowanie przez string od końca i dodawanie każdego znaku do nowego stringa
for znak in ciag_znakow[::-1]:
    odwrocony_ciag += znak

print(odwrocony_ciag)



"""Tutaj używam wycinania ciągów (slicing) z krokiem -1, aby przejść przez ciąg znaków w odwrotnej kolejności, a następnie konkatenuję każdy znak do nowego ciągu znaków, tworząc odwróconą wersję oryginalnego ciągu.

Każdy z tych programów demonstruje różne sposoby wykorzystania pętli for w Pythonie, co jest przydatne w różnych scenariuszach programowania.

"""