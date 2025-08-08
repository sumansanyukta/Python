#accessing item in a dictionary
thisdict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(thisdict["name"])
print(thisdict["age"])
print(thisdict["city"])

print(thisdict.get("name"))

#the key() method will return a list of all the keys in the dictionary
print(thisdict.keys())
