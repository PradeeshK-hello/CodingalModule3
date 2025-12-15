do = open("Codingal.txt","r")
print(do.read())
do.close()

do2 = open("Codingal.txt","r")
print(do2.read(9))
do2.close()

do3 = open("Codingal.txt","r")
print(do3.readlines(0))
do3.close()

do4 = open("Codingal.txt","r")
print(do4.readlines(3))
do4.close()

do5 = open("Codingal.txt","r")
print(do5.readlines())
do5.close()