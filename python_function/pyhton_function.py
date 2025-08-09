# A function is a block of code which only runs when is is called.
#you can pass data, known as parameter, into a function
# A function can return data as a result

#creating a function using def keyword:

def my_func():
    print("Hello from a function")

my_func()

#Arguments
#Information can be passed into functions as an arguments

def my_func(fname):
    print(fname + " Refsnes")

my_func("Emil")
my_func("Tobias")
my_func("Linus")


#arbitrary arguments *args
# if you do not know how many arguments that will be passed into your function, add a * before the parameter name in the functio definition

def my_func(*kids):
    print("The youngest child is " + kids[-1])

my_func("Emmil", "Tobias", "Linus", "eva")

#keyword arguments
def my_func(child1, child2, child3):
    print("The youngest child is" + child3)

my_func(child1 = "Emil", child2 ="Tobias", child3 ="Linus")


#Arbitrary keyword Arguments, **kwargs
#if you do not know how mnay keywords arguments that will be passed into your function, add two asteriks ** before parameters name

def my_func(**kid):
    print("His last name is " + kid["lname"])

my_func(fname = "Tobias", lname = "Refsnes")


#default parameter value
# if we call the function without argument, it uses the default value:

def my_func(country = "Norway"):
    print ("I am from " + country)

my_func("Sweden")
my_func("India")
my_func()
my_func("Brazil")

#passing a list as an Argument
#you can send any types of arguments to a function (string, number, list, dictionary)

def my_func(food):
    for x in food:
        print(x)
fruits = ["apple","banana","apple"]

my_func(fruits)

# return values
def my_func(x):
    return 5* x

print(my_func(3))
print(my_func(4))

#the pass statements
#function definitions cannot be empty, but if you need it to be empty fo some reason, use pass statement

def my_func():
    pass


#Positional-Only Arguments

def my_func(x, /):
    print(x)

my_func(3)
# error when my_func(x = 3)

#keyword-only Arguments
# to specify that a function can have oly keyword arguments, add *, before the arguments:

def my_func(*,x):
    print(x)

my_func(x=3)

#combine Positional-Only and Keyword-Only
def my_func(a,b, /, *, c,d):
    print(a + b + c+ d)

my_func(5,6,c =7, d =8)