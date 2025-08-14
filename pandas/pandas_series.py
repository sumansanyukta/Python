import pandas as pd

a = [1,7,2]

myvar = pd.Series(a)

print(myvar)
print(myvar[0])
print(myvar[1])
print(myvar[2])

a = [6,8,29]

myvar = pd.Series(a, index = ["x","y","z"])

print(myvar)
print(myvar["y"])