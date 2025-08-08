#union() method return a new set with all item from both sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)
print(set3)

# You can also use the '|' operator to achieve the same result
set4 = set1|set2
print(set4)


#join mutiple sets using union() method
set5 = {1, 2, 3}
set6 = {4, 5, 6}
set7 = {7, 8, 9}
set8 = set5.union(set6, set7)
set9 = set5|set6|set7
print(set9)
print(set8)

#join a set and a tuple using union() method
set10 = {1, 2, 3}
tuple1 = (4, 5, 6)
set11 = set10.union(tuple1)
print(set11)
# You can also use the '|' operator to join a set and a tuple
set12 = set10 | set(tuple1)
print(set12)


#update() method modifies the set in place by adding elements from another set or iterable
set13 = {1, 2, 3}
set14 = {3, 4, 5}
set13.update(set14)
print(set13)

#intersection () method returns a new set with elements common to both sets
set15 = {1, 2, 3}
set16 = {2, 3, 4}
set17 = set15.intersection(set16)
set18 = set15 & set16
print(set18)            
print(set17)

#the intersection_update() method modifies the set in place by keeping only elements found in both sets
set19 = {1, 2, 3}
set20 = {2, 3, 4}
set19.intersection_update(set20)
print(set19)

#difference() method returns a new set that will contain elements that are in the first set but not in the second set
set21 = {"apple", "banana", "cherry"}
set22 = {"banana", "cherry", "date"}
set23 = set21.difference(set22)
print(set23)
#Note: unique to the first set, and 2nd set is ignored
#You can also use the '-' operator to achieve the same result
set24 = set21 - set22
print(set24)

#difference_update() method modifies the set in place by removing elements found in another set
set25 = {"apple", "banana", "cherry"}
set26 = {"banana", "cherry", "date"}
set25.difference_update(set26)
print(set25)

#symmetric_difference() method will keep only the elements that are NOT present in both sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft","apple"}
set3 = set1.symmetric_difference(set2)
print(set3)
#You can also use the '^' operator to achieve the same result
set4 = set1 ^ set2
print(set4)

#symmetric_difference_update() method modifies the set in place by keeping only elements that are NOT present in both sets
set5 = {"apple", "banana", "cherry"}
set6 = {"google", "microsoft","apple"}
set5.symmetric_difference_update(set6)
print(set5)
