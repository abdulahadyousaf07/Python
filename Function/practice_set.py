# a1 = int(input("Enter number 01 : "))
# a2 = int(input("Enter number 02 : "))
# a3 = int(input("Enter number 03 : "))
# a4 = int(input("Enter number 04 : "))

# if(a1 > a2 and a1 > a3 and a1 > a4 ):
#     print("A1 is greater : ", a1)
    
# if(a2 > a1 and a2 > a3 and a2 > a4 ):
#     print("A2 is greater : ", a2)
    
# if(a3 > a2 and a3 > a1 and a3 > a4 ):
#     print("A3 is greater : ", a3)
    
# if(a4 > a2 and a4 > a3 and a4 > a1 ):
#     print("A4 is greater : ", a4)
    
# if(a1 == a1 == a3 == a4):
#     print("The all numbers are equal")

## Functions and Recursion Practice Set

# def greatestNumber(a , b , c):
#     if(a>b and a>c):
#         print(f"{a} is greater number")
#     elif(b>a and b>c):
#         print(f"{b} is greater number")
#     elif(c>a and c>b):
#         print(f"{c} is greater number")
#     elif(a == b == c):
#         print("Equal Numbers")
        
# x = int(input("Enter Number 01 : "))
# y = int(input("Enter Number 02 : "))
# z = int(input("Enter Number 03 : "))

# greatestNumber(x , y , z)

# def conversion(temp):
#     return (temp * (9/5))+32
    
# a = int(input("Enter Temperature in Celsius : "))
# print(f"Temperature in Fahrenheit" , {conversion(a)})

# def sum(n):
#     if(n == 1):
#         return 1
#     elif(n == 0):
#         return "No sum"
#     elif(n > 1):
#         return n + sum(n-1)

# a = int(input(("Enter Number : ")))
# b = sum(a)
# print("The Sum is : ", b)


# def pattern(n):
#     if(n == 0):
#         return
#     print("*" * n)
#     pattern(n-1)
    
# a = int(input("Enter number : "))
# pattern(a)

# def rem(l , word):
#     n = []
    
#     for item in l:
#         if not(item == word):
#             n.append(item.strip(word))
#     return n

# l = ["Harry" , "ann" , "an"]
# print(rem(l , "an"))

def table(n):
    for i in range (1 , 11):
        print(f"{n} * {i} = {n*i}")
        
a = int(input("Enter the number : "))
table(a)        