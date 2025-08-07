thislist = ["apple", "mango", "banana", "kiwi", "cherry", "orange"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = ["apple", "mango", "banana", "kiwi", "cherry", "orange"]
thislist.sort(reverse = True)
print(thislist)

def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key =myfunc)
print(thislist)

thislist = ["apple", "mango", "Banana", "kiwi", "cherry", "orange"]
thislist.sort(key=str.lower)
print(thislist)

thislist = ["apple", "mango", "banana", "kiwi", "cherry", "orange"]
thislist.reverse()
print(thislist)
