a = int(input("Enter a number : "))
b = int(input("Enter a number : "))

if(b == 0):
    raise ZeroDivisionError("Hey , Don't do this !!")

else:
    print(f"The a/b = {a/b}")