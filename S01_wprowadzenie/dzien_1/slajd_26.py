tekst = "Python jest super!"

# Wyszukiwanie w tekście
szukaj = "Python"
pozycja = tekst.find(szukaj)
print(f"'{szukaj}' znajduje się na pozycji: {pozycja}")

# Podmiana w tekście
tekst_zmieniony = tekst.replace("super", "wspaniały")
print(tekst_zmieniony)
