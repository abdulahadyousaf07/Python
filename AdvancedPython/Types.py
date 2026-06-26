from typing import List , Union , Tuple , Dict

n : int = 5
name : str = "Harry"

def sum(a:int , b:int) -> int :
    return a+b

c = sum(2 , 2)
print(c)
print(type(c))

numbers : List[int] = [1 , 2 , 3]
person : Tuple[str , int] = ("Ali" , 123)
scores : Dict[str , int] = {"David":90 , "Henry":80}

print(numbers)
print(person)
print(scores)