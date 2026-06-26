#Without Enumerate 
l = [5 , 25 , 50 , 100 , 200]
index = 0
for item in l:
    print(f"{index} = {item}")
    index += 1
    
#enumerate(iterable , start = n)  //Syntax
#where n = 1 ,2 ,3 .......
    
#With Enumerate
print("----------")
l = [5 , 25 , 50 , 100 , 200]
index = 0
for index , item in enumerate(l):
    print(f"{index} = {item}")
    
#With Enumerate starting index from 1
print("----------")
l = [5 , 25 , 50 , 100 , 200]
index = 0
for index , item in enumerate(l , start = 1):
    print(f"{index} = {item}")
