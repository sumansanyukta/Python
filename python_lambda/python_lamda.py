#A lambda function is a small anonymous function
#syntax lambda arguments : expression

x = lambda a : a + 10
print(x(5))

#lambda functon can take any number of arguments
x = lambda a,b : a * b
print(x(5,6))

x = lambda a,b,c : a + b + c
print(x(4,6,7))

#lambda with function
def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))


def myfunc(n):
    return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))


def myfunc(n):
    return lambda a : a * n

mydoubler(2)
mytripler(3)

print(mydoubler(11))
print(mytripler(6))