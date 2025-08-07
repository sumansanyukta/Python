tuple1 = ("apple", "banana", "cherry")
tuple2 = ("orange", "kiwi", "melon", "mango")

# Joining two tuples
joined_tuple = tuple1 + tuple2
print(joined_tuple)

#multiply tuples
fruit_tuple = ("apple", "banana", "cherry")
mytuple = fruit_tuple * 2
print(mytuple)

#tuple methods
print(len(joined_tuple))  # Length of the tuple
print(max(joined_tuple))  # Maximum value in the tuple
print(min(joined_tuple))  # Minimum value in the tuple
print(joined_tuple.count("apple"))  # Count occurrences of "apple"
print(joined_tuple.index("kiwi"))  # Index of "kiwi" in the tuple
print(joined_tuple.index("melon", 3))  # Index of "melon" after index 3
print(joined_tuple.index("banana", 0, 5))