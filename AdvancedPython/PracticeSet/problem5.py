a = int(input("Enter number to which you want table : "))
n = 1
while(n <= a):
    
    with open("table.txt" , "a") as f:
        table = [n*i for i in range(1 , 11)]
        f.write(f"Table of {n} is {str(table)} \n")
        
    n += 1