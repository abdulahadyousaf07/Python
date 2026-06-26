class Shape:
    def __init__(self , i , j , k):
        self._i = i
        self._j = j
        self._k = k
        
    @property 
    def i(self):
        return self._i
    
    @i.setter 
    def i(self , value):
        self._i = value
        
    @property 
    def j(self):
        return self._j
    
    @j.setter 
    def j(self , value):
        self._j = value
        
    @property 
    def k(self):
        return self._k
        
    @k.setter 
    def k(self , value):
        self._k = value
        
    
a = Shape(1, 2, 4)
print("Before setting values")
print(f"{a.i}i + {a.j}j + {a.k}k")

print("After setting values")
a.i = 9
a.j = 8
a.k = 7
print(f"{a.i}i + {a.j}j + {a.k}k")
    
        
        