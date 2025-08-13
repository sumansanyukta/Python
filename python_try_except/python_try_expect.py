# python Try Expect
# try block lets you test a block of code for errors
# the except bock lets you handle the errror
# else lock lets you excute code when there is no error
# The finally block lets you exceute code, regardless of the result of the try-and except blocks

try:
    print(x)
except:
    print("An exception occured")

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("something else went wrong")


try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")


try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The try except is finished")

try:
    f = open("demofile.txt")
    try:
        f.write("Lorem Ipsum")
    except:
        print("something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")


x = 1
if x < 0:
    raise Exception ("Sorry, no numbers below zero")

x = 4
if not type(x) is int:
    raise TypeError("Only integers are allows")
