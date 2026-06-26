#Without List Comprehension
myList1 = [1 , 2 , 3 , 4 , 5]

squaredList = []
for i in myList1:
    squaredList.append(i*i)

print(squaredList)


#new_list = [expression for item in iterable] //Syntax
#With List comprehension 
print("---------------------")
myList2 = [1 , 2 , 3 , 4 , 5]
squareList = [i*i for i in myList2]
print(squareList)
