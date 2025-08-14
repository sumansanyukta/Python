myfile = "/Users/sanyuktasuman/Documents/GitHub/python_basics/Python/Python/python_file_handling/demofile.txt"
with open(myfile, "a") as f:
    f.write("Now the file has more content!")

with open(myfile) as f:
    print(f.read())

#overwriting existing file
with open(myfile,"w") as f:
    f.write("Woops! I have deleted the content!")

with open(myfile) as f:
    print(f.read())

f =open("mynewfile.txt","x")
f.close()

import os
if os.path.exists(myfile):
    os.remove(myfile)
else:
    print("The file does not exist")

