#map(function , inputList)  //Syntax
#It applies function to all items in the inputList
#At the time of printing we need to convert it into list otherwise we get the reference of the map object

l = [1 , 2 , 3 , 4 , 5]
#Lambda Function
square = lambda n:n*n

sqList = map(square , l)
#Convert the sqList into list (reference -> list)
print(list(sqList))
