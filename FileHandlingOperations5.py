new_file = open("NewFile.txt","x")
new_file.close()

import os
print("Checking whether file exists...")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("This file does not exist")
    
my_file = open("my_file.txt","w")
my_file.write("Hi! I am Penguin and I am 1 year old.")
my_file.close()

os.remove("Codingal.txt")