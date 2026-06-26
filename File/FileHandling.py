#f = open("file.txt" , "r")
# data = f.read()
# print(data)
# f.close()

# f1 = open("myfile.txt" , "w")
# data1 = "Hi I am AI/ML engineer"

# f1.write(data1)
# f1.close()

f = open("file.txt")
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()
    
f.close()