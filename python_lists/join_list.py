list1 = ["a", "b", "c"]
list2 = [1,2,3]
list3 = list1 + list2
print(list3)


list4 = ["x", "y", "z"]
list5 = [4, 5, 6]

for x in list4:
    list4.append(x)
print(list4)

list1.extend(list2)
print(list1)