#Python Scope

#Local scope - a variable inside the a function belongs to the local scope of that function, and can only be used inside that function

def myfunc():
    x=300
    print(x)

myfunc()

#function inside function
#the local variable can be accessed from a function within the function:

def myfunc():
    x=300
    def myinnerfunc():
        print(x)
    myinnerfunc()
myfunc()

#Global scope
x=300

def myfunc():
    print(x)

myfunc()
print(x)

x=300
def myfunc():
    x=200
    print(x)

myfunc()
print(x)

#glabal keyword
def myfunc():
    global x
    x = 300

myfunc()
print(x)

x=300
def myfunc():
    global x
    x = 200

myfunc()
print(x)