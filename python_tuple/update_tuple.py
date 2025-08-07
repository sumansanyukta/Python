#change tuple value - convert to list, change convert back to tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)
temp_list = list(thistuple)
temp_list[1] = "blueberry"
thistuple = tuple(temp_list)
print(thistuple)

#add items to a tuple - convert to list, add item, convert back to tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)
temp_list = list(thistuple)
temp_list.append("date")
thistuple = tuple(temp_list)
print(thistuple)

#add tuple to another tuple 
thistuple = ("apple", "banana", "cherry")
y = ("date", "elderberry")
thistuple += y
print(thistuple)

#remove items from a tuple - convert to list, remove item, convert back to tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)
temp_list = list(thistuple)
temp_list.remove("banana")
thistuple =tuple(temp_list)
print(thistuple)

#remove entire tuple - convert to list, clear list, convert back to tuple
thistuple = ("apple", "banana", "cherry")
del(thistuple)
print("Tuple deleted")