#to remove an item in a set, you can use the remove() or discard() methods
myset = {1, 2, 3, 4}
print(myset)
myset.remove(2)
print(myset)
myset.discard(3)
print(myset)

#you can use pop() to remove and return an arbitrary item from the set, but this will be random
myset = {1, 2, 3, 4}
print(myset)
x = myset.pop()
print(x)

#clear the set using the clear() method
myset.clear()
print(myset)

#del will delete the set completely
myset = {1, 2, 3, 4}
print(myset)
del myset
print("myset deleted") 
