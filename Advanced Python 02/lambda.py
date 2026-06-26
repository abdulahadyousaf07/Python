#We can do simple math function in variable
# variableName = lambda arguments : expression //Syntax
 
square = lambda n : n*n

a = int(input("Enter the number : "))
print(f"The Square of {a} is {square(a)}")