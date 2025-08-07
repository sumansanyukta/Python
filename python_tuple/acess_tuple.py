# You can aceess tuple elements using indexing
thistuple = ("apple", "banana", "cherry")
print(thistuple[0])
print(thistuple[1])
print(thistuple[2])

# Negative indexing can also be used
print(thistuple[-1])
print(thistuple[-2])
print(thistuple[-3])

#range of indexes can be used to access multiple elements
thistuple = ("apple", "banana", "cherry", "date", "elderberry")
print(thistuple[2:5])
print(thistuple[:4])
print(thistuple[1:])
#range of negative indexes
print(thistuple[-4:-1])

#check if an item exists in a tuple
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in thistuple")
