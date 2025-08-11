# Create Class

class MyClass:
    x = 5

# Use the class named Myclass to create objects:

p1 = MyClass()
print(p1.x)


# __init__() Method

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# Note : the __init__() method is called automatically every time the class is being used to create a new object

# __str__() Method

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person ("John", 36)
print(p1)

#Create Methods
#You can create your own methods inside ojects.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person ("John", 36)
p1.myfunc()
print(p1)

p1.age = 40

print(p1.myfunc())

del p1.age #age property
del p1 #delete object