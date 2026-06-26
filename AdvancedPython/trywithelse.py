#The code goes inside i ELSE block if try successfully run
#If try fail then it do not goes in the else block

try:
    a = int(input("Enter a number : "))
    print(a)
    
except Exception as e:
    print(e)
    
else:
    print("I am inside else")