#filter(function , inputList)  //Syntax
#As compare to map() it removes the elements from the list that do not satisfy condition and in map() case the map() do not remove it
#At the time of printing we need to convert it into list otherwise we get the reference of the map object

def even(n):
    if(n%2 == 0):
        return True
    return False

onlyEven = [1 , 2 , 3 , 4 , 5]
filterList = filter(even , onlyEven)

print(list(filterList))
