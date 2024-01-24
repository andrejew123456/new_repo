s = "Hello world!"

print(s[1])  #drugi element od początku
print(s[-1])  #pierwszy element od końca


#slicing:
print(s[1:4])

print(s[1:])    #Wszystko poza pierwszym znakiem
print(s[0:len(s)-1]) #Wszystkie elementy poza ostatnim -1

print(s[:12])   #To samo co s[0:12]

print(s[:-1])   #Wszystkie elemnty bez ostatniego

print(s[:])     #Całość s[0:len(s)]

