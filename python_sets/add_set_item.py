#once a set is created, you cannot chnage its items, but you can add new items
#using the add() method

myset = {1, 2, 3}
myset.add(4)
print(myset) 

#add sets to sets
myset = {1, 2, 3}
yourset = {4, 5}
myset.update(yourset)
print(myset)

