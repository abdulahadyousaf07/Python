from functools import reduce

a = [1 , 20 , 15 , 22 , 43 , 150 , 200]

def greater(a , b):
    if(a>b):
        return a
    return b

f = reduce(greater , a)
print(f)