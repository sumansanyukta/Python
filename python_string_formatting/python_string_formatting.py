txt = f"the price is 49 dollars"
print(txt)

price = 59
txt = f"The price is {price} dollar"
txt2 = f"The price is {price:.2f} dollar"
txt3 = f"the price is {95:.2f} dollars"
txt4 = f"The price is {20*59} dollars"
print(txt)
print(txt2)
print(txt3)
print(txt4)


price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"

print(txt)

fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)

def myconverter(x):
    return x * 0.3048

txt = f"the plane is flying at a {myconverter(3000)} meter altitude"
print(txt)