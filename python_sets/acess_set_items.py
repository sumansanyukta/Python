#You cannot access set items by index or key, as sets are unordered collections. but you can use loops to interate items
myset = {"apple", "banana", "cherry"}
for x in myset:
    print(x)

#You can also check if an item is in a set using the 'in' keyword
print("banana" in myset)
print("banana" not in myset)

#add any iterables to the set using the update() method
mylist = ["orange", "kiwi"]
myset.update(mylist)
print(myset)