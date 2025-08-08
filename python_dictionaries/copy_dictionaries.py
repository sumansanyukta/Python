#copy dictionary
thisdict = {"brand": "Nike", "model": "Air Max", "year": 2021}
thisdict2 = thisdict.copy()
print(thisdict2)

#another way to copy a dictionary is to use the dict() constructor
thisdict3 = dict(thisdict)
print(thisdict3)