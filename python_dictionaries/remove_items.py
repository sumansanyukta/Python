#There are several methods to remove items from the dictionary.
thisdict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(thisdict)

#pop() method removes the specified item
thisdict.pop("age")
print(thisdict)

#popitem() method removes the last inserted item
print(thisdict.popitem())
print(thisdict)

#del keyword removes the specified item
thisdict = {'name': 'John', 'age': 30, 'city': 'New York'}
del thisdict["city"]
print(thisdict)

#clear() method empties the dictionary
thisdict.clear()
print(thisdict)

#del can also delete the dictionary completely
del thisdict
print("dictionary deleted")