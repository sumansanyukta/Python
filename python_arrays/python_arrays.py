# LISTS as an arrays

#Arrays are used to store multiple values in one single variable:

car = ["ford", "bmw","Volkswagen"]
print (car[0])
print (car[1])
print (car[2])

print(len(car))

#looping through an array
for x in car:
    print(x)

#adding element to an array using append()
car.append("honda")

print(car)
car.pop(1)
print (car)
car.remove("ford")
print(car)