def divisible5(n):
    if n%5 == 0:
        return True
    return False

a = [1 , 20 , 15 , 22 , 43 , 150]
f = list(filter(divisible5 , a))
print(f)