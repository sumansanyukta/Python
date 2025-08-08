thisdict = {"brand": "Nike", "model": "Air Max", "year": 2021}
# print all keys in the dictionary
for x in thisdict:
    print(x)

# print all values in the dictionary
for x in thisdict:
    print(thisdict[x])

# you can also use values() to return values of the dictionary
for x in thisdict.values():
    print(x)

# you can use keys() to return keys of the dictionary
for x in thisdict.keys():
    print(x)

# loop through both keys and values
for x,y in thisdict.items():
    print(x,y)
