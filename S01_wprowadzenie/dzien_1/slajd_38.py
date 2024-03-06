###   ROZWIAZANIE  ###
substancje = ["woda", "etanol", "kwas siarkowy", "woda", "chlor", "etanol"]

liczba_substancji = len(substancje)
print(liczba_substancji)
substancje.sort()
print(substancje)
substancje.append("azot")
substancje.extend(["kwas mlekowy", "siarka"])
print(substancje)