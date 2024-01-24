l = [1,'e',2, 'e']  #pusta lista
l2 =[0,1,2,3]    #cztery elementy listy
l = ['abc', ['def', 'ghi']]     #zagniezdzone podlisty
l = list('mielonka')    #lista elementow obiektu iterowanego
l = list(range(-4, 4))     #lista kolejnych liczb calkowitych
l[1]        #indeks
l[1][1]     #indeks indeksu
l[1:5]      #slice
len(l)      #dlugosc listy
l + l2      #konkatenacja
l * l2      #powtorzenie
l.append(4) #dodawanie elemntow
l.extend([5,6,7])   #dodawania elementow
l.insert(1, 'kot') #dodawanai elementow
l.index('e')  #przeszukanie listy po wartosci
l.count(1) #liczenie elementow 1
l.sort()    #sortowanie
l.reverse() #odwrocenie listy
del l[1]     #usuniecie elementu z listy spod indeksu 1, mozna usuwac slice
l.pop()     #usuniecie elementu z listy spod indeksu
l.remove('e')   #usuwanie elementow po wartosci
l[3] = []       #przypisanie do indeksu
print()