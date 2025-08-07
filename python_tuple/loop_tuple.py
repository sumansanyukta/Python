#Loof through a tuple, you can use a for loop
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)

#Loop through the tuple using range and len
thistuple2 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
for i in range(len(thistuple2)):
    print(thistuple2[i])

#Loop through the tuple using a while loop
i = 0
while i <len(thistuple2):
    print(thistuple2[i])
    i = i +1
