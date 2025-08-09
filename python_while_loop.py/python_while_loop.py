# The while loop - we can execute a set of statements as long as condition is true

i = 0
while i< 6:
    print(i)
    i +=1

# break statement - with break statement we can stop the loop even if the while loop condition is true

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i +=1

# continue to the next iteration if i is 3

i = 0
while i < 6:
    i +=1
    if i == 3:
        continue
    print(i)

# The else statement - with the else statement we can run a block of code once when the condition is no longer true

i = 1
while i < 6:
    print (i)
    i +=1
else:
    print("i is no longer less than 6")