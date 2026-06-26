#The finally blocks runs every time even if try fail or try become successful
#It's main purpose is in function when we use return in try or except then it also runs

#Without finally
def divide1():
    try:
        a = int(input("Enter a number : "))
        print(a)
        return
    
    except Exception as e:
        print(e)
        return
    
    print("I am inside of finally")
        
        
#With finally
def divide2():
    try:
        a = int(input("Enter a number : "))
        print(a)
        return
    
    except Exception as e:
        print(e)
        return
    
    finally:
        print("I am inside of finally")
        
divide1()
divide2()