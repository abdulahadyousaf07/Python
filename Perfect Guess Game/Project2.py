import random
print("----- Welcome To The Perfect Guess Game -----")

##Generate a Random Number
n = random.randint(1,100)
a = -1
i = 1
while(a!=n):
    
    a = int(input("Guess a Number : "))
    
    
    if(a == n):
        print("CONGRATS YOU WIN !!")
        break
    
    else:   
        print("You entered Wrong number")
        print("Try Again !!")
        print(f"HINT = {n-1}")
        
    i += 1
    
print(f"You win in #{i} attempt")
print("----- Thanks for Playing the Game -----")
    
