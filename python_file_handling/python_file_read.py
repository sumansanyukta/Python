#import os

# Get the absolute path of a file
#file_path = "demofile.txt" # This is a relative path
#absolute_path = os.path.abspath(file_path) 
myfile = "/Users/sanyuktasuman/Documents/GitHub/python_basics/Python/Python/python_file_handling/demofile.txt"
f= open(myfile)
print(f.read())
f.close()

with open (myfile) as f:
    print(f.read())

with open(myfile) as f:
    print(f.read(5))

with open(myfile) as f:
    print(f.readline())
    print(f.readline())

with open(myfile) as f:
    for x in f:
        print(x)