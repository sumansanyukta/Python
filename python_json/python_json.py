import json

x = '{"name": "John", "age":30, "city":"New York"}'

#parse json
y = json.loads(x)

# the result is a python dictionary:
print(y)
print(y["age"])

#convert from python to json
import json
# a Python object (dict):

x = {
    "name": "John",
    "age": 36,
    "city": "New York"
}

y = json.dumps(x)

#the result is a json string
print(y)

#You can convert python objects of the following types, into JASON strings:

import json
print(json.dumps(["apple", "banana", "cherry"]))
print(json.dumps(("marigold", "rose")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


import json

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": None,
    "cars": [
        {"model": "BMW 230", "mpg":27.5},
        {"model": "Ford Mustang", "mpg":27.5}
        ]
}

print(json.dumps(x))
print(json.dumps(x, indent=4))
print(json.dumps(x, indent=4, separators=(". "," = ")))
print(json.dumps(x, indent=4, sort_keys=True))