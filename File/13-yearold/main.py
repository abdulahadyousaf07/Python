#Table Function

def table(n):
    table = ""
    for i in range(1,11):
        table += f"{n} * {i} = {n*i}\n"
        
    with open(f"13-yearold/table_{n}.txt" , "w") as f:
        f.write(table)
  
#Main Body
      
for i in range(2,21):
        table(i)       