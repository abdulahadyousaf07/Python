#we use it to show error message instead of program crashing we use in it TRY EXCEPT , IF-ELSE 

#If we want to display our message on error
try:
    a = int(input("Enter a number : "))
    print(a)
    
except:
    print("Invalid Number")
    
print("Thanks!")

#If we want to display the error from computer 
try:
    a = int(input("Enter a number : "))
    print(a)
    
except Exception as e:
    print("Invalid Number")
    
print("Thanks!")