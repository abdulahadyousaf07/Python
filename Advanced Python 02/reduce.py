#reduce(function, iterable)  //Syntax
#Applies a function cumulatively to reduce a list to a single value.
#First two elements , Applies the function , Then takes the result and the next element , Repeats until one value is left
#  1 2 3 4 
#  |_| | |
#   |  | |
#   3  | |
#   |__| |
#     |  |
#     6  |
#     |__|
#      |
#      10
# The above one perform sum because there is sum func below it is different one also 
#10 is answer or Output of the following code 

from functools import reduce

def sum(a , b):
    return a + b

l = [1 , 2 , 3 , 4]
print(reduce(sum , l))