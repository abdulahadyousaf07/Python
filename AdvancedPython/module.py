def myFunc():
    print("Hello World!")
    
myFunc()
#If a file containing print(__name__) is run directly, it prints "__main__"
#If that file is imported into another file, it prints its own module name (file name)
print(__name__)

if(__name__ == "__main__"):
    print("Freedom")