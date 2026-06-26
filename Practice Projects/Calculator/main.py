## Functions
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b


## Interface
print("----- Welcome to Calculator -----")
print("Select :")
print("A for Addition")
print("S for Subtraction")
print("D for Division")
print("M for Multiplication")
print("Type EXIT to quit")

while True:

    choice = input("Enter the Operator : ").upper()

    if choice == "EXIT":
        print("Thanks for choosing us !!")
        break

    elif choice not in ["A", "S", "M", "D"]:
        print("Invalid Operator")
        continue

    a = int(input("Enter Number 01 : "))
    b = int(input("Enter Number 02 : "))

    match(choice):

        case "A":
            print(f"Answer = {add(a,b)}")

        case "S":
            print(f"Answer = {sub(a,b)}")

        case "M":
            print(f"Answer = {mul(a,b)}")

        case "D":
            if b == 0:
                print("Cannot divide by zero")
            else:
                print(f"Answer = {div(a,b)}")