# listy
L1 = [1, ('a', 3)]
L2 = [1, ('a', 3)]
L1 == L2   #>>>  True
L1 is L2  #>>>  False

# string - krótki
S1 = 'mielonka'
S2 = 'mielonka'
S1 == S2   #>>> True
S1 is S2   #>>> True

# string - długi
S1 = "dluzszy lancuch znakow"
S2 = "dluzszy lancuch znakow"
S1 == S2  #>>> True
S1 is S2  #>>> False
