thisdict = {"brand": "Nike", "model": "Air Max", "year": 2021}
print(thisdict["year"])
thisdict["year"] = 2022
print(thisdict["year"])

# update() method can also be used to change the value of an existing key
thisdict.update({"year": 2023})
print(thisdict["year"])
thisdict.update({"color": "black"})
