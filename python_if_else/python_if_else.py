a = 5
b = 10
if a<b:
    print("a is less than b")

#elif 

a = 10
b = 33
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is less than b")


# You can also use the if statement without an else or elif clause
a = 200
b = 33
if b>a:
    print("b is greater than a")
else:
    print("a is greater than b")

#shorthand 
if a>b: print("a is greater than b")

#shortand with if else
a = 330
b = 330
print("A") if a > b else print("B")
#shortand with if else and multiple conditions
a = 330
b = 330
print("A") if a > b else print("=") if a ==b else print("B")

#AND 
a = 200
b = 33
c = 500
if a > b and a > c:
    print("a is the greatest")
elif b > a or c > a:
    print ("b, c both are greater than a")
else: 
    print("a is not the greatest")

#NOT
a = 200
b = 33
c = 500
if not a ==b:
    print("a is not equal to b")

#Nested if
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

#pass statement
a = 33
b = 200
if b>a:
    pass