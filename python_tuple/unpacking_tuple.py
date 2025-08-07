#packing a tuple 
thistuple = ("apple", "banana", "cherry")

#unpacking the tuple
(green, yellow, red) = thistuple
print(green)
print(yellow)
print(red)

#using an aesterisk to unpack
thistuple2 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
(green, yellow, *red) = thistuple2
print(green)
print(yellow)
print(red)
(green, *yellow, red) = thistuple2
print(green)
print(yellow)
print(red)