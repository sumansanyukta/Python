#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

thisdict = {
    "brand":"Ford",
    "model":"Mustang",
    "year":1964,
    "electric": False,
    "colors": ["red", "white", "blue"],
}

print(thisdict)

print(thisdict["brand"])
print(len(thisdict))
print(type(thisdict))
print(type(thisdict["brand"]))

#dict() constructor
thisdict2 = dict(brand = "Ford", model ="Mustang", year = 1964)
print(thisdict2)