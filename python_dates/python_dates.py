import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

#Creating date objects

import datetime
x =datetime.datetime(2025,11,8)
print(x)

print(x.strftime("%a")) #weekday, shortversion
print(x.strftime("%A")) #weekday, long version
