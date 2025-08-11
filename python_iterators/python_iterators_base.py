# An iterator is an object that contains a countable number of values
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Even strings are iterable objects
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#looping through an Iterator
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)

mystr = "banana"
for x in mystr:
    print(x)