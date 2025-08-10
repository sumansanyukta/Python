#Inheritance allows us to define a class that inherits all the methods and properties from another class

#Create a parent Class

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def printname(self):
        print(self.fname, self.lname)

x = Person("John", "Doe")
x.printname()

# Create a child class
class Student(Person):
    def __init__(self, fname,lname):
        Person.__init__(self,fname,lname)

x = Student("Mike", "Olsen")
x.printname()

class Student (Person):
    def __init__(self,fname,lname):
        super().init__(fname,lname)
#super () function will make the child class inherit all the methods and properties from its parent:

# Add properties
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname,lname)
        self.graduationyear = year

x = Student("Mike", "Olsen",2019)

# Add method
class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduation = year
    def welcome(self):
        print("Welcome", self.fname, self.lname, "to the class of", self.graduation)
x = Student ("Mike", "Olsen",2024)
x.welcome()