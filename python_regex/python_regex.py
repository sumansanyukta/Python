import re
txt = "The rain in Spain"
x = re.search("^The.*Spain$",txt)

if x:
    print("Yes! we have a match!")
else:
    print("no match")


import re

txt = "The rain in Spain"
x = re.findall('ai', txt)
y = re.findall("Portugal", txt)
z = re.search("\s", txt)

a = re.split("\s", txt)
b = re.split("\s", txt,1)
c = re.sub("\s", "9", txt)
print(x)
print(y)
print("The first white-space character is located in position:", z.start())
print(a)
print(b)
print(c)


