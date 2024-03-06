### append  ###
L = ['najsmaczniejsza', 'jest', 'MIELONKA!']
L.append('puszkowana')
L >>  ['najsmaczniejsza', 'jest', 'MIELONKA!', 'puszkowana' ]



### sort () ###
L = ['abc', 'ABD', 'aBe']
L.sort()  >> ['ABD', 'aBe', 'abc']
L.sort(key=str.lower)
L   >>   ['abc', 'ABD', 'aBe']
L.sort(key=str.lower, reverse=True)
L   >>  ['aBe', 'ABD', 'abc']


### sorted()
L = ['abc', 'ABD', 'aBe']
sorted(L)  >> ['ABD', 'aBe', 'abc']
sorted(L, key=str.lower)  >> ['abc', 'ABD', 'aBe']
