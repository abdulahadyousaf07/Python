# Walrus Operator => :=
# Without Walrus 

n = len("Hel")
if n <= 3:
    print("More Letter")
else:
    print("Less Letter")
    
# With Walrus
if n := len("Hello") <= 3:
    print("More Letter")
else:
    print("Less Letter")