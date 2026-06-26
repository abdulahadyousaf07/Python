def win(a : str) -> None:
    print(f"{a} has Win the Game")
    
def lose(a : str) -> None:
    print(f"{a} has Lose the Game")

def tie(a : str , b : str) -> None:
    print(f"Neither {a} nor {b} wins. Game Tied!!")
    
print("--------------------")
print("Let's Start The Game")
print("Select : ")
print("1. S for Scissor")
print("2. R for Rock")
print("3. P for Paper")

x = input("Enter your Choice as an A : ")
a = x.upper()
y = (input("Enter your Choice as an B : "))
b = y.upper()

if(a == b):
    tie("A" , "B")
    
#S possibilities
elif(a == "S" and b == "R"):
    win("A")
    lose("B")
    
elif(a == "S" and b == "P"):
    win("A")
    lose("B")
    
#R possibilities
elif(a == "R" and b == "S"):
    win("A")
    lose("B")
    
elif(a == "R" and b == "P"):
    win("B")
    lose("A")
    
#P possibilities
elif(a == "P" and b == "S"):
    win("B")
    lose("A")
    
elif(a == "P" and b == "R"):
    win("A")
    lose("B")

