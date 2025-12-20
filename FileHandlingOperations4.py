with open("Codingal.txt","w") as file:
    file.write("Hi! I am Penguin and am 1 year old.")
file.close() 

with open("Codingal.txt","r") as file:
    data = file.readlines()
    print("Words in this file are...")
    for line in data:
        word = line.split()
        print(word)
file.close()        