#Python for loops
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set or a string)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

#looping through a string
for x in 'banana':
    print(x)

a = "blueberry"
for x in a:
    print (x)

#the break statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == 'banana':
        break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == 3:
        break
    print(x)

#continue statement
# do not print banana

fruits = ["apple", "banana", "cherry", "kiwi", "dates"]
for x in fruits:
    if x == 'banana':
        continue
    print(x)

#range function
for x in range(6):
    print(x)

#range function with parameters
for x in range(2,6):
    print(x)

# ELSE in for loop
for x in range(6):
    print(x)
else:
    print("range is finished")

#else will not be executed if the loop is stopped by a break
for x in range(6):
    if x == 3: break
    print(x)
else:
    print("range is over")

#nested loop
#The "inner loop" will be executed one time for each iteration of the outer loop

adj = ["red","big","tasty"]
fruits = ["apple", "banana","cherry"]
for x in adj:
    for y in fruits:
        print(x,y)

# the pass statement
for x in [0,1,2]:
    pass 